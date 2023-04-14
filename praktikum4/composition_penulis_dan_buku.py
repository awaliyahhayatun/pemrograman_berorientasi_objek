class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def tulis_buku(self, judul, halaman):
        buku = Buku(judul, halaman, self)
        return buku
    
class Buku:
    def __init__(self, judul, halaman, penulis):
        self.judul = judul
        self.halaman = halaman
        self.penulis = penulis

p1 = Penulis("Budi Raharjo")
b1 = p1.tulis_buku("Kumpulan Solusi Pemrograman", 80)


print("Nama Penulis : ", b1.penulis.nama)
print("Judul Buku : ", b1.judul)