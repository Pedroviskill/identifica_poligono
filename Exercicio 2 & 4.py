#Número de lados
#Exercício 2 

import math


numlado=int(input("insira o número de lados:  "))

if numlado == 3:
    lado1 = float(input("Insira a medida do Base:  "))
    lado2 = float(input("Insira a medida do Altura:  "))
    lado3 = float(input("Insira a medida do lado 3:  "))
    if (lado1 == lado2) & (lado2 == lado3):
       
        area= ((lado1**2)* math.sqrt(3))/4
        print("O valor da área é:  ", area)
        
    else:
            if (lado1 == lado2) and (lado2 != lado3) or (lado2 == lado3) and (lado3 != lado1):
                area=(lado1*lado2)/2 
                print("O valor da área é:  ", area)

            else:
                if (lado1 != lado2) & (lado2 != lado3):
                    area=(lado1*lado2)/2
                    print("O valor da área é:  ", area)

if numlado ==4:
    lado1 = float(input("Insira a medida do Base:  "))
    lado2 = float(input("Insira a medida do Altura:  "))
    
    area= lado1*lado2
    print("O valor da área é:  ", area)

if numlado ==5:
    lado1 = float(input("Insira a medida do Lado:  "))
    lado2 = float(input("Insira a medida do Lado:  "))
    area= ((3*lado1**2)*math.sqrt(3))/2
    print("O valor da área é:  ", area)


if numlado>5:
     print("NÃO É UM POLIGONO")
else:
     if numlado<3:
          print("Não é um poligono")