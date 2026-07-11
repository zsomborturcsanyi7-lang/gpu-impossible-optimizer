@echo off
setlocal
title IOL OMNIPOTENCE - GLOBAL SUPER MODE

echo ======================================================
echo    IOL OMNIPOTENCE - GLOBAL SUPER MODE
echo    Device: Acer Nitro
echo    Status: INITIALIZING...
echo ======================================================
echo.

:: Ellenorizzuk a rendszergazdai jogokat
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [FIGYELEM] Kerlek, futtasd ezt a fajlt RENDSZERGAZDAKENT
    echo a maximalis teljesitmenyert!
    echo.
    pause
)

:: Inditjuk a Globalis Szolgaltatast
python iol_global_service.py

pause
