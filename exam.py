import random


cantidad = int(input("Ingrese la cantidad de números a validar: "))


numeros = []
for i in range(cantidad):
    numero = random.randint(100, 99999)
    numeros.append(numero)

print("\nNúmeros generados:", numeros)


for n in numeros:
   
    suma_digitos = 0
    for d in str(n):
        suma_digitos += int(d)
    
  
    invertido = int(str(n)[::-1])
    
    
    if suma_digitos % 2 == 0 and invertido % 3 == 0:
        print(n, "-> Sí es camaleón")
    else:
        print(n, "-> No es camaleón")