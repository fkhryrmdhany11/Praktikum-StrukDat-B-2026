def konversi(hasil, kodeAwal, kodeAkhir, data_kurs):
    if kodeAwal == kodeAkhir:
        return hasil

    if kodeAwal == "IDR":
        return hasil / data_kurs[kodeAkhir]

    if kodeAkhir == "IDR":
        return hasil * data_kurs[kodeAwal]

    kodeAkhirIdr = hasil * data_kurs[kodeAwal]
    return kodeAkhirIdr / data_kurs[kodeAkhir]