keep_asking = True
while keep_asking: 
    try : 
        x = int(input("masukkan nilai x : "))
        print("50 dibagi dengan ", x, "hasilnya adalah :", 50/x)
    except ValueError :
        print("nilai yang anda masukkan bukan integer, silahkan ditunggu kembali..!!")
