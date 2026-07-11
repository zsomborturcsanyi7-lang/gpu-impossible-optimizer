@echo off
setlocal
title IOL - SUBNAUTICA 2 OPTIMIZER

echo ======================================================
echo    IOL (IMPOSSIBLE OPTIMIZATION LAYER) - ACTIVE
echo    Target: Subnautica 2 
echo    Device: Acer Nitro
echo ======================================================
echo.

:: 1. Rendszer optimalizalasa
echo [IOL] Kernel szintu prioritások beallitasa...
python iol_optimizer.py

:: 2. IOL Global Wrapper inditasa a jatekhoz
echo [IOL] Subnautica 2 inditasa IOL INFINITY modban...
echo.
echo ******************************************************
echo * IOL INFINITY AKTIV (VEGSO FAZIS):                *
echo * - Context Switching Suppression (CSS)             *
echo * - VRAM Overdraft (VO)                             *
echo * - Explorer.exe ideiglenes felfuggesztese          *
echo * CEL: STABIL 70-100 FPS ATLAG                      *
echo ******************************************************
echo.
echo FIGYELEM: Ne zard be ezt az ablakot jatek kozben!
echo A tálca és az asztal eltűnhet, de a játék után visszatér.
echo.

python iol_wrapper.py "C:\Program Files (x86)\Steam\steamapps\common\Subnautica2\Subnautica2.exe"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [HIBA] Az IOL Wrapper hibaval allt le! Hibakod: %ERRORLEVEL%
)

echo.
echo [IOL] Jatek befejezve.
pause
