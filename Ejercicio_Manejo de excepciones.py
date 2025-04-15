try:
    num = int(input("Ingrese un numero: "))
    
    print(f"El doble es: {num*2}")

except ValueError:
    print("Error: No ingresaste un numero valido")
else:
    print(f"El numero ingresado es: {num}")
    
    