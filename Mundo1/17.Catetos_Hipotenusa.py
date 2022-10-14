from math import hypot

#co = cateto oposto |
#ca = cateto adjacente -
#hi = hipotenusa

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co,ca)

print("A hipotenusa vai medir {:.2f}.".format(hi))


