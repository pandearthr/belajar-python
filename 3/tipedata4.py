#list kosong
list_kosong = []

#list yang berisi kumpulan string
list_buah = ['pisang', 'nanas', 'melon', 'durian']

#list yang berisi kumpulan integer
list_nilai = [80, 70, 90, 60]

#list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'presiden soekarno', False]

#cetak isi seluruh list
print('list_kosong:', list_kosong)
print('list_buah:', list_buah)
print('list_nilai:', list_nilai)
print('list_jawaban:', list_jawaban)
print("\n")

#cetak isi list tertentu
print(list_buah [0])
print(list_buah[1])
print(list_buah[2])
print(list_buah[3])
print("\n")

#cetak isi list menggunakan index negatif untuk mencetak dari belakang
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

#NB: yang perlu diperhatikan adalah: bahwa indeks negatif
#tidak dimulai dari 0, akan tetapi dimulai dari angka 1.