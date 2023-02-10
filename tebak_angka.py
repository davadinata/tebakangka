import os

print('='*40)
print(' '*10,'PERMAINAN TEBAK ANGKA',' '*9)
print('  HANYA BISA MENEBAK SEBANYAK 5 KALI  ')
print('='*40)
print("Level:")
print('1. Mudah')
print('2. Medium')
print('3. Susah')
lvl=int(input('Pilih Level : '))

if lvl == 1:
    os.system('cls')
    import mudah
if lvl == 2:
    os.system('cls')
    import medium
if lvl == 3:
    os.system('cls')
    import susah
