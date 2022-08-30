

def anio_bi (a):
    if a % 4==0:
        if a % 100==0:
            if a % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print("saber si un anio es bisiesto.")
anio = int(input("ingrese al anio para saber si es bisiesto: "))

#while type(anio) != int:
#    print("ingrese datos validos:")
#200    anio = int (input("ingrese el anio para ver si es bisiesto: "))

if anio_bi(anio) == True:
    print("el anio ", anio, "es bisiesto")
else:
    print("el anio ", anio, "No es bisiesto")