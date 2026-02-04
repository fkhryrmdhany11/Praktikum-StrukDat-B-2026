kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

sama = kelas_A.intersection(kelas_B)
print(sama)
hanya_A = kelas_B.difference(kelas_A)
print(hanya_A)
kelas_A.update(kelas_B)
print(kelas_A)
    