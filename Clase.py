#App  que permita dividir dos numeros 

def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print("La division entre Cero no se puede logar")
        return None

division_cero(2,1)

    
    