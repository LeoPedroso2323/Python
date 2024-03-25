import time
numero1 = int(input("Digite um  número positivo:"))

if numero1 % 2 == 0 and numero1 >=0:
    print('""P-A-R!!""')
else:
    print("Tente outra vez")

time.sleep(2)