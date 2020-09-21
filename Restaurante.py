class Cliente:
    def __init__(self):
        pass

    def ordenar(self, orden, menu, opcionMenu):
        if(opcionMenu not in menu.lista):
            return "No existe esta opcion"
        else:
            orden.opcionesMenu.append(opcionMenu)
            return "Se añadio {} a la Orden".format(opcionMenu)

    def solicitarCuenta(self, mesero):
        total = mesero.entregarOrden()
        self.pagarCuenta(mesero,total)

    def pagarCuenta(self, mesero, total):
        mesero.cobrarCuenta()
        return "Se pagaron {} de la cuenta".format(total)

class Orden:
    def __init__(self):
        self.opcionesMenu = []

    def cancelar(self):
        self.opcionesMenu = []
        return "Orden cancelada"

    def __str__(self):
        if(len(self.opcionesMenu) == 0):
            return "Orden vacia"
        else:
            return "Opciones de menu en la orden {}".format(str(self.opcionesMenu)[1:-1]  )

class  Menu:
    def __init__(self, lista):
        self.lista = lista


#Cliente
cliente = Cliente()

#Menu
opcionesMenu = ['Agua','Carne','Tacos','Ensalada']
menu = Menu(opcionesMenu)

#Orden
orden = Orden()

print(cliente.ordenar(orden,menu,'Tamarindo'))
print(cliente.ordenar(orden,menu,'Carne'))
print(cliente.ordenar(orden,menu,'Agua'))
print(orden)
print(orden.cancelar())
print(orden)
