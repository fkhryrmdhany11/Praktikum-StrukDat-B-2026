katalog = [ 
    {'nama': 'Belajar Python',  'harga': 75000, 'stok': 5}, 
    {'nama': 'Struktur Data',   'harga': 95000, 'stok': 3}, 
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}, ]

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for item in katalog:
        if nama_buku in item['nama']:
            if item['stok'] > jumlah_beli:
                harga = item['stok'] -  1
                print(f'Total Harga Yang harus dibayar = {harga}')
            else:
                print('Stok Tidak Cukup')
            break
        else:
            print('Buku Tidak Ditemukan')
            break

nama_buku = input('Masukkan Nama Buku: ')
jumlah_beli = int(input('Masukkan Jumlah Beli: '))
print(proses_transaksi(katalog, nama_buku, jumlah_beli))