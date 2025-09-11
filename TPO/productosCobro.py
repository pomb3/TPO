def productoSelec(elección):
    producto =[
        ['Manzana','Televisor','Zapatillas','Cubiertos','Desodorante','Espejo'],
        [5,			1000, 			100, 		75,			50,			200    ]]
    articulo, precio = producto[0][elección], producto[1][elección]
    return articulo, precio
def cobro(precio):
    pagado, total = 0, precio
    B500, B100, B20, B5 = 0, 0, 0, 0 # Billetes disponibles
    while pagado < precio:
        while total >= 500:
            pagado +=500
            total -=500
            B500+=1
        while total >= 100:
            pagado +=100
            total -=100
            B100+=1
        while total >= 20:
            pagado+=20
            total-=20
            B20+=1
        while total >= 5:
            pagado +=5
            total-=5
            B5+=1
    if pagado >= precio:
        return B500, B100, B20, B5


def descuentos(eleccion):
# nocliente 1  / cliente 2 / jubilado 3 / cupon 4 
# martes 2 / miercoles 3 / jueves 4
    descuento = 1.0
    if eleccion == 2:
        descuento = 0.9
    if eleccion == 3:
        descuento = 0.65
    if eleccion == 4:
        descuento = 0.95
    return descuento