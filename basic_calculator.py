print("Calculadora basica de SUMA RESTA DIVISION Y MULTIPLICACION")
print("---")
# Creamos las funciones para las operaciones basicas (Suma, resta, multiplicacion y division)
def suma(a, b):
    x = a + b
    print(f"{str(a)} + {str(b)} = {str(x)}")

def resta(a, b):
    x = a - b
    print(f"{str(a)} - {str(b)} = {str(x)}")

def mult(a, b):
    x = a * b
    print(f"{str(a)} * {str(b)} = {str(x)}")

def div(a, b):
    x = a / b
    print(f"{str(a)} / {str(b)} = {str(x)}")

# Damos las opciones de las distintas operaciones
print("A. Suma")
print("B. Resta")
print("C. Multiplicacion")
print("D. Division")
print("E. Salir")
print("---")

# Creamos el input para que el usuario pueda elegir entre alguna de las opciones de calculo.
opcion = input("Elegi una opcion: ")
if opcion.lower() == "a" or opcion.lower() == "suma":
    print("Suma dos numeros")
    a  = int(input("Introduce el primer numero: "))
    b  = int(input("Introduce el segundo numero: "))
    suma(a,b)
elif opcion.lower() == "b" or opcion.lower() == "resta":
    print("Resta dos numeros")
    a  = int(input("Introduce el primer numero: "))
    b  = int(input("Introduce el segundo numero: "))
    resta(a,b)
elif opcion.lower() == "c" or opcion.lower() == "multiplicacion":
    print("Multiplica dos numeros")
    a  = int(input("Introduce el primer numero: "))
    b  = int(input("Introduce el segundo numero: "))
    mult(a,b)
elif opcion.lower() == "d" or opcion.lower() == "division":
    print("Divide dos numeros")
    a  = int(input("Introduce el primer numero: "))
    b  = int(input("Introduce el segundo numero: "))
    div(a,b)
elif opcion.lower() == "e" or opcion.lower() == "salir":
    print("Aguarde un momento. Apagando...")
    quit
# En el caso de que ninguna de las opciones sean correctas, saltara una alerta notificandolo.
else:
    print("Opcion incorrecta. Por favor, elige entre las opcion que les brindamos.")