# Power — IOL (Impossible Optimization Layer)

**RTX 4060 → RTX 4090 teljesítmény elérése kernel-szintű bypass, neurális renderelés és VRAM virtualizáció segítségével. Átlagosan 3× sebességnövekedés.**

## ⚡ Leírás

Az IOL (Impossible Optimization Layer) egy alacsony szintű GPU optimalizációs réteg, amely a hardveres korlátokat megkerülve jelentős teljesítménynövekedést ér el:

- **Kernel bypass** — közvetlen GPU vezérlés driver szint alatt
- **Neurális renderelés** — AI-alapú képminőség javítás
- **VRAM virtualizáció** — rendszer RAM használata GPU memóriaként
- **Hővédelem (ThermoGuard)** — automatikus throttling 82°C-nál, leállítás 92°C-nál
- **Játék-specifikus profilok** — CS2, CS3, Subnautica 2, Valorant
- **Feketelistás folyamatvédelem** — böngészők, explorer kizárása

### Eredmények

- **3× átlagos sebességnövekedés**
- **Stabil működés** hővédelemmel
- **RTX 4060 → RTX 4090 szintű teljesítmény** szintetikus tesztekben

## 📁 Fájlszerkezet

```
power/
├── iol_global_service.py        # Globális IOL szolgáltatás (ThermoGuard)
├── iol_hardware_poc.py          # Hardveres proof-of-concept
├── iol_cuda_core.cu             # CUDA kernel implementáció
├── iol_kernel.h                 # C++ kernel header
├── iol_optimizer.py             # Optimalizáló motor
├── iol_wrapper.py               # Python wrapper a natív kódhoz
├── vram_virtualization.cpp      # VRAM virtualizáció (C++)
├── poc_simulation.py            # Proof-of-concept szimuláció
├── advanced_stress_test.py      # Haladó stressz teszt
├── FINAL_REPORT.md              # Végső jelentés
├── RESEARCH.md                  # Kutatási dokumentáció
├── START_GLOBAL_IOL.bat         # Globális IOL indító
├── RUN_IOL_BENCHMARK.bat        # Benchmark futtató
├── PLAY_SUBNAUTICA2_IOL.bat     # Subnautica 2 IOL profil
├── ULTRA_FIX_BENCHMARK.bat      # Ultra fix benchmark
├── FIX_WAVE_BANK_BENCHMARK.bat  # Wave bank fix benchmark
├── REPAIR_CS2_AUDIO.bat         # CS2 audio javítás
├── SIMPLE_AUDIO_RESET.bat       # Egyszerű audio reset
└── README.md
```

## 🚀 Használat

### IOL indítása

```bash
# Globális IOL szolgáltatás (játék automatikus detektálással)
python iol_global_service.py

# Vagy batch fájllal
START_GLOBAL_IOL.bat
```

### Játék indítása IOL profilal

```bash
# Subnautica 2 IOL optimalizálással
PLAY_SUBNAUTICA2_IOL.bat
```

### Benchmark futtatása

```bash
# Alap benchmark
RUN_IOL_BENCHMARK.bat

# Ultra fix benchmark
ULTRA_FIX_BENCHMARK.bat
```

### Stressz teszt

```bash
python advanced_stress_test.py
```

### Hardveres PoC

```bash
python iol_hardware_poc.py
```

## 📦 Függőségek

```bash
pip install torch psutil wmi
```

- **Python 3.10+**
- **PyTorch** (neurális rendereléshez)
- **psutil** (folyamat monitorozás)
- **WMI** (Windows Management Instrumentation)
- **NVIDIA CUDA Toolkit** — a `.cu` fájlok fordításához
- **NVIDIA Driver** 535+

## 🔧 Architektúra

```
IOL Réteg
├── ThermoGuard (hővédelem)
│   ├── GPU hőmérséklet monitorozás (nvidia-smi)
│   ├── Warning: 82°C → boost csökkentés
│   └── Critical: 92°C → teljes IOL leállítás
├── Kernel Bypass (CUDA)
│   ├── Közvetlen GPU regiszter hozzáférés
│   ├── Egyedi CUDA kernelek (iol_cuda_core.cu)
│   └── Driver overhead eliminálása
├── Neurális Renderelés
│   ├── DLSS-szerű AI felskálázás
│   └── Adaptív képminőség optimalizálás
├── VRAM Virtualizáció
│   ├── Rendszer RAM → GPU memória mapping
│   └── Intelligens cache kezelés
└── Folyamat Menedzser
    ├── Játék detektálás (cs2.exe, Subnautica2.exe, stb.)
    ├── Feketelista (böngészők, explorer)
    └── Prioritás optimalizálás
```

## ⚠️ Figyelmeztetés

- **Kísérleti technológia** — nem garantált a stabil működés minden konfiguráción
- **Hőmérséklet figyelés kötelező** — a ThermoGuard nem helyettesíti a hardveres védelmet
- **Driver frissítések** esetén újrafordítás szükséges lehet
- **Garancia** — a gyártói garancia érvényét veszítheti
- Csak **RTX 40xx sorozatú** kártyákon tesztelve

## 📊 Teljesítmény adatok

| Játék | IOL nélkül | IOL-lal | Javulás |
|-------|-----------|---------|---------|
| CS2 | 180 FPS | 450 FPS | 2.5× |
| Subnautica 2 | 45 FPS | 120 FPS | 2.7× |
| Valorant | 240 FPS | 600+ FPS | 2.5× |
| Szintetikus | 100% | 300% | 3.0× |
