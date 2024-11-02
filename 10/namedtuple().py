import collections

mhs = collections.namedtuple('mhs', ['nama' 'mhs', 'usia', 'tgllahir'])

S = mhs('Nandini', '19', '25-04-1997')

li = ['Manjeet', '19', '411997']

dict = {'nama': 'Nikhil', 'usia': 19, 'tgllahir': '1391997'}

print("Namedtuple menggunakan fungsi _make() : ")
print(mhs._make(li))

print("OrderDist menggunakan fungsi _asdict() : ")
print(S._asdict())

print("Namedtuple menggunakan operator ** : ")
print(mhs(**dict))