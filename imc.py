# Programa para calcular el IMC

# 1. Pedir datos al usuarios
nombre = input("escribe tu nombre: ")
edad = input("esctibe tu edad: ")
peso = input("escribe tu peso en kg: ")
estatura = input("escribe tu estatura en metros: ")
# 2. Convertir al tipo correcto(casting)
edad = int(edad)      # número enteros
peso = float(peso)    # con decimales
estatura = float(estatura)  # con decimales
# 3. Calcular el IMC
imc = peso / (estatura ** 2)
# 4. Mostrar resultados
print("\nResultado: ")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg ")
print(f"Estatura: {estatura} m")
print(f"Tu IMC es: {imc: .2f}")
 


