def buat_matriks_kosong(baris, kolom):
    return [[0 for _ in range(kolom)] for _ in range(baris)]
 
 
def ukuran_matriks(matriks):
    baris = len(matriks)
    kolom = len(matriks[0]) if baris > 0 else 0
    return baris, kolom
 
 
def tampilkan_matriks(matriks, nama="Matriks"):
    print(f"{nama} =")
    for row in matriks:
        print("  ", row)
    print()
 
 
def penjumlahan_matriks(A, B):
    baris_A, kolom_A = ukuran_matriks(A)
    baris_B, kolom_B = ukuran_matriks(B)
 
    if baris_A != baris_B or kolom_A != kolom_B:
        raise ValueError("Ukuran matriks A dan B harus sama untuk penjumlahan")
 
    hasil = buat_matriks_kosong(baris_A, kolom_A)
    for i in range(baris_A):
        for j in range(kolom_A):
            hasil[i][j] = A[i][j] + B[i][j]
    return hasil
 
 
def pengurangan_matriks(A, B):
    baris_A, kolom_A = ukuran_matriks(A)
    baris_B, kolom_B = ukuran_matriks(B)
 
    if baris_A != baris_B or kolom_A != kolom_B:
        raise ValueError("Ukuran matriks A dan B harus sama untuk pengurangan")
 
    hasil = buat_matriks_kosong(baris_A, kolom_A)
    for i in range(baris_A):
        for j in range(kolom_A):
            hasil[i][j] = A[i][j] - B[i][j]
    return hasil
 
 
def perkalian_matriks(A, B):
    baris_A, kolom_A = ukuran_matriks(A)
    baris_B, kolom_B = ukuran_matriks(B)
 
    if kolom_A != baris_B:
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B")
 
    hasil = buat_matriks_kosong(baris_A, kolom_B)
 
    for i in range(baris_A):
        for j in range(kolom_B):
            total = 0
            for k in range(kolom_A):
                total += A[i][k] * B[k][j]
            hasil[i][j] = total
 
    return hasil
 
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
 
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
 
    tampilkan_matriks(A, "Matriks A")
    tampilkan_matriks(B, "Matriks B")
 
    tampilkan_matriks(penjumlahan_matriks(A, B), "A + B")
    tampilkan_matriks(pengurangan_matriks(A, B), "A - B")
    tampilkan_matriks(perkalian_matriks(A, B), "A x B")
