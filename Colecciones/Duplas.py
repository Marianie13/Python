#App para registro de empleados

from typing import Tuple

def obtener_info_empleado(empleado: Tuple[int, str, str]) ->Tuple:
    
    id_empleado, nombre_empleado, cargo_empleado = empleado
    print(f"id: {id_empleado}, Nombre:{nombre_empleado}, Cargo:{cargo_empleado}")
    
def analizar_salario(salarios: Tuple[int, ...])-> None:
    
    print(f"saliros tabulados: {salarios}")
    print(f"Cantidad de salarios: {len(salarios)}")
    print(f"El salario mas alto registrado es: {max(salarios)}")
    print(f"El salario mas bajo registrado es: {min(salarios)}")
    print(f"La suma de todos los salarios registrados es: {sum(salarios)}")
    print(f"Los salarios registrados de forma ordenada: {sorted(salarios)}")
    
    
    salario_a_buscar = 500
    print(f"El salario {salario_a_buscar} se encuentra en la lista de salarios: {salarios.count(salario_a_buscar)} veces")
    
    if salario_a_buscar in salarios:
        print(f"El salario con un valor  de{salario_a_buscar} se encuentra en la posicion {salarios.index(salario_a_buscar)}")


def main():
    empleado = (111111, "Cristian Rubio", "Director de Desarrollo")
    
    obtener_info_empleado(empleado)
    
    salarios_de_empleados= (5000, 2000, 3000, 4000, 5000)
    
    analizar_salario(salarios_de_empleados)
    
if __name__ == "__main__":
    main()