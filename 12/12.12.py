randomlist = ['a', 0, 2]

for i in randomlist:
    try:
        print("nilai yang diinput adalah : ", 1)
        r = 1/int(i)
        break
    except Exception as e:
        print("maaf!", e.__class__, " terjadi.")
        print()
print("nilai kebalikan dari : ", i, ":adalah : ", r)
