from modelo import *

class Menu:

    def agregar_moto(self) -> None:
        placa = input("ingrese la placa de la moto: ")
        modelo = input("ingrese el modelo de la moto (año de fabricacion): ")
        marca = input("ingrese la marca de la moto: ")
        cilindraje = input("ingrese el cilindraje: ")
        categoria = input("ingrese la categoria (1 para nueva - 2 para usada): ")
        precio_unitario = float(input("ingrese el precio: "))
        Compraventa.ingre_moto.append(Moto(placa, modelo, marca, cilindraje, categoria, precio_unitario))

    def menu(self):

        opciones = {1: self.agregar_moto, 2: Compraventa().catalogo_moto, 3: Compraventa().registrar_usuario()}

        while (True):
            print("Mande 1 para ingresar moto")
            print("Mande 2 para ver catalogo motos por modelo")
            print('Mande otro. salir')
            opcion = int(input("elige una opcion: "))
            # Con cualquier otro numero diferente a 1 o 2, salir

            if opcion not in opciones.keys():
                break;
            opciones[opcion]()


if __name__ == '__main__':
    Menu().menu()
