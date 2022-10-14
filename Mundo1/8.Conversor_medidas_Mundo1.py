#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite uma distancia em metros: "))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
dam = medida / 10
hm = medida / 1000
# dm = decimetros, dam = decametros, hm = hectometro

print("A distacia de {} metros, corresponde a {:.0f} centimetros e {:.0f} milimetros e {:.0f} decimetros e {:.0f} Kilometros e {:.0f} decametros e {:.0f} hectometros.".format(medida, cm, mm, dm, km, dam, hm))