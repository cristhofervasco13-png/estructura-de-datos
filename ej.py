#JS vs Python
#convertir grados celcius a fahrenheit
celsius= int(input("ingrese una cantidad: "))
fahrenheit= celsius * 9/5 + 32
print(f"{celsius} grados celsius son {fahrenheit}°F grados fahrenheit")

#segundos a horas, minutos y segundos
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")

#intercambiar dis variables 
a= 5, b= 8
a, b = b, a
print(f"a = {a}, b = {b}")

#calcular el IVA del 15%
precio = int(input("ingrese el precio: "))
precio_iva = precio * 0.15
precio_total = precio_iva + precio
print(f"su precio a pagar es: {precio_total}")


#VARIABLES Y OPERADORES 
#sumar digitos de un numero de tres cifras
numero = int(input("Número de 3 cifras: "))

centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10

suma = centenas + decenas + unidades
print(f"Suma: {suma}")

#convertir minutos a horas
total = int(input("Minutos totales: "))

horas = total // 60
mins = total % 60

print(f"{horas} horas {mins} minutos")

#indice de masa corporal
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")

#redondeo por cifra decimal
num = float(input("Número: "))
dec = int(input("Decimales: "))

resultado = round(num, dec)
print(resultado)

#descuento por cantidad
PRECIO = 12
cant = int(input("Cantidad: "))

if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")

#CONTROL DE FLUJO
#tabla de multiplicar
n = int(input("tabla de: "))
for i in range(1, 13):
   print(f"{n} x {i} = {n * i}")

#contar digitos de un numero
num = int(input("numero: "))
n = abs(num)
digitos = 0
if n == 0 :
    digitos = 1
else:
    while n > 0:
        digitos += 1
        n = n // 10        
print(f"{digitos} dígitos")

#suma de imparares
n = int(input("¿Cuántos números? "))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f"Número {i+1}: "))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")

#validar entrada
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                      
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")

#adivina el numero
import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")

#serie de fibonacci
n = int(input("¿Cuántos? "))
a, b = 0, 1                         

for _ in range(n):                 
    print(a, end=" ")
    a, b = b, a + b                

print()                            
