class pegawai :
    jumlah_pgw = 0

    def __init__(self, nama, jenkel, alamat, telepon, gaji):
        self.nama = nama
        self.jenkel = jenkel
        self.alamat = alamat
        self.telepon = telepon
        self.gaji = gaji
        pegawai.jumlah_pgw += 1

        def tampil_jumlah(self):
            print ("total pegawai %d" % pegawai.jumlah_pgw)

        def tampil_profil(self):
            print("nama :", self.nama, ", jenis kelamin: ", self.jenkel, "alamat : ", self.alamat, "telepon : ", self.telepon, "gaji : ", self.gaji)

pgw1 = pegawai("Restu Singgih", "L", "Jakarta", "087809299090", 4500000)
pgw2 = pegawai("Nilam Cahya", "P", "Cirebon", "081290902323", 7850000)

pgw1.tampil_profil()
pgw2.tampil_profil()
print("Total Pegawai : ", pegawai.jumlah_pgw)