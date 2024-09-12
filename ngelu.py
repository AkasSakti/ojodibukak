import numpy as np

# Fungsi untuk meminta input dari pengguna
def input_matrix(rows, cols):
    matrix = []
    print(f"Masukkan elemen-elemen matriks ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Masukkan elemen [{i+1},{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

# Meminta ukuran matriks dari pengguna
rows = int(input("Masukkan jumlah baris matriks: "))
cols = int(input("Masukkan jumlah kolom matriks: "))

# Input matriks 2D dari pengguna
matrix1 = input_matrix(rows, cols)
matrix2 = input_matrix(rows, cols)

# Penjumlahan skalar (skalar 12)
scalar_addition = matrix1 + 12
print("\nPenjumlahan skalar 12 dengan matriks pertama:")
print(scalar_addition)

# Penjumlahan antar matriks
matrix_addition = matrix1 + matrix2
print("\nPenjumlahan antara matriks 1 dan matriks 2:")
print(matrix_addition)

# Perkalian antar matriks
matrix_multiplication = np.matmul(matrix1, matrix2)
print("\nPerkalian antara matriks 1 dan matriks 2:")
print(matrix_multiplication)

# Dot product (hasil kali titik) antar matriks
dot_product = np.dot(matrix1, matrix2)
print("\nDot product antara matriks 1 dan matriks 2:")
print(dot_product)

# Mean dari matriks pertama
mean_matrix1 = np.mean(matrix1)
print("\nMean (rata-rata) dari matriks 1:")
print(mean_matrix1)

# Median dari matriks pertama
median_matrix1 = np.median(matrix1)
print("\nMedian dari matriks 1:")
print(median_matrix1)

# Standar deviasi dari matriks pertama
std_matrix1 = np.std(matrix1)
print("\nStandar deviasi dari matriks 1:")
print(std_matrix1)

# Variansi dari matriks pertama
var_matrix1 = np.var(matrix1)
print("\nVariansi dari matriks 1:")
print(var_matrix1)
