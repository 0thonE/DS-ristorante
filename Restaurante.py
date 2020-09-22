from Ingredientes import OpcionMenu,Ingrediente,Platillo,Bebida,Complemento

class Cliente:
    mesaAsignada=None
    __ordenes= []

    def __init__(self):
        pass

    def ordenar(self, menu, opcionesMenu):
        orden=Orden()
        self.__ordenes.append(orden)
        for opcionMenu in opcionesMenu:
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
    lista = []

    def __init__(self, lista):
        self.lista = lista

    def agregar(self, opcion):
        self.lista.append(opcion)

    def eliminar(self, opcion):
        if(opcion not in self.lista):
            return "No existe esta opcion"
        else:
            self.lista.remove(opcion)
            return "Se elimin[o] {} de Menu".format(opcion)






#Cliente
cliente = Cliente()

# Preparables

#Datos de prueba
salchicha = Ingrediente('Salchicha', 10)
carne = Ingrediente('Carne', 10)
lechuga = Ingrediente('Lechuga', 10)
pan = Ingrediente('Pan', 1)
limon = Ingrediente('Limon', 10)
agua = Ingrediente('Agua', 10)
papas = Ingrediente('Papas', 10)
azucar = Ingrediente('Azucar', 10)

hamburguesa = Platillo('Hamburguesa', [lechuga, carne, pan], 'Hamburguesa de carne')
limonada = Bebida('Limonada', [agua, limon], 'Limonada natural')
papas_comp = Complemento('Papas',[papas], 'Complemento de papas')

combo_hamburguesa = OpcionMenu([hamburguesa, limonada, papas_comp], 33.5)
combo_hamburguesa2 = OpcionMenu([hamburguesa, limonada,limonada, papas_comp], 43.5)


#Resultados
print(combo_hamburguesa)
print(hamburguesa)
print(hamburguesa.preparar())
print(hamburguesa.preparar())
pan.surtir(5)
print(hamburguesa.preparar())
print(pan)


#Menu
menu = Menu([combo_hamburguesa,combo_hamburguesa2,hamburguesa,limonada])



print(cliente.ordenar(menu, [combo_hamburguesa]))
print(cliente.ordenar(menu,[combo_hamburguesa2]))

