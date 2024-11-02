try: 
    a = int(input("masukkan nilai a : "))
    b = int(input("masukkan nilai b : "))
    c = a / b
    print("nilai c adalah : ", c)
except Exception as e:
    print("data yang andaa masukkan salah..!!", e.__class__)
    