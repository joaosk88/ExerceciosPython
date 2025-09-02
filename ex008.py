#Leia um valor em metros e o exiba em centimetros e milimetros
medida = float(input('Digite uma metragem'))
cm= medida*  100
mm= medida*  1000
km= medida/  1000

print('a medida {}m corresponde a:\n CM {:.0f}\n MM {:.0f}\n KM{}'.format(medida, cm,mm,mm))