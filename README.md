# Ninja Heroes NewEra Account Checker

Tool untuk melakukan pengecekan massal akun Ninja Heroes NewEra secara otomatis.

## Fitur

- ✅ Pengecekan massal dari file list (email:password)
- ✅ Deteksi server yang tersedia untuk setiap akun

## Instalasi

### 1. Clone repository (atau download script)

```bash
git clone https://github.com/DarkSkull777/ninja-checker.git
cd ninja-checker
```

Atau download langsung file checker.py

2. Install dependencies

```bash
pip install -r requirements.txt
```

🚀 Cara Penggunaan

Format Dasar

```bash
python nhcheck.py -l <file_list> [OPTIONS]
```

Persiapan File List

Buat file teks berisi daftar akun dengan format email:password (satu akun per baris):

contoh: accounts.txt

```
user1@gmail.com:password123
user2@yahoo.com:rahasia789
user3@example.com:qwerty123
```

Opsi Command Line

Opsi Deskripsi Wajib
-l, --list File list akun (email:password) ✅ Ya
-o, --output File untuk menyimpan hasil FOUND ❌ Tidak
--only Hanya tampilkan akun yang FOUND (sembunyikan NOT AVAILABLE & ERROR) ❌ Tidak

Contoh Penggunaan

1. Pengecekan normal (tampilkan semua hasil)

```bash
python nhcheck.py -l accounts.txt
```

Output:

```
[FOUND] -> user1@gmail.com:password123 | server 1 , 3 , 5
[NOT AVAILABLE] user2@yahoo.com:rahasia789
[ERROR] user3@example.com:qwerty123 -> timeout
```

2. Hanya tampilkan akun yang FOUND

```bash
python checker.py -l accounts.txt --only
```

Output:

```
[FOUND] -> user1@gmail.com:password123 | server 1 , 3 , 5
[FOUND] -> user4@test.com:pass456 | server 2
```

3. Simpan hasil FOUND ke file

```bash
python checker.py -l accounts.txt -o hasil.txt
```

4. Kombinasi --only dengan save hasil

```bash
python checker.py -l accounts.txt -o hasil.txt --only
```

File hasil.txt akan berisi:

```
user1@gmail.com:password123 | server 1 , 3 , 5
user4@test.com:pass456 | server 2
```

📊 Penjelasan Output

Warna Status Arti
🟢 Hijau [FOUND] Akun valid dengan server terdeteksi
🔴 Merah [NOT AVAILABLE] Akun tidak valid atau password salah
🟡 Kuning [ERROR] Terjadi error koneksi/timeout
