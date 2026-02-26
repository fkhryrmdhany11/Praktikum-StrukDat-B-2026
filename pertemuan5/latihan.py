# 1. Diberikan list nilai mahasiswa: 
nilai_tugas = [70, 85, 90, 65, 80] 

# a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks. 
posisi = nilai_tugas.index(65)
nilai_tugas.pop(posisi)
nilai_tugas.insert(posisi, 75)
print(nilai_tugas)

# b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke terkecil. 
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

# c. Tampilkan jumlah total seluruh nilai dalam list tersebut. 
print(f'Jumlah total : {sum(nilai_tugas)}')

# d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak tampilkan "Tidak ada”. 
print('ada nilai sempurna') if nilai_tugas == 100 else print('tidak ada')

print('')

# 2. Diberikan sebuah list yang berisi beberapa tuple. Setiap tuple berisi (Nama, Nilai): 
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)] 

# a. Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75, 
# tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf [Nama], Anda harus remidi."
for nama, nilai in kumpulan_nilai:
    print(f'Selamat {nama}, Anda Lulus!') if nilai >= 75 else print(f'Maaf {nama}, Anda harus remidi.')

print('')

# 3. Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:  
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

# a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang) 
sendiri = sesi_pagi.intersection(sesi_siang)
print(sendiri)

# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua sesi tanpa duplikat). 
unik = sesi_pagi.union(sesi_siang)
print(unik)

# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)

print('')

# 4. Diberikan data buku dalam bentuk dictionary: 
transaksi = [{"produk": "Buku", "harga": 10000, "jumlah": 3}, 
             {"produk": "Pena", "harga": 5000, "jumlah": 10}, 
             {"produk": "Penghapus", "harga": 2000, "jumlah": 2}] 

# a. Ubah jumlah buku menjadi 8. 
for i in transaksi:
    if i['produk'] == 'Buku':
        i.update({'jumlah': 8})
    print(i)

# b. Tambahkan 2 produk baru. 
transaksi.append({'produk': 'Paku', 'harga': 2000, 'jumlah': 2})
transaksi.append({'produk': 'Palu', 'harga': 20000, 'jumlah': 1})

# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan. 
# Tampilkan ringkasan seperti ini: 
# Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
for i in range(len(transaksi)):
    total = transaksi[i]['harga'] * transaksi[i]['jumlah']
    print(f'produk : {transaksi[i]['produk']} | total : {total}')