@echo off
python scripts/check_requirements.py requirements.txt
if errorlevel 1 (
    echo Installing missing packages...
    python3.8 -m pip install -r requirements.txt
)
python3.8 -m autogpt %*
pause