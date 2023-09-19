x = int(input("Masukkan nilai x (bilangan bulat sembarang): "))

if x != 0:
    hasil = 2 * (x ** 3) + 2 * x + 15 / x
else:
    print("Tidak dapat menghitung fungsi untuk x = 0")
    hasil = None

if hasil is not None:
    print(f"Hasil dari f({x}) = {hasil}")