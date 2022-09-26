# Primer Hola Mundo
import numbers


print("Hola Mundo")

# IMPRIMIR DATOS
saludo = "Hola soy un string"
print(saludo)

saludo2 = "Hola"
nombre = "Imanol"
print(saludo2 + " " +nombre)

# LECTURA DE DATOS
alert= "Ingresa tu nombre"
nombre2 = input()
print ("Hola" + "" + nombre2)

# OPERADORES ARITMETICOS
print("Ingresa el primer valor")
num1 = int(input())
print("Ingresa el segundo valor")
num2 = int(input())
resultado = num1 + num2
print(resultado)

# OPERADORES DE COMPARACION
print("Ingresa tu edad")
edad = int(input())
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# CASTING
print("Ingresa el primer valor")
num11 = int(input())
print("Ingresa el segundo valor")
num22 = int(input())
resultado2 = num11 + num22
print("El resultado es :" + str(resultado2))

# Arreglos
numeroos = [1,2,3,4,5]
#           0 1 2 3 4
print(numeroos[2])

# Declaracion de funciones
def saludar():
    print("Hola, te estoy saludando desde una funcion")
saludar()

# Argumento de funciones
def bienvenida (tuNombre):
    return "Bienvenido {}, estoy retornando una funcion".format(tuNombre)
print("Ingresa tu nombre")
tuNombre = input()
print(bienvenida(tuNombre))

# Ciclo While
rep = 1
while rep <= 3:
    print("mensaje")
    rep += 1
print("El ciclo se termino")

# Ciclo For
miNombre = "Imanol"
for elemento in miNombre:
    print(elemento)