matkul = {"alpro", "strukdat", "arsikom", "aljabar"} 
# Membuat set dengan tanda kurung kurawal {}
print(matkul) 
# Menampilkan isi set dengan urutan acak

matkul = {"alpro", "strukdat", "arsikom"} 
# Membuat set
matkul.add("aljabar") 
# Gunakan method add() menambahkan angka 4 ke dalam set
print(matkul) 
# Menampilkan set terbaru

matkul = {"alpro", "strukdat", "arsikom"} 
# Membuat set
matkul.remove("strukdat") 
# Gunakan method remove() untuk menghapus "strukdat"
print(matkul) 
# Menampilkan set setelah dihapus

matkul = {"alpro", "strukdat", "arsikom"} 
# Membuat set
for x in matkul: 
# Perulangan membaca tiap item set
    print(x) 
    # Menampilkan item satu per satu

matkul1 = {"alpro", "strukdat", "arsikom"} 
# Membuat set matkul1
matkul2 = {"arsikom", "aljabar", "pancasila"} 
# Membuat set matkul2
print(matkul1.union(matkul2)) 
# Gunakan method union() untuk menggabungkan dua set tanpa duplikat