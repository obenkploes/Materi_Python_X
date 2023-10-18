import random

angka_rahasia = random.randint(1,100)

angka_tebak = 0
kesempatan = 1

print('Game tebak angka')
print('Masukkan angka dari 1 - 100')

while angka_rahasia != angka_tebak and kesempatan < 6 :
    angka_tebak = int(input('Masukkan tebakanmu :'))
    if angka_tebak < angka_rahasia:
        print('Kekecilan bos!!!')
    elif angka_tebak > angka_rahasia:
        print('Kebesaran bos!!!')
    else:
        print('HOREE!!! KAMU MENANG!!!')    
    kesempatan += 1

if kesempatan > 5:
    print('Kesempatan menjawab habis !')
    