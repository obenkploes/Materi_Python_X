import random

no = 0
tebak =random.randint(1,20)
while no != tebak:
    no = int(input('Masukkan tebakanmu :'))
    if no == tebak:
        print('Tebakanmu benar')
    else:
        if no < tebak:
            print('Kurang sedikit')
        else:
            print('Kelebihan sedikit')