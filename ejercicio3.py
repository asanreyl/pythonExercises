precio_pro=float(input('Precio del producto en euros: '))
bille_mone=(500,200,100,50,20,10,5,1,0.50,0.20,0.10,0.05,0.02,0.01)
resultado={}

for i in bille_mone:
    contador_bille=0
    while precio_pro >= i:
        contador_bille += 1
        precio_pro= precio_pro-i
    resultado[i]=contador_bille
 
for a in resultado:
    if a >=5:
        print('Número de billetes de', a, ':',  resultado[a])
    else:
        print('Número de monedas de ', a, ':', resultado[a])

