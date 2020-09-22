from Ingredientes import OpcionMenu,Ingrediente,Platillo,Bebida,Complemento
from Restaurante import Cliente,Orden,Menu
from Mesa import Mesa,Mesero,Cuenta






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

simple_guesa = OpcionMenu([hamburguesa, limonada], 28.5)
combo_hamburguesa = OpcionMenu([hamburguesa, papas_comp], 28.5)
combo_hamburguesa2 = OpcionMenu([hamburguesa, limonada, papas_comp], 33.5)
combo_hamburguesa3 = OpcionMenu([hamburguesa,hamburguesa, limonada,limonada, papas_comp], 63.5)


#Resultados
print(combo_hamburguesa)
print(hamburguesa)
print(hamburguesa.preparar())
print(hamburguesa.preparar())
pan.surtir(5)
print(hamburguesa.preparar())
print(pan)


#Menu
menu = Menu([simple_guesa,combo_hamburguesa,combo_hamburguesa2,combo_hamburguesa3])



print(cliente.ordenar(menu, [combo_hamburguesa]))
print(cliente.ordenar(menu,[combo_hamburguesa2]))



# crear mesas
mesa1=Mesa(1,3)
mesa2=Mesa(2,10)
mesa3=Mesa(3,6)
mesa4=Mesa(4,5)
mesa5=Mesa(2,2)

# crear meseros
meseroRoberto = Mesero('Roberto',menu)
meseroRoberto.asignarMesas([mesa1,mesa2])
meseroLuis = Mesero('Luis',menu)
meseroRoberto.asignarMesas([mesa4,mesa3,mesa5])

clientes=[]
for i in range(0,mesa1.lugares):
    clientes.append(Cliente())

mesa1.sentarClientes(clientes)

meseroRoberto.tomarOrden(mesa1)


clientes[0].solicitarCuenta(meseroRoberto)



