import os.path
import sys
import collections
import json
from fpdf import FPDF

from Engine.Person import *

GENERATOR_DATA = False

# ALIVENESS states
INVALID_STATE = 0
POTENTIAL_ARRIVE_STATE = 1
CONFIRM_ARRIVE_STATE = 2
POTENTIAL_DEPARTURE_STATE = 3
CONFIRM_DEPARTURE_STATE = 4
FINISH_STATE = 5

configData = ConfigData()


# Update person state
def stateUpdate(person: Person, probe: ProbeRequest):
    if person.LivenessState == INVALID_STATE or \
            person.LivenessState == FINISH_STATE or person.getMostRecentTime() is None:
        return POTENTIAL_ARRIVE_STATE

    if person.LivenessState == POTENTIAL_ARRIVE_STATE:
        if timeBetween2(person.getMostRecentTime(), probe.time) < float(configData.ArriveThreshold):
            return CONFIRM_ARRIVE_STATE
        else:
            return INVALID_STATE
    elif person.LivenessState == CONFIRM_ARRIVE_STATE:
        if timeBetween2(person.getMostRecentTime(), probe.time) >= float(configData.ArriveThreshold):
            return POTENTIAL_DEPARTURE_STATE
        else:
            return CONFIRM_ARRIVE_STATE
    elif person.LivenessState == POTENTIAL_DEPARTURE_STATE:
        if timeBetween2(person.getMostRecentTime(), probe.time) < float(configData.ArriveThreshold):
            return CONFIRM_ARRIVE_STATE
        elif timeBetween2(person.getMostRecentTime(), probe.time) > float(configData.DepartureThreshold):
            return CONFIRM_DEPARTURE_STATE
    return POTENTIAL_DEPARTURE_STATE


#     @ dict fields:
#     @   time
#     @   unit_id
#     @   person_id
#     @   meters
#     @   dBm
#   [{'time': '2022-04-11 23:51:23.158938', 'unit-id': 'point1', 'dBm': '-16', 'Person': '1', 'meters': '100'},
#   {'time': '2022-04-11 23:52:23.158938', 'unit-id': 'point2', 'dBm': '-16', 'Person': '1', 'meters': '120'}]

