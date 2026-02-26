from kurs import kurs
from konverter import konversi
from tabulate import tabulate

def tampilkan_kurs():
    tabel = []
    for kode, nilai in kurs.items():
        tabel.append([kode, f"{nilai:,}".replace(",", ".")])
    
    print("=== KONVERTER MATA UANG ===")
    print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    kodeAwal = input("Dari (IDR/USD/EUR/SGD/JPY): ")
    kodeAkhir = input("Ke (IDR/USD/EUR/SGD/JPY): ")
    Jumlah = float(input("Jumlah: "))

    hasil = konversi(Jumlah, kodeAwal, kodeAkhir, kurs)

    print(f"\nRp {Jumlah:,.0f} = {hasil:,.2f} {kodeAkhir}".replace(",", "."))

if __name__ == "__main__":
    main()