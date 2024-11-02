# Modul untuk mengelola data mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, uts, uas, quiz, banyak_tugas, nilai_tugas):
        self.nama = nama
        self.nim = nim
        self.uts = uts
        self.uas = uas
        self.quiz = quiz
        self.banyak_tugas = banyak_tugas
        self.nilai_tugas = nilai_tugas

    def hitung_nilai_akhir(self):
        rata_tugas = sum(self.nilai_tugas) / self.banyak_tugas
        nilai_akhir = 0.3 * self.uts + 0.4 * self.uas + 0.1 * self.quiz + 0.2 * rata_tugas
        return nilai_akhir

    def hitung_indeks_dan_predikat(self, nilai_akhir):
        if 85 <= nilai_akhir <= 100:
            indeks = "A"
            predikat = "Sangat Baik"
        elif 70 <= nilai_akhir < 85:
            indeks = "B"
            predikat = "Baik"
        elif 55 <= nilai_akhir < 70:
            indeks = "C"
            predikat = "Cukup"
        elif 40 <= nilai_akhir < 55:
            indeks = "D"
            predikat = "Kurang"
        else:
            indeks = "E"
            predikat = "Tidak Lulus"

        return indeks, predikat

    def tampilkan_info(self):
        nilai_akhir = self.hitung_nilai_akhir()
        indeks, predikat = self.hitung_indeks_dan_predikat(nilai_akhir)

        print("\nInformasi Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Nilai UTS: {self.uts}")
        print(f"Nilai UAS: {self.uas}")
        print(f"Nilai Quiz: {self.quiz}")
        print(f"Banyak Tugas: {self.banyak_tugas}")
        for i in range(self.banyak_tugas):
            print(f"Nilai Tugas ke-{i + 1}: {self.nilai_tugas[i]}")
        print(f"Rata-rata Nilai Tugas: {sum(self.nilai_tugas) / self.banyak_tugas:.2f}")
        print(f"Nilai Akhir: {nilai_akhir:.2f}")
        print(f"Nilai Indeks: {indeks}")
        print(f"Nilai Predikat: {predikat}")

# Proses input data mahasiswa
def input_mahasiswa():
    try:
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        quiz = float(input("Masukkan nilai Quiz: "))
        banyak_tugas = int(input("Masukkan banyak tugas: "))
        nilai_tugas = []
        for i in range(banyak_tugas):
            nilai = float(input(f"Masukkan nilai Tugas ke-{i + 1}: "))
            nilai_tugas.append(nilai)
        return Mahasiswa(nama, nim, uts, uas, quiz, banyak_tugas, nilai_tugas)
    except ValueError:
        print("Error: Nilai harus berupa angka.")

# Program utama
if __name__ == "__main__":
    try:
        mahasiswa = input_mahasiswa()
        mahasiswa.tampilkan_info()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
