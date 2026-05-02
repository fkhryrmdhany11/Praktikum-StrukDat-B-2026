katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, ]

def cari_buku(katalog, keyword):
    for item in katalog:
        if keyword in item['nama']:
            return f'{item}'
        else:
            print('Buku Tidak Ditemukan')
            break


keyword = input('Masukkan Keyword: ')
print(cari_buku(katalog, keyword))