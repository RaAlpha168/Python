@echo off
echo Downloading script from GitHub...

REM Download the Python script using curl
curl -o setup.py https://github.com/RaAlpha168/Python/blob/main/run.py

echo Running the Python script...
python setup.py

pause
