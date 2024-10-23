#Aditya Bintoro
class perpustakaan:
    def __init__(self,nama):
        self.nama=nama
        self.__buku = []
    def tambah_buku(self,buku):
        self.__buku.append(buku)
    def tampilkan_buku(self):
        for buku in self.__buku:
         print(buku.info())
    def __str__(self):
        return f"perpustakaan: {self.nama}"
    
class Buku:
    def __init__(self,judul,penulis):
        self.judul=judul
        self.penulis=penulis
    def info(self):
        return f"buku: {self.judul} oleh {self.penulis}"

class BukuFiksi(Buku):
    def __init__(self,judul,penulis,genre):
        super().__init__(judul,penulis)
        self.genre=genre
    def info(self):
        return f"buku fiksi: {self.judul} oleh {self.penulis}, genre: {self.genre}"
    
class BukuNonFiksi(Buku):
    def __init__(self,judul,penulis,topik):
        super().__init__(judul,penulis)
        self.topik=topik
    def info(self):
        return f"Buku Non-Fiksi: {self.judul} oleh {self.penulis}, Topik: {self.topik}"


Perpustakaan = perpustakaan("Perpustakaan Kota")

buku1 = BukuFiksi("Harry Potter","J.K. Rowling","Fantasi")
buku2 = BukuNonFiksi("Sapiens","Yuval Noah Harari","Sejarah")
Perpustakaan.tambah_buku(buku1)
Perpustakaan.tambah_buku(buku2)

print(Perpustakaan)
Perpustakaan.tampilkan_buku()



    


        

