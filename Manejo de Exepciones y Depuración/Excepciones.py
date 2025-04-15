try: 
    #Código 
except AlgunaExecepión as e:
    #Codigo
else:
    #Código
finally:
    #Codigo
    
#Algunas excpeciones comunes:
try:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print("La division entre Cero no se puede logar")
        return None