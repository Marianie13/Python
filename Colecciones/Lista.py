#App: Gestion de pedidos de una tienda 
def agregar_pedido(pedidos: list[str], nuevo_pedido: str) -> list[str]:
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos:list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print("El pedidono se encuentra en la lista")
    return pedidos

def buscar_pedido(pedidos:list[str], pedido_a_burcar: str) -> int:
    if pedido_a_burcar in pedidos:
       return  pedidos.index(pedido_a_burcar)
    else:
        print("El pedido no se encutra en la lista")
    return -1

#Ejecucion del modulo
def main():
    #Lista incial de pedidos
    pedidos_tienda = ["Pedido1", "Pedido3"]
    
   #Agregar un nuevo pedido a la tienda
    pedidos_tienda = agregar_pedido(pedidos_tienda, "Pedidos2")
    
    #Mostrar los elmentos de la lista de forma desordenada
    print("Lista actualizada de pedidos", pedidos_tienda)

    #Ordene la lista
    pedidos_tienda.sort()
    print("Lista de pedidos ordenadas", pedidos_tienda)
    
    #Buscar un pedido en especifico
    pedido_a_buscar = "Pedido 3"
    indice = buscar_pedido(pedidos_tienda, pedido_a_buscar)
    if indice != -1:
        print(f"El {pedido_a_buscar} se encuentra en la posicion{indice}")
        
    #Eliminar un pedido de la lista
    pedido_a_eliminar = "Pedido 1"
    pedidos_tienda = eliminar_pedido(pedidos_tienda, pedido_a_eliminar)
    print("La lista resultante luego de elimar a {pedido_a_eliminar} es {pedido_tienda}")
    
    
    
if __name__ == "__main__":
    main()    
    
       
    
    
    