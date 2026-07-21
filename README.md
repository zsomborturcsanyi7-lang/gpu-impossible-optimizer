# IOL (Impossible Optimization Layer) — Kísérleti GPU optimalizációs PoC

**Status:** ⚠️ Prototype — PoC validálva RTX 3050 Ti-n (3x gyorsulás), kernel driver kellene production-höz

Kísérleti GPU optimalizációs réteg: CUDA kernal bypass, VRAM virtualizáció, neurális renderelés. **Csak koncepció — nem production kész.**

## ⚠️ THIS PROJECT IS UNFINISHED — FEEL FREE TO CONTINUE IT ⚠️

**Ez a projekt NINCS KÉSZEN. Bárki folytathatja, aki akarja!**
Ezt a projektet Zsombi & Hermes Agent (Nous Research) közösen fejlesztette, de egyik projekt sincs 100%-osan befejezve.

---

## Ami a repóban van

| Fájl | Leírás |
|------|--------|
| `iol_cuda_core.cu` | CUDA kernel (kernel bypass kísérlet) |
| `iol_kernel.h` | Kernel header |
| `iol_hardware_poc.py` | Hardware PoC |
| `iol_optimizer.py` | Optimalizáló logika |
| `iol_global_service.py` | Globális service |
| `iol_wrapper.py` | Wrapper réteg |
| `vram_virtualization.cpp` | VRAM virtualizációs kísérlet |
| `poc_simulation.py` | PoC szimuláció |
| `advanced_stress_test.py` | Stressz teszt |
| `.bat` fájlok | Windows batch szkriptek (játék profilok, benchmark) |

## Játék profilok (kísérleti)
CS2, CS3, Subnautica 2, Valorant — `.bat` fájlok a konfigurált futtatáshoz.

## Fejlesztő
Zsombi & Hermes Agent (Nous Research)
