masa_kerja = float(input("masukan masa kerja : "))
gaji_pokok = int(input("masukan gaji pokok : "))
if masa_kerja >= 10 :
    kenaikan_gaji = (20/100) * float(gaji_pokok)
else :
    kenaikan_gaji = (5/100) * float(gaji_pokok)

print("jumlah kenaikan gaji : ", kenaikan_gaji)
total_gaji = gaji_pokok + kenaikan_gaji
print("total gaji : ", total_gaji)