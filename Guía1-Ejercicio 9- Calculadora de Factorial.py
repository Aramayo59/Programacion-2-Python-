# Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. El programa debe manejar números enteros grandes y mostrar el resultado.
num = int(input("Ingresa un número: "))


factorial = 1
for i in range(1, num + 1):
    factorial *= i


print("El factorial de", num, "es:", factorial)
