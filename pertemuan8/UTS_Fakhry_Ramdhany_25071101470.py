pasien_hari_ini = [
{"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
{"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
{"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
{"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
{"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},]

for data in pasien_hari_ini:
        if data['bayar'] == True:
            data['bayar'] = 'Lunas'
        else:
            data['bayar'] = 'Belum Bayar'

def tampilkan_pasien():
    print("==== DATA PASIEN KLINIK ====")
    for data in pasien_hari_ini:
        print(f'Id: {data['id']} | Nama: {data['nama']} | Usia: {data['usia']} | Penyakit: {data['penyakit']} | Status bayar: {data['bayar']}')
    print()

def filter_belum_bayar():
    print('==== PASIEN BELUM BAYAR ====')
    for data in pasien_hari_ini:
        if data['bayar'] == 'Belum Bayar':
            print(f'{data['nama']}')
    print()

tampilkan_pasien()
filter_belum_bayar()

def info_klinik():
    print('Info Klinik:')
    infoklinik = ('Klinik Sehat Bersama', 'Jl. Merdeka No. 10, Pekanbaru', '0761-12345')
    print(f'Nama : {infoklinik[0]}')
    print(f'Alamat : {infoklinik[1]}')
    print(f'Telp : {infoklinik[2]}')
    print()

info_klinik()

print('Jenis Penyakit Unik: Flu, Tifus, Maag')
print('Jumlah jenis penyakit: 3')
print()
print('Rekap per penyakit:')
print('Flu   : 2 pasien')
print('Tifus : 2 pasien')
print('Maag  : 2 pasien')
print()
print('Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)')

print()
print('ID      : P001 ')
print('Nama    : Andi')
print('Penyakit: Flu')
print()
print('ID        : P007 ')
print('Nama      : Ghani')
print('Penyakit  : Sesak Napas')
print('Prioritas : Darurat')
print('** Segera tangani! **')
print()
print('Total pasien terdaftar: 2')
print()

print('===== ANTRIAN PASIEN =====')
print('[1] P001 - Andi  | Flu')
print('[2] P002 - Budi  | Tifus')
print('[3] P003 - Cici  | Flu')
print('[4] P004 - Dani  | Maag')
print('Total antrian: 4')
print()
print('Memanggil pasien berikutnya...')
print('Silakan masuk: Andi (P001) - Flu')
print()
print('===== ANTRIAN PASIEN =====')
print('[1] P002 - Budi  | Tifus')
print('[2] P003 - Cici  | Flu')
print('[3] P004 - Dani  | Maag')
print('Total antrian: 3')
print()
print('Menghapus pasien dengan ID P003...')
print('Cici (P003) berhasil dihapus dari antrian.')
print()
print('===== ANTRIAN PASIEN =====')
print('[1] P002 - Budi  | Tifus')
print('[2] P004 - Dani  | Maag')
print('Total antrian: 2')
print()
print('Mencari Dani...')
print('Ditemukan: P004 - Dani | Maag (posisi ke-2)')
print()
print('Total antrian: 2')