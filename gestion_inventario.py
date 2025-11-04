"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: David Fernández Aido
Fecha: 4 de noviembre de 2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, nombre, contacto, codigo):
        # TODO: definir los atributos de la clase
        self.nombre = nombre
        self.contacto = contacto
        self.codigo = codigo

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        return f"'Nombre del Proveedor : ',{self.nombre}, 'Contacto Proveedor:',{self.contacto},'Codigo Proveedor',{self.codigo}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        # TODO: definir los atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = Proveedor()
        

    def __str__(self):
        # TODO: devolver una representación legible del producto
        return f"[{self.codigo}],{self.nombre}, '-',{self.precio},({self.stock}) '| Proveedor: '{self.proveedor}' ({self.proveedor.contacto}) "
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        # TODO: definir los atributos e inicializar la lista de productos
        self.nombre_fichero = nombre_fichero
        self.productos = []
        

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        pass

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        pass

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        for p in self.productos:
            if p.codigo == producto.codigo:
                print('codigo repetido')
                return
        self.productos.append(producto)
        print('Producto añadido')
            
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print('No hay productos')
        else:
            for p in self.productos:
                print(p)

        # TODO: mostrar todos los productos almacenados
        pass

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None
        # TODO: buscar un producto por código

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        producto = self.buscar(codigo)
        if producto:
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            if nuevo_stock is not None:
                producto.stock = nuevo_stock
            print('Producto modificado')
        else:
            print('No existe el producto')

        # TODO: buscar el producto y actualizar sus atributos
        
    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        producto = self.buscar(codigo)
        if producto:
            self.productos.remove(producto)
            print('Producto eliminado')
        else:
            print('No exite el producto')
        # TODO: eliminar el producto de la lista

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            codigo = input('codigo: ')
            nombre = input('nombre: ')
            precio = float(input('precio: '))
            stock = int(input('stock: '))
            nombreprov = input('nombre del proveedor: ')
            contactoprov = input('contacto del proveedor: ')
            proveedor = Proveedor(nombreprov, contactoprov)
            producto = Producto(codigo, nombre, precio, stock, proveedor)
            Inventario.anadir_producto(producto)
        elif opcion == '2':
            Inventario.mostrar()
        elif opcion == '3':
            codigo = input('Codigo del producto: ')
            producto = Inventario.buscar(codigo)
            if producto:
                print(producto)
            else:
                print('producto no encontrado')
        elif opcion == '4':
            codigo = input('Codigo del producto: ')
            nuevo_nombre = input('Nuevo nombre (dejar vacio si no cambia): ')
            nuevo_precio = float(input('Nuevo precio (dejar vacio si no cambia): '))
            nuevo_stock = int(input('Nuevo stock (dejar vacio si no cambia): '))
            Inventario.modificar(
                codigo,
                nuevo_nombre if nuevo_nombre else None,
                nuevo_precio if nuevo_precio else None,
                nuevo_stock if nuevo_stock else None,
            )
        elif opcion == '5':
            codigo = input('Codigo del producto: ')
            producto = Inventario.buscar(codigo)
            if producto:
                Inventario.eliminar(producto)
                print('eliminado')
            else:
                print('El producto no existe')
        elif opcion == '6':
            print('Opcion no creada')
        elif opcion == '7':
            print('Opcion no creada')
        elif opcion =='8':
            print('Hasta luego')
            break
        
        # TODO: implementar las acciones correspondientes a cada opción del menú


if __name__ == "__main__":
    main()
