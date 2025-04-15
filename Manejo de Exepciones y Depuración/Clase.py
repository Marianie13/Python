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
"""


def division_segura():
    try:
        numerador = int (input("Ingrese porfavor el numerador de la división: "))
        denominador = int(input("Ingrese por favor el denominador de la división: "))
        resultado = numerador / denominador
        print(f"El resultado de la división de {numerador} entre el {denominador} es igual a: {resultado}")
    except(ZeroDivisionError, ValueError) as e:
        print(f"Error {e}")
        
division_segura()
    
"""
#Manejo de expeciones especificas "Exception" no es recomendable siempre por que suele tener errores

"""
def abrir_archivo():
    try:
        with open("daros.txt", "r") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            print("numero")
    except Exception as e:
      print(f"Se produjo un error")
      
abrir_archivo()

"""
#Uso del else y finally
#Ejercico de division por cero
"""
def division_completa():
    try:
        numero = int(input("Ingrese un número: "))
        resultado = 10 / numero 
        print(f"El resultado de la división es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error {e}")
    else: 
        print(f"El resultadode la división es {resultado}")
    finally:
        print("La operación finalizo")

division_completa()
"""
#App que permite procesar pedidos
#Validar el codigo del producto sea alfanumerico
#Validar que la cantidad sea mayor a cero

"""
def procesar_pedido():
    try:
        codigo_producto = input("Ingrese el codigo del producto: ")
        cantidad = int(input("Ingrese la canridad del producto: "))
        
        if not codigo_producto.isalnum():
             raise ValueError("El codigo del producto debe ser lfanumerico")
        
        if not cantidad >= 0:
            raise ValueError("la cantidad del producto debe ser mayor a cero")
        
        precio_unitario = 50
        total = precio_unitario * cantidad
    
    except ValueError as e:
        print(f"Error al procesar el pedido: {e}")
    else: 
        print(f"Total a pagar {total}")
    finally:
        print(f"Operacion finalizada")
    
procesar_pedido()

"""
#Execepciones personalizadas 

class ErrorDePago(Exception):
    """Gestión de excepciones"""
    pass

class PasaleraDePago():
    """Simulacion una estragia tecnologica de pago"""
    
    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
         
         if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("El numero de la tarjeta no es valido")
         if monto <=0:
             raise ErrorDePago("El monto debe ser mayor a cero")
         return f"Pago del ${monto} fue procesado con éxito"
    
def procesar_pago_cliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"Iniciando el proceso de pago para {nombre_cliente}")
        resultado = PasaleraDePago.procesar_pago(numero_tarjeta, monto)
    except ErrorDePago as e:
        print(f"Error al procesar el pago {e}")
    except Exception as e:
        print(f"Se produjo un erro insperadoe {e}")
    else:
        print(resultado)
    finally:
            print(f"Registro finalizado")
if __name__ =="__main__":
    #procesar_pago_cliente("Jose","43234", 99.79)
    #procesar_pago_cliente("Luis", "123454", 180)
    procesar_pago_cliente("Carolina","492849", 0)
    
    
    
       
         
         
    
            
            
            
            