@echo off

for /f "delims=" %%i in ('where python') do set python_path=%%i

cd C:/Users/USER/Documents/smart_junction/GUI

C:\Users\USER\miniconda3\envs\smart_junction\python.exe  C:/Users/USER/Documents/smart_junction/GUI/SmartJunction.py"

pause