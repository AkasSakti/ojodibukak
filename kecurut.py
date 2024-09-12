import math

# Fungsi untuk menghitung luas permukaan kerucut
def hitung_luas_permukaan_kerucut(jari_jari, tinggi):
    # Menghitung garis pelukis (s) menggunakan Teorema Pythagoras
    garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)
    
    # Menghitung luas permukaan kerucut
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    return luas_permukaan

# Meminta input dari pengguna
jari_jari = float(input("Masukkan jari-jari alas kerucut (dalam satuan meter): "))
tinggi = float(input("Masukkan tinggi kerucut (dalam satuan meter): "))

# Menghitung luas permukaan
luas = hitung_luas_permukaan_kerucut(jari_jari, tinggi)

# Menampilkan hasil
print(f"Luas permukaan kerucut adalah {luas:.2f} meter persegi")
