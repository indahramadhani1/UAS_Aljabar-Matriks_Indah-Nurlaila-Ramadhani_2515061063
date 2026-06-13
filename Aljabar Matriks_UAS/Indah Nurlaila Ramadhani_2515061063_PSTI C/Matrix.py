import Indah063 as m
 
 
def main():
    A = [
        [2, 1, 1],
        [1, 3, 2],
        [1, 0, 0]
    ]
 
    B = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
 
    m.tampilkan_matriks(A, "Matriks A")
    m.tampilkan_matriks(B, "Matriks B")
 
    print(">> Penjumlahan A + B")
    m.tampilkan_matriks(m.penjumlahan_matriks(A, B))
 
    print(">> Pengurangan A - B")
    m.tampilkan_matriks(m.pengurangan_matriks(A, B))
 
    print(">> Perkalian A x B")
    m.tampilkan_matriks(m.perkalian_matriks(A, B))
 
 
if __name__ == "__main__":
    main()