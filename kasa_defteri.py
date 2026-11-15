# Fonksiyon 1: Başlangıç kasasını ve işlemleri tutan ana sözlük yapısı
def kasa_yoneticisi():
    kasa_verileri = {"acilis_kasasi": 0.0, "islemler": []}
    
    # 1. Girdi: Açılış kasası (Hata korumalı)
    while True:
        try:
            acilis = float(input("Bugünkü açılış kasası tutarını girin (TL): "))
            if acilis < 0:
                print("❌ Açılış kasası negatif olamaz!")
                continue
            kasa_verileri["acilis_kasasi"] = acilis
            break
        except ValueError:
            print("❌ Hatalı giriş! Lütfen geçerli bir sayı yazın.")

    # Döngü (Menü)
    while True:
        print("\n--- KASA DEFTERİ MENÜSÜ ---")
        print("1. Yeni İşlem Ekle (Gelir/Gider)")
        print("2. Günlük Durumu Gör ve Raporla")
        print("3. Çıkış ve Dosyaya Kaydet")
        
        secim = input("Seçiminiz (1/2/3): ")
        
        if secim == "1":
            islem_ekle(kasa_verileri)
        elif secim == "2":
            bakiye_hesapla(kasa_verileri)
        elif secim == "3":
            rapor_yazdir(kasa_verileri)
            print("Program kapatıldı. Veriler kaydedildi.")
            break
        else:
            print("❌ Geçersiz seçim, lütfen 1, 2 veya 3 girin.")

# Fonksiyon 2: İşlem Ekleme (2. ve 3. Girdiler burada alınıyor)
def islem_ekle(veri_sozlugu):
    print("\n--- Yeni İşlem ---")
    
    # 2. Girdi: İşlem Türü
    tur = input("İşlem türü nedir? (gelir / gider): ").strip().lower()
    if tur not in ["gelir", "gider"]:
        print("❌ Hatalı giriş! Sadece 'gelir' veya 'gider' yazabilirsiniz.")
        return

    aciklama = input("İşlem açıklaması (Örn: Kahve satışı, Elektrik faturası): ")

    # 3. Girdi: Tutar (Hata korumalı)
    while True:
        try:
            tutar = float(input("Tutar (TL): "))
            if tutar < 0:
                print("❌ Tutar negatif olamaz!")
                continue
            break
        except ValueError:
            print("❌ Hatalı giriş! Lütfen sayısal bir değer girin.")

    # Listeye ekleme
    veri_sozlugu["islemler"].append({"tur": tur, "aciklama": aciklama, "tutar": tutar})
    print("✅ İşlem başarıyla eklendi.")

# Fonksiyon 3: Hesaplama ve Raporlama (Karar yapıları içerir)
def bakiye_hesapla(veri_sozlugu):
    toplam_gelir = 0
    toplam_gider = 0
    
    for islem in veri_sozlugu["islemler"]:
        if islem["tur"] == "gelir":
            toplam_gelir += islem["tutar"]
        elif islem["tur"] == "gider":
            toplam_gider += islem["tutar"]
            
    net_durum = toplam_gelir - toplam_gider
    kapanis_kasasi = veri_sozlugu["acilis_kasasi"] + net_durum
    
    print("\n--- GÜNCEL RAPOR ---")
    print(f"Açılış Kasası: {veri_sozlugu['acilis_kasasi']} TL")
    print(f"Toplam Gelir: {toplam_gelir} TL")
    print(f"Toplam Gider: {toplam_gider} TL")
    print(f"Kapanış Kasası: {kapanis_kasasi} TL")
    
    # Karar yapısı: Kâr/Zarar durumu
    if net_durum > 0:
        print("Durum: Kardasınız 🟢")
    elif net_durum < 0:
        print("Durum: Zarardasınız 🔴")
    else:
        print("Durum: Başa baş noktadasınız 🟡")
        
    return toplam_gelir, toplam_gider, kapanis_kasasi

# Fonksiyon 4: Sonuçları dosyaya kaydetme
def rapor_yazdir(veri_sozlugu):
    toplam_gelir, toplam_gider, kapanis_kasasi = bakiye_hesapla(veri_sozlugu)
    
    dosya_adi = "gunluk_kasa_raporu.txt"
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write("KUCUK ISLETME KASA RAPORU\n")
        dosya.write("-------------------------\n")
        dosya.write(f"Acilis Kasasi: {veri_sozlugu['acilis_kasasi']} TL\n")
        dosya.write(f"Toplam Gelir: {toplam_gelir} TL\n")
        dosya.write(f"Toplam Gider: {toplam_gider} TL\n")
        dosya.write(f"Kapanis Kasasi: {kapanis_kasasi} TL\n\n")
        dosya.write("Detayli Islemler:\n")
        for islem in veri_sozlugu["islemler"]:
            dosya.write(f"- {islem['tur'].upper()}: {islem['aciklama']} | Tutar: {islem['tutar']} TL\n")
            
    print(f"📁 Rapor başarıyla '{dosya_adi}' dosyasına kaydedildi!")

if __name__ == "__main__":
    kasa_yoneticisi()
