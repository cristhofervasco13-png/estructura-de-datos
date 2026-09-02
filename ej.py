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