class adit:
    def __init__(self,nama,impian):
        self.nama=nama
        self.impian=impian
    
    def cita_cita(self):
        return f"{self.nama} ingin menjadi {self.impian}"
adit1= adit("adit","sigma")
print(adit1.cita_cita())