def analyze(dir_path: str, date: str, data: list[dict]):
    # Output into log
    if GENERATOR_DATA:
        with open('C:\\Users\\USER\\Desktop\\test\\generateData.txt', 'r') as file:
            data_t = file.read().rstrip()
            data = json.loads(data_t)
    res_log = open(os.path.join(dir_path, "result_log" + date + ".log"), "w")
    print('---START ANALYZING ' + date + '---\n', file=res_log)
    print('---GET CONFIGURATION DATA---\n', file=res_log)
    configData.print(res_log)
    print("Number of Lines in data: ", len(data), file=res_log)
    print('', file=res_log)

    # Total number of Persons
    PersonsCounter = 0

    Persons = {}
    Results = []
    potentialDepartureSet = set()
    activateSet = set()

    # Setup Location Engine
    LocationData.locationsEngine = LocationsEngine(configData, data)

    # Last calculated probe time
    EndTime = ''

    # Sort data per person and time_stamp
    data_per_person = collections.defaultdict(list)
    for line in data:
        data_per_person[line['person_id']].append(line)

    for person_id in data_per_person.keys():
        data_per_person[person_id] = sorted(data_per_person[person_id], key=lambda x: x['time'])

    # States Machine Engine
    for person_id in data_per_person.keys():
        # Add new person for analyzing
        # print("Add new Person ID #", PersonsCounter, file=res_log)
        Persons[PersonsCounter] = Person(PersonsCounter)
        Persons[PersonsCounter].LivenessState = POTENTIAL_ARRIVE_STATE
        personID = PersonsCounter
        PersonsCounter += 1

        for probe in data_per_person[person_id]:
            probe_t = ProbeRequest(**probe)

            # check if probe is relevant by distance
            if abs(int(probe_t.dBm)) > abs(int(configData.SystemUpperLimit)):
                continue

            EndTime = probe_t.time

            # Cluster more than one person in this ID
            if Persons[personID].LivenessState == FINISH_STATE:
                # Add new person for analyzing
                # print("Add new Person ID #", PersonsCounter, file=res_log)
                Persons[PersonsCounter] = Person(PersonsCounter)
                Persons[PersonsCounter].LivenessState = POTENTIAL_ARRIVE_STATE
                personID = PersonsCounter
                PersonsCounter += 1

            # Calc person new validation state
            Persons[personID].LivenessState = stateUpdate(Persons[personID], probe_t)
            state_t = Persons[personID].LivenessState
            Persons[personID].addProbe(probe_t, configData)

            if state_t == CONFIRM_ARRIVE_STATE:
                activateSet.add(personID)
            if state_t == POTENTIAL_DEPARTURE_STATE:
                if personID in activateSet:
                    activateSet.remove(personID)
                potentialDepartureSet.add(personID)
            if state_t == CONFIRM_DEPARTURE_STATE:
                potentialDepartureSet.remove(personID)
                Results.append(Persons[personID])
                Persons[personID].LivenessState = FINISH_STATE

    # Check for valid IDs that still on potential departure state
    for person_id in potentialDepartureSet:
        if timeBetween2(Persons[person_id].getMostRecentTime(), EndTime) > int(configData.DepartureThreshold):
            Results.append(Persons[person_id])

    for person_id in activateSet:
        Results.append(Persons[person_id])
    print("---DONE ANALYZING---", file=res_log)
    print("Tot number of analyzed persons is: ", PersonsCounter, file=res_log)
    print("Tot number of confirm persons is: ", len(Results), file=res_log)
    print('Confirm persons are:', *Results, sep='\n- ', file=res_log)
    print('Confirm Crossing persons are:', file=res_log)
    c = 0
    for person in Results:
        if person.CrossingPerson:
            print(person.id, end=', ', file=res_log)  # Need to export summery into PDF!!
            c += 1
            if c % 5 == 0:
                print("", file=res_log)
    print('\nTotal confirm persons: ', c, file=res_log)
    print('\n\n\n\n', file=res_log)
    res_log.close()

    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()

    pdf.set_font("Arial", size=24)
    txt = "Smart Junction Analyze"
    pdf.cell(200, 10, txt=txt, ln=1, align='C')

    pdf.set_font("Arial", size=18)
    pdf.cell(200, 10, txt="Summary:", ln=1, align='L')
    pdf.cell(200, 10, txt="", ln=1, align='L')

    pdf.set_font("Arial", size=12)
    txt = "Total number of analyzed persons is: " + str(PersonsCounter)
    pdf.cell(200, 10, txt=txt, ln=1, align='L')
    txt = "Total number of valid persons is: " + str(len(Results))
    pdf.cell(200, 10, txt=txt, ln=1, align='L')
    txt = 'Total number of crossing persons is: ' + str(c)
    pdf.cell(200, 10, txt=txt, ln=1, align='L')
    pdf.cell(200, 10, txt="", ln=1, align='L')

    for person in Results:
        if person.CrossingPerson:
            txt = 'Person #' + str(person.id) + ":"
            pdf.cell(200, 10, txt=txt, ln=1, align='L')
            with open('out.txt', 'w') as f:
                print(person.locationsSummary(True), file=f)
                # insert the texts in pdf
                f.close()
            with open('out.txt', 'r') as f:
                for x in f:
                    pdf.cell(200, 10, txt=x, ln=1, align='L')
                f.close()

    # save the pdf with name .pdf
    pdf_path = os.path.join(dir_path, "SmartJunctionAnalyze" + date + ".pdf")
    pdf.output(pdf_path)
    return None
