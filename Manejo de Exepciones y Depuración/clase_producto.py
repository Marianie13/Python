import logging
from dataclasses import dataclass, field
"""
# Configuración del logging para archivo y consola
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Handler para archivo
file_handler = logging.FileHandler('registro.log', mode='a')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Agregar handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
"""
# Clase Producto
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"No hay suficiente cantidad del producto {self.nombre}.El stock disponible es: {self.cantidad}")
            print(f"No hay suficiente cantidad de producto{self.nombre} el stock disponible es de{self.cantidad}")
            raise ValueError(f"No hay suficiente cantidad del producto {self.nombre} El stock disponible{self.cantidad}")
        else:
            self.cantidad -= cantidad
            logging.info(f"Compra exitosa: {cantidad} unidades de {self.nombre}. Stock restante: {self.cantidad}")
            print(f"La compra fue exitosa. Stock restante{self.cantidad}")
            return self.precio * cantidad

# Clase Tienda
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f"{producto.nombre} agregado. Precio: {producto.precio}, Stock: {producto.cantidad}")
        print(f"{producto.nombre} agregado con exito. El precio es de  {producto.precio}cantidad {producto.cantidad} unidades en stock")
    
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f"Total de la compra: ${total}")
                print(f"Compra realizada {cantidad} unidades de {nombre_producto} por un total ${total}")
                return total
            except ValueError as e:
                logging.error(f"Error en la compra: {e}")
        else:
            logging.warning(f"Producto {nombre_producto} no encontrado en la tienda.")

# Código principal
if __name__ == "__main__":
    tienda = Tienda()

    inventario_portatil = Producto(nombre="Portátil", precio=1000, cantidad=10)
    tienda.agregar_producto(inventario_portatil)

    tienda.realizar_compra("Portátil", 4)

    
    
        

    