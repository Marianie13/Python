#El bloque try se utiliza para envolver el codigo que puede generar excepciones. Si ocurre una excepción.add()

try:
    num = int(input("Ingrese un numero: "))
    
    print(f"El doble es: {num*2}")

except ValueError:
    print("Error: No ingresaste un numero valido")
#Se ejecuta else solo si ocurre ninguna excepcion dentro del bloque
else:
    print(f"El numero ingresado es: {num}")

#TODO:El bloque finally se ejecuta siempre, indepedientemete de si ocurre  o no ocurre una excepción.
#Es util para liberar recursos, cerrar archivos conexiones o bases de datos, etc.add()
try:
    archivo = open("archivo.txt","r")
    contenido = archivo.read()
except FileNotFoundError:
    print('Error: El archivo no exite')
finally:
    try:
       archivo.close()
       print("Archivo cerrado")
    except NameError:
       print("El archivo no se abrio, no hay que cerrar")

#TODO:Bloque multiples  excepciones   
#Puedes manejar diferentes tipos de exepciones en el bloque separados por
#excep
try:
    num = int(input("Ingresa un numero: "))
    resultado = 10/num
except ValueError:
    print("Error : no ingrese un numero valido.")
except ZeroDivisionError:
    print("Error: nos e puede dividir por 0")

#TODO:Creacion  de excepcion personalizada

class misExcpeciones(Excepcion):
    def__init__(self,mensaje)
    super(). __init__(mensaje)
    
try:
    edad = int(input("Ingrese su edad: "))
    if edad <0:
        raise misExcpeciones("La edad no puede ser negativa")
    print(f"Tu edad es{edad}")
except misExcpeciones as e:
    print(f"Error: {e}")
    




    
    