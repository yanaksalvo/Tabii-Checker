# Tabii Hesap Kontrol Aracı
Bu Python scripti, `tabii.com` platformundaki hesapların geçerliliğini kontrol etmek için tasarlanmıştır. E-posta ve şifre kombinasyonlarını (combos) kullanarak giriş yapar, kullanıcı bilgilerini çeker ve hesapları abonelik durumlarına göre sınıflandırır (örneğin, Premium, Ücretsiz veya doğrulanmamış). Geçerli Premium hesaplar `.txt` dosyasına kaydedilir.

## Özellikler
- `tabii.com` API'sine karşı e-posta:şifre kombinasyonlarını kontrol eder.
- Hesap abonelik türlerini belirler (örneğin, Premium, Ücretsiz).
- Doğrulanmamış e-posta hesaplarını tespit eder.
- Geçerli Premium hesap kimlik bilgilerini `.txt` dosyasına kaydeder.
- Kolay okuma için renk kodlu konsol çıktısı:

    - Yeşil: Geçerli Premium hesaplar (HIT).
    - Sarı: Ücretsiz veya doğrulanmamış hesaplar (CUSTOM).
    - Kırmızı: Geçersiz kimlik bilgileri veya hatalar (BAD).

## Gereksinimler 
- Python 3.x
- Gerekli Python kütüphanesi: requests
- `.txt` formatında bir combo dosyası (e-posta:şifre kombinasyonları listesi).

---
# Kurulum

### 1. Projeyi Klonlayın

- `git clone https://github.com/yanaksalvo/Tabii-Checker.git`
-  `cd Tabii-Checker`

### 2. Modülleri Yükleyin
Bağımlılıkları(Modülleri) Yükleyin Gerekli Python kütüphanesini pip ile yükleyin:

- `pip install requests`

### 3. Combo Dosyanızı Hazırlayın
.txt formatında bir dosya (örneğin, combo.txt) oluşturun ve şu formatta e-posta ve şifre kombinasyonlarını ekleyin:

`email1:sifre1
email2:sifre2
email3:sifre3`



---

# Kullanım

### 1. Kodu Çalıştırın

- `python tabii_checker.py`

### 2. Combo Dosya Yolu Girin

### 3. Çıktıyı Kontrol Edin

- Script her bir komboyu işleyecek ve sonuçları terminalde gösterecektir:

    - **Yeşil**: Geçerli Premium hesap ( hits.txt dosyasına kaydedilir).
    - **Sarı**: Ücretsiz veya doğrulanmamış hesap.
   -  **Kırmızı**: Geçersiz kimlik bilgileri, engellenmiş istekler veya hatalar.
 
---

## Kod Açıklaması

    giris_yap_ve_token_al: Sağlanan e-posta ve şifre ile giriş yapmayı dener; başarılıysa bir erişim token'ı döndürür, engellenmişse "YASAKLI" döndürür.
    kullanici_bilgilerini_kontrol_et: Erişim token'ını kullanarak kullanıcı hesabı detaylarını (abonelik durumu, e-posta doğrulama gibi) çeker.
    combolari_isle: Combo dosyasını okur, her satırı işler ve renk kodlu sonuçları çıkarır.
    Renk Sınıfı (Renkler): Terminalde renkli çıktı için ANSI escape kodlarını tanımlar.

## Notlar

    Script, tabii.com API uç noktalarını (/auth/v2/login ve /auth/v2/me) kullanır. Bu uç noktaların hala geçerli olduğundan emin olun, çünkü API'ler zamanla değişebilir.
    Sık sık "YASAKLI" (engellenmiş) yanıtları alıyorsanız, IP banlarını önlemek için VPN veya proxy kullanmayı düşünebilirsiniz.
    Bu script yalnızca eğitim amaçlıdır. Kimlik bilgilerinin veya API'lerin izinsiz kullanımı, hizmet şartlarını veya yerel yasaları ihlal edebilir.

## Sorun Giderme

    FileNotFoundError: Combo dosya yolunun doğru olduğundan emin olun.
    ModuleNotFoundError: requests kütüphanesini yükleyin (pip install requests).
    Çıktı Yok: Combo dosyanızın formatını kontrol edin (e-posta:şifre).

## Katkıda Bulunma

Bu depoyu fork edebilir, sorun bildirebilir veya geliştirmelerle pull request gönderebilirsiniz!
## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için  dosyasına bakın.

# NOT : Açıklama Yapay Zeka İLE Yazılmıştır.
