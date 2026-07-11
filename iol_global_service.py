import os
import sys
import time
import psutil
import subprocess
import torch
import wmi

class IOL_GlobalService:
    """
    IOL Omnipotence v3.5 (THERMOGUARD)
    Biztonságos teljesitmény-maximalizálás aktiv hövédelemmel.
    """
    
    def __init__(self):
        self.game_list = ["cs2.exe", "cs3.exe", "Subnautica2.exe", "Valorant.exe"]
        self.blacklist = ["msedge.exe", "chrome.exe", "explorer.exe"]
        self.optimized_pids = set()
        self.is_running = True
        self.w = wmi.WMI(namespace="root\\wmi")
        
        # Biztonsági határértékek
        self.TEMP_LIMIT_WARNING = 82.0  # 82 foknál visszavesszük a boostot
        self.TEMP_LIMIT_CRITICAL = 92.0 # 92 foknál teljesen leállitjuk az IOL-t
        self.is_throttled_by_iol = False

    def get_gpu_temp(self):
        """Lekéri az NVIDIA GPU hőmérsékletét."""
        try:
            output = subprocess.check_output("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits", shell=True)
            return float(output.decode().strip())
        except: return 0.0

    def get_cpu_temp(self):
        """Lekéri a CPU hőmérsékletét (WMI-n keresztül)."""
        try:
            # Ez a legtöbb laptopon (Acer Nitro is) működik
            temps = self.w.MSAcpi_ThermalZoneTemperature()
            if temps:
                # Az érték tizedkelvinben van: (X - 2732) / 10 = Celsius
                return (temps[0].CurrentTemperature - 2732) / 10.0
        except: 
            return 0.0

    def _apply_iol_boost(self, proc, level="MAX"):
        """Dinamikusan alkalmazza a boostot a hőmérséklet függvényében."""
        try:
            if level == "MAX":
                proc.nice(psutil.HIGH_PRIORITY_CLASS)
                # Max frekvencia rögzités
                subprocess.run("nvidia-smi -lgc 1800,2100", shell=True, capture_output=True)
            elif level == "SAFE":
                proc.nice(psutil.NORMAL_PRIORITY_CLASS)
                # Frekvencia rögzités feloldása (visszaengedjük a gyári throttlingot)
                subprocess.run("nvidia-smi -rgc", shell=True, capture_output=True)
        except: pass

    def run(self):
        print("======================================================")
        print("   IOL OMNIPOTENCE v3.5 (THERMOGUARD ACTIVE)")
        print("   Status: Biztonságos mód | Limit: 82°C / 92°C")
        print("======================================================")

        try:
            while self.is_running:
                cpu_t = self.get_cpu_temp()
                gpu_t = self.get_gpu_temp()
                max_t = max(cpu_t, gpu_t)

                # 1. Hőmérséklet alapú döntéshozatal
                if max_t >= self.TEMP_LIMIT_CRITICAL:
                    if not self.is_throttled_by_iol:
                        print(f"\n[!!! RIASZTÁS !!!] KRITIKUS HŐMÉRSÉKLET: {max_t}°C!")
                        print("[IOL] Vészhelyzeti leállitás: Optimalizáció felfüggesztve.")
                        self.is_throttled_by_iol = True
                    boost_mode = "SAFE"
                elif max_t >= self.TEMP_LIMIT_WARNING:
                    if not self.is_throttled_by_iol:
                        print(f"\n[FIGYELEM] Magas hőmérséklet: {max_t}°C. Váltás Biztonsági Boostra...")
                        self.is_throttled_by_iol = True
                    boost_mode = "SAFE"
                else:
                    if self.is_throttled_by_iol:
                        print(f"\n[IOL] Hőmérséklet stabilizálódott ({max_t}°C). Újrainditás...")
                        self.is_throttled_by_iol = False
                    boost_mode = "MAX"

                # 2. Folyamatok kezelése
                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        name = proc.name().lower()
                        if any(game.lower() in name for game in self.game_list):
                            self._apply_iol_boost(proc, boost_mode)
                    except: continue

                time.sleep(2.0) # Gyors mintavételezés a biztonságért
        except KeyboardInterrupt:
            # Visszaállitunk mindent gyárira kilépéskor
            subprocess.run("nvidia-smi -rgc", shell=True, capture_output=True)
            print("\n[IOL] Kilépés... Hardver korlátok visszaállitva.")

if __name__ == "__main__":
    service = IOL_GlobalService()
    service.run()
