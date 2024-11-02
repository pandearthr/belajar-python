import collections

mhs = collections.namedtuple('mhs', ['nama', 'usia', 'tgllahir'])

S = mhs('Nandini', '19', '25-04-1997')

print("Usia Mahasiswa menggunakan Index : ", end="")
print(S[1])

print("Nama mahasiswa menggunakan keyname : ", end="")
print(S.nama)

print("Tanggal lahir menggunakan fungsi getattr() : ", end="")
print(getattr(S, 'tgllahir'))