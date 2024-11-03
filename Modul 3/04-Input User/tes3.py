# Mengimpor konstanta pi dari modul math
import math

# Meminta input dari pengguna untuk jari-jari lingkaran
radius = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas lingkaran
luas = math.pi * (radius ** 2)

# Menampilkan hasil luas lingkaran
print(f"Luas lingkaran dengan jari-jari {radius} adalah {luas:.2f} satuan luas.")
