class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
    
class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []
    
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

m1 = Mahasiswa("Awaliyah Hayatun", "(J3D118086)")
k1 = KelompokKKM("Kelompok 1")
m1.gabung_kelompok(k1)

m2 = Mahasiswa("Salma Nur Adila", "(J3D118084)")
k2 = KelompokKKM("Kelompok 2")
m2.gabung_kelompok(k2)

print(k1.nama)
for anggota in k1.anggota:
    print(anggota.nama, anggota.nim)

print("")

print(k2.nama)
for anggota in k2.anggota:
    print(anggota.nama, anggota.nim)