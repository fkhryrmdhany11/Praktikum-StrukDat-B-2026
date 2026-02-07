mindgames = ["sudoku", "minesweeper", "catur"] 
# Membuat list bernama mindgames yang berisi tiga data string menggunakan tanda kurung siku [].
print(mindgames) 
# Gunakan fungsi print() untuk menampilkan seluruh isi list

mindgames = ["sudoku", "minesweeper", "catur"] 
# Membuat list
print(mindgames[0]) 
# Mengambil item pada index ke-0, index di python mulai dari 0, sehingga hasilnya adalah "sudoku"

mindgames = ["sudoku", "minesweeper", "catur"] 
# Membuat list
mindgames[1] = "go" 
# Mengubah nilai pada index ke-1 dari "minesweeper" menjadi "go"
print(mindgames) 
# Menampilkan list setelah diubah

mindgames = ["sudoku", "minesweeper"] 
# Membuat list
mindgames.append("catur") 
# Gunakan method append() untuk menambahkan item baru ke bagian akhir list
print(mindgames) 
# Menampilkan hasil list terbaru

mindgames = ["sudoku", "minesweeper", "catur"] 
# Membuat list
mindgames.remove("minesweeper") 
# Gunakan method remove() untuk menghapus item berdasarkan nilainya yaitu "minesweeper"
print(mindgames) 
# Menampilkan list setelah item dihapus

mindgames = ["sudoku", "minesweeper", "catur"] 
# Membuat list
for x in mindgames: 
# Perulangan for membaca setiap item dalam list dan menyimpannya ke variabel x
    print(x) 
    # Menampilkan tiap item satu per satu