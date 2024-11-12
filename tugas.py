# list untuk menyimpan data
data_mahasiswa = []

# Perulangan untuk memasukkan data
while True:
    # Meminta input dari pengguna
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan nim mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas (30%): "))
    uts = float(input("Masukkan nilai UTS (35%): "))
    uas = float(input("Masukkan nilai UAS (35%): "))
    
    # Menghitung nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    
    # Menyimpan data dalam list sebagai dictionary
    data_mahasiswa.append({
        'Nama': nama,
        'Nim' : nim,
        'Nilai Tugas': tugas,
        'Nilai UTS': uts,
        'Nilai UAS': uas,
        'Nilai Akhir': nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    tambah_data = input("Apakah ingin menambah data lagi? (y/t): ").lower()
    
    if tambah_data == 't':
        break

# Menampilkan data yang telah dimasukkan
print("\nDaftar Data Mahasiswa:")
print("No. | Nama | Nim | Tugas | UTS | UAS | Nilai Akhir")
for i, data in enumerate(data_mahasiswa, start=1):
    print(f"{i}. {data['Nama']}| {data['Nim']} | {data['Nilai Tugas']} | {data['Nilai UTS']} | {data['Nilai UAS']} | {data['Nilai Akhir']:.2f}")
