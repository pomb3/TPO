# Seleccionar producto()
# Generar cliente()
# Cobrar()
# cajas()
# descuentos()
# Menú()
# Socios()
import random
import productosCobro
def generarCliente():
    cliente = []
    i=1
    for i in range(random.randint(1,5)): #Cantidad de productos del cliente
        cliente.append(random.randint(0, 5))
    return cliente

def caja(cliente, descuento):
    productos=[]
    precioTotal = 0
    i=1
    for i in range(len(cliente)):
        producto, precio = productosCobro.productoSelec(cliente[i])
        productos.append(producto)
        precioTotal += precio
        print(f'{productos[i]}: ${precio}')
    B500, B100, B20, B5 = productosCobro.cobro(precioTotal)
    print(f'\nBilletes de $500: {B500}\nBilletes de $100: {B100}\nBilletes de $20: {B20}\nBilletes de $5: {B5}\n')
    print(f'\nTotal sin descuento: {precioTotal}')
    print(f'Descuento: {100-(100*descuento)}%')
    precioTotal *= descuento
    print(f'Precio final: {precioTotal}')
    print(f'\nLos productos seleccionados son: {productos}')
    return productos, precioTotal


def main():
    while True:
        try:
            opcion = int(input('\n---Menú Principal---\n1. Generar cliente\n2. Cerrar menú\nElige una opcion: '))
            if opcion == 1:
                cliente = generarCliente()
                descuento = int(input('\n1. Sin descuento\n2. 10% de descuento\n3. 35% de descuento\n4. 5% de descuento\nIngrese el número correspondiente de descuento: '))
                caja(cliente, productosCobro.descuentos(descuento))
                
            elif opcion == 2:
                print('Cerrando caja')
                break
        except ValueError:
            print('Error. Ingrese un número')

main()