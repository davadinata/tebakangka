import random
import os

rand = random.randint(1,10)
print('='*40)
print(' '*6,'PERMAINAN TEBAK ANGKA MUDAH',' '*7)
print(' '*3,'HANYA BISA MENEBAK SEBANYAK 5 KALI  ')
print('='*40)
p = 3
rep = str

while p > 0:
    answ=int(input("Masukan Angka = "))

    if answ > rand :
        p -= 1
        print("Angka Terlalu Besar")
        print(f'Kesempatan menjawab tersisa {p} \n')

    if answ < rand :
        p-=1
        print("Angka Terlalu Kecil")
        print(f'Kesempatan menjawab tersisa {p} \n')
            
    if answ == rand: 
        p-=1
        print("Selamat, Jawaban Benar!")
        print('Tersisa', p ,'kali kesempatan menjawab \n')
        break
    
if p == 0 :
    print("Kesempatanmu Habis!")
    print('Jawaban adalah', rand)

rep = str(input("Lagi Y or N?"))
if rep == 'Y':
    os.system('cls')
    import tebak_angka
if rep == 'N':
    exit()
if rep == 'y':
    os.system('cls')
    import tebak_angka
if rep == 'n':
    exit()