#Listas
productos = ["Carne", "Papa", "Tomate"]
productos.append("Yuca")
print(productos)

#Tupla
empleado =[1010, "Luis Molero", "Director", 150000]
print(empleado) 
empleado[1] = "Camilo Pardo"
print(empleado)

#Set (Conjuntos) en Python
categorias = {"Terror", "Drama", "Scfc"}
categorias.add("Susoenso")
print(categorias)

#Diccionarioas (dict) en pyton

clientes = {
    "id": 1010,
    "Nombre": "luis",
    "Apellido": "Molrero"
}
print(clientes)
clientes["email"] = "luis@gmail.com"
print(clientes)