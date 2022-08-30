def area_tri (b,a):
    #area = base * altura / 2
    return b * a /2

def area_circulo (r):
    return 3.1416 * r**2


print("calcular area del triangulo y un circulo:")
base = float (input("ingrese base del triangulo: "))
altura =float (input("ingrese altura del triangulo: "))

radio = float(input(" \ningrese el radio del circulo: "))

area = area_tri(base,altura)
circulo = area_circulo(radio)
print("\nel area es del trialgulo es  " , round(area,2))
print("el area es del circulo es  " , round(circulo,2))


