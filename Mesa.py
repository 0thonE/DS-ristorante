class Mesa():

    def __init__(self, mesa, clientes, mesero, lugares):
        self.mesa = mesa
        self.clientes = clientes
        self.mesero = mesero
        self.lugares = lugares

    def agregarAcuenta(self):
        pass

    def crearCuenta(self, numeroCuenta):
        self.cuenta = Cuenta(numeroCuenta)
        
    def cerrarCuenta(self):
        pass

class Mesero():
    def __init__(self, nombre, mesas):
        self.nombre = nombre
        self.mesas = []

    def tomarOrden(self, pedido):
        pedido = Cliente.ordenar.opcionMenu
        return "Se tomo la orden de {}".format(
            pedido
        )

    def entregarOrden(self, orden):
        pass

    def entregarCuenta(self):
        cliente.solicitarCuenta(nombre)
        
    def cobrarCuenta(self, total):
        Mesa.cerrarCuenta
        return "Se cobraron {} de la cuenta".format(
            total
        )

class Cuenta():

    status = "abierto"

    def __init__(self, numeroCuenta):
        self.numeroCuenta = numeroCuenta
        self.ordenes = []

    def total(self):
        pass

    def agregarOrden(self, pedido):
        pedido = Cliente.ordenar.orden
