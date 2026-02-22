class Buku:
    def __init__(self, buku, penulis, tahun):
        self.buku = buku
        self.penulis = penulis
        self.tahun = tahun
    
    def tampilkan_buku(self):
        print(f'buku {self.buku} | penulis {self.penulis} | tahun {self.tahun}')

    def ubah_tahun(self, tahunbaru):
        self.tahun = tahunbaru

buku1 = Buku('bulan', 'tere liye', 2016)
buku2 = Buku('aljabar', 'rinaldi munir', 2017)
buku3 = Buku('perahu layar', 'mashasi', 2000)

buku1.tampilkan_buku()
buku3.ubah_tahun(2019)
print(f'{buku3.tahun}')