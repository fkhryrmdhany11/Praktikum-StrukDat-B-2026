data = {"name": "Fakhry", "age": 18} 
# Membuat dictionary dengan pasangan key:value
print(data) 
# Menampilkan dictionary

data = {"name": "Fakhry", "age": 18} 
# Membuat dictionary
print(data["name"]) 
# Mengambil value berdasarkan key "name"

data = {"name": "Fakhry", "age": 18} 
# Membuat dictionary
data["age"] = 19 
# Mengubah value pada key "age"
print(data) 
# Menampilkan hasil perubahan

data = {"name": "Fakhry"} 
# Membuat dictionary
data["age"] = 18 
# Menambahkan pasangan key:value baru
print(data) 
# Menampilkan dictionary

data = {"name": "Fakhry", "age": 18} 
# Membuat dictionary
data.pop("age") 
# Gunakan method pop() untuk menghapus key "age"
print(data) 
# Menampilkan hasil

data = {"name": "Fakhry", "age": 18} 
# Membuat dictionary
for key, value in data.items(): 
# Gunakan method items() untuk mengambil pasangan key dan value
    print(key, value) 
    # Menampilkan semua isi dictionary