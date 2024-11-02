# Modul untuk mengelola data karyawan
class Karyawan:
    def __init__(self, nik, nama_lengkap, umur, masa_kerja, gaji_pokok, bagian, jabatan):
        self.nik = nik
        self.nama_lengkap = nama_lengkap
        self.umur = umur
        self.masa_kerja = masa_kerja
        self.gaji_pokok = gaji_pokok
        self.bagian = bagian
        self.jabatan = jabatan

# Fungsi untuk memeriksa apakah nilai adalah integer
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Proses input data karyawan
def input_karyawan():
    try:
        nik = input("NIK: ")
        nama_lengkap = input("Nama Lengkap: ")
        umur = input("Umur: ")
        masa_kerja = input("Masa Kerja: ")
        gaji_pokok = input("Gaji Pokok: ")
        bagian = input("Bagian: ")
        jabatan = input("Jabatan: ")

        if is_integer(umur) and is_integer(masa_kerja) and is_integer(gaji_pokok):
            return Karyawan(nik, nama_lengkap, int(umur), int(masa_kerja), int(gaji_pokok), bagian, jabatan)
        else:
            print("Data yang Anda input salah, silakan dicoba lagi.")
            return None
    except ValueError:
        print("Data yang Anda input salah, silakan dicoba lagi.")
        return None

# Program utama
if __name__ == "__main__":
    karyawan = input_karyawan()
    if karyawan:
        print("\nInformasi Karyawan:")
        print(f"NIK: {karyawan.nik}")
        print(f"Nama Lengkap: {karyawan.nama_lengkap}")
        print(f"Umur: {karyawan.umur}")
        print(f"Masa Kerja: {karyawan.masa_kerja}")
        print(f"Gaji Pokok: {karyawan.gaji_pokok}")
        print(f"Bagian: {karyawan.bagian}")
        print(f"Jabatan: {karyawan.jabatan}")
