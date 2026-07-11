@echo off
setlocal
echo [IOL-ULTRA-FIX] Wave Bank hiba es GPU utkozes elharitasa...

:: 1. Audio szolgaltatasok leallitasa (brute force)
echo [IOL] Audio szolgaltatasok felfuggesztese...
powershell -Command "Stop-Service -Name Audiosrv -Force"
powershell -Command "Stop-Service -Name DtsApo4Service -Force"

:: 2. IOL Optimalizalo futtatasa (csak a beallitasok, hatterfolyamat nelkul)
echo [IOL] Rendszer optimalizalasa...
python iol_optimizer.py

:: 3. UserBenchmark inditasa közvetlenül (Wrapper hatter-GPU szal nelkul)
echo [IOL] UserBenchmark inditasa...
echo FIGYELEM: Ha az urhajos jatek megjelenik, jatszd le!
start "" "C:\Users\iga\AppData\Roaming\UserBenchmark\UserBenchmark.exe"

echo.
echo VARD MEG, AMIG A BENCHMARK TELJESEN BEFEJEZODIK!
echo Ha megnyilt a bongeszoben az eredmeny, nyomj meg egy gombot az audio visszakapcsolasahoz.
pause

echo [IOL] Audio szolgaltatasok ujrainditasa...
powershell -Command "Start-Service -Name Audiosrv"
powershell -Command "Start-Service -Name DtsApo4Service"
echo Kesz.
pause
