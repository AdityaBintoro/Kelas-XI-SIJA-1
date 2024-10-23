class mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def deskripsi(self):
        return f"{self.merk} {self.model} dibuat pada tahun {self.tahun}."
     
mobil1 = mobil("Toyota","Corolla",2020)
print(mobil1.deskripsi())