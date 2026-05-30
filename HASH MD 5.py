import hashlib

# Fungsi untuk membuat hash MD5
def buat_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

# Input data awal user
print("=== INPUT DATA AWAL USER ===")
nama = input("Nama   : ")
email = input("Email  : ")
hp = input("No HP  : ")

# Gabungkan data profil
data_awal = f"{nama}|{email}|{hp}"

# Buat hash MD5 awal
hash_awal = buat_md5(data_awal)

print("\nHash MD5 Awal:")
print(hash_awal)

# Input data baru
print("\n=== INPUT DATA BARU USER ===")
nama_baru = input("Nama   : ")
email_baru = input("Email  : ")
hp_baru = input("No HP  : ")

# Gabungkan data baru
data_baru = f"{nama_baru}|{email_baru}|{hp_baru}"

# Buat hash MD5 baru
hash_baru = buat_md5(data_baru)

# Tampilkan hasil perbandingan
print("\n=== HASIL PERBANDINGAN ===")
print("Hash Lama :", hash_awal)
print("Hash Baru :", hash_baru)

# Cek apakah data berubah
if hash_awal == hash_baru:
    print("\nStatus: Data TIDAK berubah.")
else:
    print("\nStatus: Data TELAH berubah atau dimodifikasi.")