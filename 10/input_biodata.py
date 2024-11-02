import hitunggaji
import hitunglembur

global id, nama, golongan, jml_lembur

def isi_biodata():
    print("\nModul Utama Pegawai")
    print("----------------------------------")
    print("ID Pegawai : ", nama)
    print("Golongan Kerja: ", golongan)
    print("jumlah lembu : ", jml_lembur)

    gj = hitunggaji.get_gaji(golongan)
    print("gaji pegawai: ", gj)

    lb = hitunglembur.get_lembur(jml_lembur)
    print("honor lembur :", lb)

id = input("masukkan ID Pegawai : ")
nama = input("Masukkan Nama Pegawai : ")
golongan = input("Masukkan Golongan Kerja : ")
jml_lembur = int(input("Masukkan Jumlah Lembur : "))
