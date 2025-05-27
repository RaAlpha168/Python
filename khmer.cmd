@echo off
echo Downloading script from GitHub...

REM Correct raw URL (not the blob version)
curl -o run.py https://raw.githubusercontent.com/RaAlpha168/Python/main/run.py

echo Running the Python script...
python run.py

set /p=Press Enter to exit... <nul & pause >nul
