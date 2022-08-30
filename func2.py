def num_primo (n):
    if n <= 0:
        return False    

    for i in range(2,n):
        if n%i == 0:
            return False
    return True
print("verificador de numeros primos")
num = int(input("ingrese el numero: "))
#primo = num_primo(num)
if num_primo(num)== True:
    print("el numero", num , " es un numero primo")
else:
    print('el numero', num , "NO ES un numero primo")


