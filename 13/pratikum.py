number = 1
while number !=-1 :
    try :
        number = int(input("masukkan angka : "))
        print( "anda memasukkan : ", number)
    except ValueError :
        print ("bukan angka bilangan integer !")