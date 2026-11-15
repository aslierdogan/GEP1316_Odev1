# Yapay Zekâ Çalışma Günlüğü (Promptlar)

1. **Prompt 1:** "İşletme öğrencisiyim, GEP1316 dersi ara değerlendirme ödevi için küçük işletme kasa defteri otomasyonu fikrini seçtim. En az 3 girdi, 2 karar yapısı ve 1 döngü içeren bir Python taslağı yazar mısın?"
   - **Karar ve Gerekçe:** Kabul edildi. Programın ana menüsü ve temel gelir-gider hesaplama iskeleti bu yanıtla oluşturuldu.

2. **Prompt 2:** "Kullanıcı tutar veya açılış kasası kısmına sayı yerine harf girdiğinde program hata verip kapanıyor. Bunu `try-except` bloklarıyla nasıl güvenli hale getirebiliriz?"
   - **Karar ve Gerekçe:** Kabul edildi. Ödevdeki 'hatalı girdi verilirse program çökmemeli' şartını sağlamak için veri doğrulama döngüleri eklendi.

3. **Prompt 3:** "Toplanan gelir ve giderleri gün sonunda bir `.txt` dosyasına biçimli bir şekilde yazdıran fonksiyonu ekleyebilir misin?"
   - **Karar ve Gerekçe:** Kabul edildi. `rapor_yazdir()` fonksiyonu ve `with open(...)` yapısı koda entegre edildi.

4. **Prompt 4 (YZ Hatasının Yakalanması):** "Yapay zekânın ilk verdiği kodda kullanıcı tutar veya açılış kasası kısmına eksi (-) değer girebiliyordu ve kasa hesabı bozuluyordu. Bunu nasıl engelleriz?"
   - **Karar ve Gerekçe:** Düzenlendi. YZ'nin atladığı bu uç durum fark edilerek `if tutar < 0:` kontrolü ile negatif sayı girişi engellendi.

5. **Prompt 5:** "GitHub deposu için programın ne yaptığını ve nasıl çalıştırıldığını açıklayan sade bir `README.md` metni hazırlar mısın?"
   - **Karar ve Gerekçe:** Kabul edildi. Depo dokümantasyonu tamamlandı.
