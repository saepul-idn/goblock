import requests
import time
import random

# URL halaman web yang ingin diambil
url = "https://share-link-idn.blogspot.com/"

# Daftar mesin pencari populer untuk Referer
referers = [
    "https://google.com",
    "https://bing.com",
    "https://yahoo.com",
    "https://duckduckgo.com",
    "https://baidu.com",
    "https://yandex.com",
    "https://ask.com",
    "https://aol.com",
    "https://wolframalpha.com",
    "https://ecosia.org",
    "https://gigablast.com",
    "https://search.brave.com",
    "https://startpage.com",
    "https://seznam.cz"
]

# Header dengan User-Agent dan Referer (Referer akan diatur secara acak)
headers_template = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

# Fungsi untuk melakukan permintaan
def fetch_url():
    # Pilih Referer secara acak
    random_referer = random.choice(referers)
    headers = headers_template.copy()
    headers["Referer"] = random_referer
    
    # Mengirim permintaan GET
    response = requests.get(url, headers=headers)
    print(f"Request menggunakan Referer: {random_referer}")
    print(f"Status Code: {response.status_code}")
    #print(f"HTML Konten: {response.text[:500]}")  # Menampilkan 500 karakter pertama dari HTML

# Loop tanpa batas dengan Referer acak
iteration = 1
while True:
    print(f"Request ke-{iteration}")
    fetch_url()
    print("Menunggu 10 detik sebelum permintaan berikutnya...")
    time.sleep(10)  # Tunggu 10 detik sebelum mengulang
    iteration += 1
