class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def get_volume(self):
        return self.panjang * self.lebar * self.tinggi

# Instansiasi objek balok
balok1 = Balok(15, 10, 8)
balok2 = Balok(20, 15, 6)
balok3 = Balok(35, 20, 5)

# Menampilkan volume masing-masing balok
print('Volume balok1:', balok1.get_volume())
print('Volume balok2:', balok2.get_volume())
print('Volume balok3:', balok3.get_volume())
