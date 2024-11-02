try :
    x=input(input('masukkan angka hingga 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "berada diluar jangkauan nilai")
else:
    print(x, "berada dalam jangkauan nilai")
    