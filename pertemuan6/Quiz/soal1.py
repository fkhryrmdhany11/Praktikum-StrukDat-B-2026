Dict = {}
List = []

def tambah_buku(nama, harga, stok):
    Dict.update({'nama' : nama, 'harga' : harga, 'stok' : stok})

    if harga > 0:
        return Dict
    else:
        print("Error")
        return None

for i in range(3):
    nama = input('Masukkan Judul Buku: ')
    harga = float(input('Masukkan Harga Buku: '))
    stok = int(input('Masukkan Stok Buku: '))
    tambah_buku(nama, harga, stok)
    List.append(Dict)
    print('')

print(List)