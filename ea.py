import requests
import time
import random

# Membaca data dari file

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return []

# Fungsi untuk melakukan permintaan HTTP menggunakan proxy
def fetch_url(url, headers, referers, proxies):
    try:
        random_referer = random.choice(referers)
        headers["Referer"] = random_referer

        # Pilih proxy secara acak
        proxy = random.choice(proxies)
        proxy_dict = {
            "http": proxy,
            "https": proxy
        }

        response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
        response.raise_for_status()  # Memastikan status code 200

        print(f"Request ke {url} berhasil dengan Referer: {random_referer} dan Proxy: {proxy}")
        print(f"Status Code: {response.status_code}")
        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error saat mengakses {url}: {e}")
        return None

# Fungsi utama
if __name__ == "__main__":
    # Memuat data dari file
    urls = load_data("url.txt")
    referers = load_data("referers.txt")
    user_agents = load_data("user-agent.txt")
    proxies = load_data("proxy.txt")

    if not urls:
        print("Daftar URL kosong. Pastikan file url.txt tidak kosong.")
        exit()

    if not referers:
        print("Daftar Referer kosong. Pastikan file referers.txt tidak kosong.")
        exit()

    if not user_agents:
        print("Daftar User-Agent kosong. Pastikan file user-agent.txt tidak kosong.")
        exit()

    if not proxies:
        print("Daftar Proxy kosong. Pastikan file proxy.txt tidak kosong.")
        exit()

    # Menjalankan loop untuk setiap URL
    iteration = 1
    max_iterations = 100  # Batas jumlah iterasi

    while iteration <= max_iterations:
        print(f"Iterasi ke-{iteration}")

        # Pilih User-Agent secara acak untuk setiap iterasi
        chosen_user_agent = random.choice(user_agents)
        headers_template = {"User-Agent": chosen_user_agent}
        print(f"User-Agent yang digunakan: {headers_template['User-Agent']}")

        for url in urls:
            fetch_url(url, headers_template, referers, proxies)
            delay = random.uniform(5, 15)  # Waktu tunggu acak antara 5-15 detik
            print(f"Menunggu {delay:.2f} detik sebelum permintaan berikutnya...")
            time.sleep(delay)

        iteration += 1

    print("Selesai. Semua iterasi telah dijalankan.")
