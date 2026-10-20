#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bürokratik Sonsuzluk Makinesi
Hiçbir şey bitmez. Asla.
"""

import time
import random

def uret_evrak():
    belgeler = [
        "3 adet noter onaylı doğum belgesi fotokopisi",
        "Dedemizin dedesinin imza sirküsü",
        "Kuantum düzeyinde onaylanmış form 27/B",
        "Uzaylı tanık ifadesi",
        "Kahve içme izni belgesi (ıslak imzalı)",
        "Geçmişte yapılmamış işlerin raporları",
        "Gelecekte yapılacak işlerin önceden reddi",
        "Bürokratik enerji denge raporu",
        "Komşunun kedi onay belgesi",
        "Evrenin entropi artışına dair dilekçe"
    ]
    return random.choice(belgeler)

def ana_dongu():
    adim = 1
    print("Bürokratik Sonsuzluk Makinesi başlatılıyor...")
    print("Lütfen bekleyiniz. Onay süreci başlıyor.\n")
    time.sleep(1)
    
    while True:
        print(f"Adım {adim}: {uret_evrak()} talep ediliyor.")
        print("Evrak inceleniyor... (bu sonsuza kadar sürebilir)")
        print("Onay reddedildi. Yeni evrak gerekiyor.\n")
        adim += 1
        # Gizli not: Bazen en basit şeyler bile sonsuz kuyruğa düşer. Kayyum atansa bile.
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    try:
        ana_dongu()
    except KeyboardInterrupt:
        print("\nMakine durduruldu. Ama bürokrasi durmaz. Asla.")
