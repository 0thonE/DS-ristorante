from abc import  ABC

class OpcionMenu:
    def __init__(self, preparables, precio):
        self.incluye = preparables
        self.precio = precio

    def __str__(self):
        incluyeStr = ''
        for x in self.incluye:
            incluyeStr += x.nombre + ', '
        incluyeStr = incluyeStr[:-2]
        return 'Opcion incluye: {} a un precio de {}'.format(incluyeStr, self.precio)


class Preparable(ABC): #Interfaz
    def __init__(self, nombre, ingredientes, descripcion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.descripcion = descripcion
        pass

    def preparar(self):
        for x in self.ingredientes:
            x.usar(1)
        return 'Preparando {}...'.format(self.nombre)

    def __str__(self):
        incluyeStr = ''
        for x in self.ingredientes:
            incluyeStr += x.nombre + ', '
        incluyeStr = incluyeStr[:-2]
        return '{} incluye: {} '.format(self. nombre, incluyeStr) 


class Platillo(Preparable):
    def preparar(self):
        return 'Platillo - {}...'.format(super.preparar())


class Bebida(Preparable):
    def preparar(self):
        return 'Bebida - {}...'.format(super.preparar())


class Complemento(Preparable):
    def preparar(self):
        return 'Complemento - {}...'.format(super.preparar())


class Ingrediente:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
        pass

    def surtir(self, n):
        self.stock = self.stock + n
        pass

    def usar(self, n):
        self.stock = self.stock - n
        pass

    def __str__(self):
        return '{} tiene un stock de {}'.format(self.nombre, self.stock)


#Datos de prueba
salchicha = Ingrediente('Salchicha', 10)
carne = Ingrediente('Carne', 10)
lechuga = Ingrediente('Lechuga', 10)
pan = Ingrediente('Pan', 10)
limon = Ingrediente('Limon', 10)
agua = Ingrediente('Agua', 10)
papas = Ingrediente('Papas', 10)
azucar = Ingrediente('Azucar', 10)

hamburguesa = Platillo('Hamburguesa', [lechuga, carne, pan], 'Hamburguesa de carne')
limonada = Bebida('Limonada', [agua, limon], 'Limonada natural')
papas_comp = Complemento('Papas',[papas], 'Complemento de papas')

combo_hamburguesa = OpcionMenu([hamburguesa, limonada, papas_comp], 33.5)


#Resultados
print(combo_hamburguesa)
print(hamburguesa)
print(hamburguesa.preparar())
print(pan)