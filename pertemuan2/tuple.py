mobil = ("lambor", "rolls royce", "ferrari") 
# Membuat tuple menggunakan tanda kurung biasa ()
print(mobil) 
# Menampilkan seluruh isi tuple

mobil = ("lambor", "rolls royce", "ferrari") 
# Membuat tuple
print(mobil[1]) 
# Mengambil data index ke-1 yaitu "rolls royce"

mobil = ("lambor", "rolls royce", "ferrari") 
# Membuat tuple
print(len(mobil)) 
# Menggunakan fungsi len() menghitung jumlah item dalam tuple

mobil = ("lambor", "rolls royce", "ferrari") 
# Membuat tuple
temp = list(mobil) 
# Tuple diubah menjadi list agar bisa dimodifikasi
temp[0] = "audi" 
# Mengubah item pertama menjadi "audi"
mobil = tuple(temp) 
# Mengubah kembali list menjadi tuple
print(mobil) 
# Menampilkan tuple hasil perubahan