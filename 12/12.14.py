keep_asking = True
while keep_asking:
    try :
        x = int(input("masukkan nilai x : "))
    except ValueError :
        print("data yang diinput bukan integer, silahkan coba kembali ..")
    else : 
        print("50 dibagi dengan" , x,"hasilnya adalah : ", 50/x)
