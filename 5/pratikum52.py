NIP = input("masukan id number : ")
nama_pegawai = input("masukan nama pegawai : ")
gaji_pokok = int(input("masukan gaji pokok : "))

komisi = float(3.5/100) * float(gaji_pokok)
total_gaji = float(gaji_pokok) + komisi

print("\n")
print("\nData gaji pegawai")
print("================================")
print("NIP : ", NIP)
print("nama pegawawi : ", nama_pegawai)
print("gaji pokok : ", gaji_pokok)
print("komisi : ", komisi)
print("total gaji : ", total_gaji)