class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_jurnal(self, judul, isi):
        jurnal = Jurnal(judul, isi, self)
        return jurnal
    
class Jurnal:
    def __init__(self, judul, isi, penulis):
        self.judul = judul
        self.isi = isi
        self.penulis = penulis

p1 = Peneliti("Abdul Kodir", "Pemrograman Python")


j1 = p1.tulis_jurnal("Logika Pemrograman Python", "logika yang digunakan untuk memprogram python")

print("peneliti : ", j1.penulis.nama)
print("jurnal : ", j1.judul)