# Küçük İşletme Kasa Defteri ve Günlük Rapor Uygulaması

Bu Python komut satırı uygulaması, küçük işletmelerin (kafe, dükkan vb.) günlük açılış kasasını, gelir ve gider işlemlerini takip etmesini, net kâr/zarar durumunu hesaplamasını ve gün sonu raporunu otomatik olarak `.txt` dosyasına kaydetmesini sağlar.

## Özellikler
- Hatalı veya negatif sayı girişlerinde programın çökmesini engelleyen veri doğrulama (`try-except`).
- Sürekli işlem eklemeye imkân tanıyan menü döngüsü (`while`).
- Gelir ve giderleri sözlük ve liste yapısında saklama.
- Gün sonu raporunu hem ekrana biçimli yazdırma hem de `gunluk_kasa_raporu.txt` dosyasına kaydetme.

## Nasıl Çalıştırılır?
1. Python 3 yüklü bir ortamda veya çevrimiçi bir Python derleyicisinde (örn. Programiz, Google Colab) `kasa_defteri.py` dosyasını açın.
2. Kodu çalıştırın ve ekrandaki menü adımlarını takip edin.
