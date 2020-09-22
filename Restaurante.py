# from Ingredientes import OpcionMenu,Ingrediente,Platillo,Bebida,Complemento

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
                print("No existe esta opcion")
            else:
                orden.agregar(opcionMenu)
                # print ("Se añadio {} a la Orden".format(opcionMenu)) 

        return orden

    def solicitarCuenta(self, mesero):
        total = mesero.entregarCuenta(self.mesaAsignada)
        print(self.pagarCuenta(mesero,total))

    def pagarCuenta(self, mesero, total):
        mesero.cobrarCuenta(total,self.mesaAsignada)
        return "Se pagaron {} de la cuenta".format(total)

class Orden:
    totalOpciones=0

    def __init__(self):
        self.opcionesMenu = []

    def cancelar(self):
        self.opcionesMenu = []
        return "Orden cancelada"

    def agregar(self,opcion):
        self.opcionesMenu.append(opcion)
        self.totalOpciones+=len(opcion.incluye)

    def ingresar(self):
        for opcion in self.opcionesMenu:
            for preparable in opcion.incluye:
                preparable.preparar()
                # preparable.preparar(self.egresar)


    def egresar(self):
        self.totalOpciones-=1
        if(self.totalOpciones==0):
            print('ha salido')



    def __str__(self):
        ordenStr=''
        if(len(self.opcionesMenu) == 0):
            return "Orden vacia"
        else:
            for opc in self.opcionesMenu:
                ordenStr+=f'{opc}'.replace('Se añadio Opcion incluye:', '-')
            return "Opciones de menu en la orden {}".format(ordenStr)


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

    def __str__(self):
        i=0
        string='\n\n'
        for opcion in self.lista:
            string+=f'[{i}] {opcion}\n'
            i+=1
        
        return string


   

# #Cliente
# cliente = Cliente()

# # Preparables

# #Datos de prueba
# salchicha = Ingrediente('Salchicha', 10)
# carne = Ingrediente('Carne', 10)
# lechuga = Ingrediente('Lechuga', 10)
# pan = Ingrediente('Pan', 1)
# limon = Ingrediente('Limon', 10)
# agua = Ingrediente('Agua', 10)
# papas = Ingrediente('Papas', 10)
# azucar = Ingrediente('Azucar', 10)

# hamburguesa = Platillo('Hamburguesa', [lechuga, carne, pan], 'Hamburguesa de carne')
# limonada = Bebida('Limonada', [agua, limon], 'Limonada natural')
# papas_comp = Complemento('Papas',[papas], 'Complemento de papas')

# combo_hamburguesa = OpcionMenu([hamburguesa, limonada, papas_comp], 33.5)
# combo_hamburguesa2 = OpcionMenu([hamburguesa, limonada,limonada, papas_comp], 43.5)


# #Resultados
# print(combo_hamburguesa)
# print(hamburguesa)
# print(hamburguesa.preparar())
# print(hamburguesa.preparar())
# pan.surtir(5)
# print(hamburguesa.preparar())
# print(pan)


# #Menu
# menu = Menu([combo_hamburguesa,combo_hamburguesa2,hamburguesa,limonada])



# print(cliente.ordenar(menu, [combo_hamburguesa]))
# print(cliente.ordenar(menu,[combo_hamburguesa2]))

