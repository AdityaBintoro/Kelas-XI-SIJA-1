class makanan:
    def __init__(self,jenis):
        self.jenis=jenis

    def info(self):
        return f"jenis nya {self.jenis}."
    
class minuman(makanan):
    def __init__(self,jenis,nama):
        super().__init__(jenis)
        self.nama=nama
    
    def info_minuman(self):
        return f"jenis {self.jenis}nya,{self.nama}."
makanan1=minuman("minuman","jus")
print(makanan1.info())
print(makanan1.info_minuman())
        
        