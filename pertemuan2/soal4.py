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

for  data in mahasiswa.values():
    if data['ipk'] > 3.5:
        print(f'mahasiswa dengan ipk di atas 3.5 : {data['nama']}')

rata = sum(data['ipk'] for data in mahasiswa.values()) / len(mahasiswa)

print(f'rata rata ipk {rata: .2f}')

mahasiswa['A004'] = {'nama' : 'wowo', 'prodi' : 'persawitan', 'ipk' : 3.00}
print(mahasiswa)