from math import *
from random import * 

arv_tekstina = input('Palun sisesta mingi arv: ')
arv = float(arv_tekstina)

if arv < 10000:
    vastus = arv
else:
    vastus = -arv
print('Selle arvu absoluutväärtus on ' + str(vastus))