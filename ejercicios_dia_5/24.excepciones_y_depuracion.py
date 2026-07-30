try:
    valor1 = int(input("Ingrese valor 1: "))
    valor2 = int(input("Ingrese valor 2: "))
    division = valor1 / valor2
    
except ZeroDivisionError:
    print("No se puede dividir para cero")

# ValueError
# ZeroDivisionError

try:
    valor3 = int(input("Ingrese un valor: "))
    resultado = valor3 **4
    print(resultado)
except ValueError:
    print("El valor no es el correcto, debe ingresar un valor numérico")