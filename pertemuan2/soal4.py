mahasiswa = {
    "A001": {"nama": "Budi", 
             "prodi": "Informatika",
             "ipk": 3.45},

    "A002": {"nama": "Siti", 
             "prodi": "Sistem Informasi", 
             "ipk": 3.20},

    "A003": {"nama": "Andi", 
             "prodi": "Informatika",
             "ipk": 3.75}
}

for nim, data in mahasiswa.items():
    if data['ipk'] > 3.5:
        print(nim + ':', data)

# jumlah = 0
# banyak = 0
# for nim, data in mahasiswa.items():
#   print(x)