# from Ingredientes import OpcionMenu,Ingrediente,Platillo,Bebida,Complemento
# from Restaurante import Cliente,Orden,Menu

import random


class Mesa():
    cuenta = None

    def __init__(self, mesa, lugares, mesero="", clientes=[]):
        self.mesa = mesa
        self.clientes = clientes
        self.mesero = mesero
        self.lugares = lugares

    def agregarCuenta(self, orden):
        self.cuenta.agregarOrden(orden)

    def crearCuenta(self, numeroCuenta):
        self.cuenta = Cuenta(numeroCuenta)

    def cerrarCuenta(self,numeroCuenta):
        self.cuenta.status = 'cerrada'
        print(f'la cuenta {self.cuenta} se cerró')
        self.cuenta = None

    def sentarClientes(self, clientes):
        i = 0
        for cliente in clientes:
            if(i < self.lugares):
                cliente.mesaAsignada = self
                self.clientes.append(cliente)
                i += 1

    def desalojar(self):
        self.cleintes = []

    def asignarMesero(self, mesero):
        self.mesero = mesero


class Mesero():
    def __init__(self, nombre, menu, mesas=[]):
        self.nombre = nombre
        self._menu = menu
        self.mesas = mesas

    def tomarOrden(self, mesa):
        mesa.crearCuenta(random.randint(1001, 9999))
        print(self._menu)
        for cliente in mesa.clientes:
            inSel = inSel = list(map(int, input(
                'Porfavor eliga con numeros separados por comas lo que desea ordenar:').replace(" ", "").split(',')))
            seleccion = []
            for sel in inSel:
                seleccion.append(self._menu.lista[sel])
            mesa.cuenta.agregarOrden(cliente.ordenar(self._menu, seleccion))

        print(f'Se tomo la orden de la mesa {mesa.mesa}\n ')


    def asignarMesas(self, mesas):
        for mesa in mesas:
            self.mesas.append(mesa)

    def entregarOrden(self, orden):
        pass

    def entregarCuenta(self, mesa):
        return mesa.cuenta.total()

    def cobrarCuenta(self, total, mesa):
        mesa.cerrarCuenta(mesa.cuenta.numeroCuenta)
        return "Se cobraron {} de la cuenta".format(
            total
        )


class Cuenta():

    status = "abierto"

    def __init__(self, numeroCuenta):
        self.numeroCuenta = numeroCuenta
        self.ordenes = []

    def total(self):
        total = 0
        for orden in self.ordenes:
            for opcion in orden.opcionesMenu:
                total += opcion.precio
        return total

    def agregarOrden(self, pedido):
        self.ordenes.append(pedido)
        for order in self.ordenes:
            order.ingresar()

    def __str__ (self):
        return f'con numero {self.numeroCuenta}'
