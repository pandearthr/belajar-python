saldo = 1000000      
bunga = 0.02         

for bulan in range(1, 11):   
    saldo = saldo + (saldo * bunga)

print("Jumlah uang setelah 10 bulan adalah: Rp", int(saldo))
