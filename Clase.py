#App  que permita dividir dos numeros 
"""
#Con captura de expeciones

def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print("La division entre Cero no se puede logar")
        return None

division_cero(2,0)

"""
#Mismo ejercici explicando las execiones multiples

def division_segura():
    try:
        numerador = int (input("Ingrese porfavor el numerador de la división: "))
        denominador = int(input("Ingrese por favor el denominador de la división: "))
        resultado = numerador / denominador
        print(f"El resultado de la división de {numerador} entre el {denominador} es igual a: {resultado}")
    except(ZeroDivisionError, ValueError) as e:
        print(f"Error {e}")
        
division_segura()
    