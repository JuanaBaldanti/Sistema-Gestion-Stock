import random

productosId = ["id0", "id1", "id2", "id3"]
productosNombre = ["Remera Algodón", "Pantalón Jean", "Consola PS5", "Auriculares BT"]
productosCategoria = ["Vestimenta", "Vestimenta", "Tecnología", "Tecnología"]
productosPrecio = [15.00, 45.00, 499.99, 75.50]
productosStock = [50, 30, 10, 40]
productosVendidos = [0, 0, 0, 0]
productosRecaudacion = [0, 0, 0, 0]

comprasId = []
comprasDni = []
comprasProductoId = []
comprasCantidad = []
comprasTotal = []
comprasMedioPago = []

clienteDni = []
clienteRecaudacion = []
clienteCompras = []

cuponesCodigo = ["6852", "4182", "2186", "5742"]
cuponesDescuento = [15, 25, 30, 40]

NomAdmin = ["Laura", "Erik", "Juana", "Bernardo"]
DniAdmin = ["46706091", "47435898","47496268", "60470761"]

def borrarElemento(lista, valor, listasParalelas = []):
    listaAux = []
    paralelasAux = []
    for list in listasParalelas:
        paralelasAux.append([])
    for i in range(len(lista)):
        if lista[i] != valor:
            listaAux.append(lista[i])
            for j in range(len(listasParalelas)):
                paralelasAux[j].append(listasParalelas[j][i])
    lista.clear()
    for list in listasParalelas:
        list.clear()
    for item in listaAux:
        lista.append(item)
    for i in range(len(listasParalelas)):
        for j in range(len(paralelasAux[i])):
            listasParalelas[i].append(paralelasAux[i][j])

def busquedaBinaria(lista, valor, obtenerPosicion = False):
    inicio = 0
    fin = len(lista) - 1
    encontrado = False
    posicion = 0
    while inicio <= fin and not encontrado:
        medio = (inicio + fin) // 2 # posición central
        if lista[medio] == valor:
            encontrado = True
            posicion = medio
        elif valor < lista[medio]:
            fin = medio - 1 # buscar en la mitad izquierda
        else:
            inicio = medio + 1 # buscar en la mitad derecha
    if encontrado and obtenerPosicion:
        return posicion
    elif encontrado:
        return True
    else:
        return False
    
def verificarID():
    ID = 0
    nom = input("Ingrese su nombre: ")
    dniValido = False
    while not dniValido:
        dni = input("Ingrese su DNI: ")
        if validarDNI(dni):
            dniValido = True
        else:
            print("================================================================")
            print("❌ DNI inválido")
            print("================================================================")
    for i in range (len(NomAdmin)):
        if nom == NomAdmin[i]:
            ID = ID+1
    if busquedaBinaria(DniAdmin, dni):
        ID = ID+1
    admin = False
    if ID == 2:
        admin = True
    return mostrarMenu(admin, dni)
    
def esNumero(texto):
    numeros = "0123456789"
    largo = len(texto)
    primerDigito = True
    if largo == 0 or largo == 1 and texto[0] not in numeros:
        return False
    for caracter in texto:
        if caracter not in numeros:
            if caracter != "-" or caracter == "-" and not primerDigito:
                return False
        primerDigito = False
    return True

def validarDNI(dni):
    if esNumero(dni) and len(dni) == 8 and int(dni) > 0:
        return True
    else:
        return False
    
def copiarLista(lista):
    copia = []
    for elemento in lista:
        copia.append(elemento)
    return copia

def ordenamientoSeleccion(lista, mayor_a_menor = False, listasParalelas = []):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if mayor_a_menor:
                if lista[i] < lista[j]:
                    if len(listasParalelas) > 0:
                        for listaParalela in listasParalelas:
                            aux = listaParalela[i]
                            listaParalela[i] = listaParalela[j]
                            listaParalela[j] = aux
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if lista[i] > lista[j]:
                    if len(listasParalelas) > 0:
                        for listaParalela in listasParalelas:
                            aux = listaParalela[i]
                            listaParalela[i] = listaParalela[j]
                            listaParalela[j] = aux
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def calcularPorcentajes(lista):
    total = 0
    porcentajes = []
    for valor in lista:
        total += valor
    for valor in lista:
        if valor == 0:
            porcentajes.append(0)
        else:
            porcentajes.append((valor / total) * 100)
    return porcentajes

def registrarCompra(dni, productoId, cantidad, medioPago, total):
    nuevoId = len(comprasId) + 1
    comprasId.append(nuevoId)
    comprasDni.append(int(dni))
    comprasProductoId.append(productoId)
    comprasCantidad.append(cantidad)
    comprasTotal.append(total)
    comprasMedioPago.append(medioPago)
    dniNum = int(dni)
    clienteExiste = False
    i = 0
    while i < len(clienteDni) and not clienteExiste:
        if clienteDni[i] == dniNum:
            clienteRecaudacion[i] = clienteRecaudacion[i] + total
            clienteCompras[i] = clienteCompras[i] + 1
            clienteExiste = True
        i = i + 1
    if not clienteExiste:
        clienteDni.append(dniNum)
        clienteRecaudacion.append(total)
        clienteCompras.append(1)
    i = 0
    productoEncontrado = False
    while i < len(productosId) and not productoEncontrado:
        if productosId[i] == productoId:
            productosStock[i] = productosStock[i] - cantidad
            productosVendidos[i] = productosVendidos[i] + cantidad
            productosRecaudacion[i] = productosRecaudacion[i] + total
            productoEncontrado = True
        i = i + 1

def gestionarStock(producto):
    print("================================================================")
    print(f"-----AJUSTANDO STOCK {productosNombre[producto]} ({productosStock[producto]})-------")
    seleccion = input("Ingrese un número positivo para sumar stock y uno negativo para restar: ")
    if esNumero(seleccion):
        ajusteStock = int(seleccion)
        nuevoStock = productosStock[producto] + ajusteStock
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return gestionarStock(producto)
    if nuevoStock < 0:
        print("⛝       Cambio no realizado       ⛝ ")
        print("================================================================")
        print("X---X---X---EL STOCK DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarStock(producto)
    else:
        productosStock[producto]=nuevoStock
        print("================================================================")
        print(f"Nuevo Stock de {productosNombre[producto]} | Stock actualizado: {productosStock[producto]}")
        print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()
    
def gestionarPrecio(producto):
    print("================================================================")
    print(f"-----AJUSTANDO PRECIO {productosNombre[producto]} (${productosPrecio[producto]})-------")
    seleccion = input("Ingrese el nuevo precio del producto: $")
    if esNumero(seleccion):
        ajustePrecio = int(seleccion)
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return gestionarPrecio(producto)
    if ajustePrecio<=0:
        print("================================================================")
        print("X---X---X---EL PRECIO DEL PRODUCTO NO PUEDE SER NEGATIVO---X---X---X")
        print("⛝       Cambio no realizado       ⛝ ")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarPrecio(producto)
    else:    
        productosPrecio[producto]=ajustePrecio
        print("================================================================")
        print(f"Nuevo Precio de {productosNombre[producto]} | Precio actualizado: ${productosPrecio[producto]}")
        print("☑    CAMBIO REALIZADO CORRECTAMENTE    ☑")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()
    
def verCupones():
    print("================================================================")
    print("- - - - - CUPONES ACTUALES - - - - -")
    if len(cuponesCodigo) == 0:
        print("No hay cupones disponibles.")
    else:
        for i in range(len(cuponesCodigo)):
            print(f"{cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")
    print("================================================================")
    input("Presione Enter para continuar...")
    return gestionarCupones()

def borrarCupon():
    print("================================================================")
    print("- - - - - BORRAR CUPÓN - - - - -")
    if len(cuponesCodigo) == 0:
        print("No hay cupones disponibles.")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarCupones()
    else:
        print("[0] Volver")
        for i in range(len(cuponesCodigo)):
            print(f"[{i+1}] {cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")
        borrarSel = input("Seleccione un cupón para borrar: ")
        
        if esNumero(borrarSel):
            borrarNum = int(borrarSel)
        else:
            print("================================================================")
            print("❌ Ingrese un número")
            return borrarCupon()
        if borrarNum == "0":
            return gestionarCupones()
        elif borrarNum <= len(cuponesCodigo) and borrarNum > -1:
            x=borrarNum-1
            print("------------------------------------------------------------")
            print(f"❌ Estas seguro que deseas eliminar el cupón: {cuponesCodigo[x]} {cuponesDescuento[x]}% descuento ❌❗❗")
            opp=input("====> S/N: ")
            if opp == "s" or opp == "S":
                borrarElemento(cuponesCodigo, cuponesCodigo[x], [cuponesDescuento])
                print("============================================================")
                print("==================❌ CUPÓN ELIMINADO ❌==================")
                return gestionarCupones()
            else:
                print("===============================================")
                print("❌ ❌ ❌ Operacion cancelada ❌ ❌ ❌")
                return gestionarCupones()
        else:
            print("================================================================")
            print("❌ Ingrese una opción válida")
            return borrarCupon()

def modificarCupon():
    print("================================================================")
    print("- - - - - MODIFICAR CUPÓN - - - - -")
    if len(cuponesCodigo) == 0:
        print("No hay cupones disponibles.")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarCupones()
    else:
        print("[0] Volver")
        for i in range(len(cuponesCodigo)):
            print(f"[{i+1}] {cuponesCodigo[i]} ({cuponesDescuento[i]}% descuento)")
        modificarSel = input("Seleccione un cupón para modificar: ")
        if esNumero(modificarSel):
            modificarNum = int(modificarSel)
        else:
            print("================================================================")
            print("❌ Ingrese un número")
            return modificarCupon()
        if modificarNum == "0":
            return gestionarCupones()
        elif modificarNum <= len(cuponesCodigo) and modificarNum > -1:
            modificarNum=int(modificarNum)
            ModC=modificarNum-1
            print(f"- - - - -Modificando Cupon: {cuponesCodigo[ModC]} {cuponesDescuento[ModC]}% descuento- - - - -")
            print()
            NewC=input("Ingrese el nuevo codigo del cupón: ")
            NewD=input("Ingrese el nuevo descuento del cupón: ")
            cuponesCodigo[ModC]=NewC
            cuponesDescuento[ModC]=NewD
            print("= = = = =Cupón modificado correctamente= = = = =")
            print(f"Cupon modificado: Codigo={cuponesCodigo[ModC]} Descuento={cuponesDescuento[ModC]}%")
            gestionarCupones()
        else:
            print("================================================================")
            print("❌ Ingrese una opción válida")
            modificarCupon()

def agregarCupon():
    print("================================================================")
    print("- - - - - AGREGAR CUPÓN - - - - -")
    print("Ingrese 0 para cancelar ingreso")
    codigo = input("Ingrese el código del cupón (4 dígitos): ")

    if codigo == "0":
        return gestionarCupones()
    elif codigo in cuponesCodigo:
        print("================================================================")
        print("❌ Cupón ya existe")
        return agregarCupon()
    elif len(codigo) < 4 or len(codigo) > 4:
        print("================================================================")
        print("❌ Código debe ser de 4 dígitos")
        return agregarCupon()
    else:
        descuento = 0
        while descuento <= 0 or descuento > 100:
            descInput = input("Descuento (1-100): ")
            if esNumero(descInput):
                descuento = int(descInput)
                if descuento <= 0 or descuento > 100:
                    print("================================================================")
                    print("❌ Descuento debe estar entre 1 y 100")
                    return agregarCupon()
            else:
                print("================================================================")
                print("❌ Ingrese un número válido")
                return agregarCupon()
        cuponesCodigo.append(codigo)
        cuponesDescuento.append(descuento)
        print("================================================================")
        print("✅ Cupón agregado")
        return gestionarCupones()

def Comprar(admin, ID):
    print("================================================================")
    print("- - - - - 💸 COMPRA 💸 - - - - -")
    if len(productosNombre) > 0:
        random_index = random.randint(0, len(productosNombre) - 1)
        print("================================================================")
        print(f"💡 Producto recomendado de hoy: {productosNombre[random_index]} — ${productosPrecio[random_index]} ({productosStock[random_index]} en stock)")
    if admin:
        print("================================================================")
        print("Ingrese 0 para volver al menu")
        dni = input("Ingrese su DNI: ")
    else:
        dni = ID
    if dni == "0":
        return
    elif validarDNI(dni):
        medioPago = ""
        pagoSeleccionado = False
        while not pagoSeleccionado:
            print("================================================================")
            print("- - - - - MEDIO DE PAGO - - - - -")
            print("[0] Volver")
            print("[1] Efectivo")
            print("[2] Tarjeta")
            medio = input("Medio de pago: ")
            if medio == "0":
                if admin:
                    return Comprar()
                else:
                    return
            elif medio == "1":
                medioPago = "Efectivo"
                pagoSeleccionado = True
            elif medio == "2":
                medioPago = "Tarjeta"
                pagoSeleccionado = True
            else:
                print("================================================================")
                print("❌ Opción inválida")
        prodValido = False
        prodInput = ""
        productoIndice = ""
        while not prodValido:
            print("================================================================")
            print("- - - - - PRODUCTOS DISPONIBLES - - - - -")
            for i in range(len(productosNombre)):
                print(f"[{i}] {productosNombre[i]} - ${productosPrecio[i]}")
            prodInput = input("Seleccione producto (número): ")
            if esNumero(prodInput):
                productoIndice = int(prodInput)
            if esNumero(prodInput) and productoIndice >= 0 and productoIndice < len(productosNombre):
                if productosStock[productoIndice] > 0:
                    prodValido = True
                else:
                    print("================================================================")
                    print("❌ Sin stock")
            else:
                print("================================================================")
                print("❌ Producto no válido")
        cantidadValida = False
        cantidad = ""
        while not cantidadValida:
            print("================================================================")
            print(f"- - - - - CANTIDAD DE PRODUCTO - - - - -")
            cantInput = input(f"Cantidad de {productosNombre[productoIndice]}: ")
            if esNumero(cantInput):
                cantidad = int(cantInput)
            if esNumero(cantInput) and cantidad > 0 and cantidad <= productosStock[productoIndice]:
                cantidadValida = True
            else:
                print("================================================================")
                print(f"❌ Cantidad inválida. Max: {productosStock[productoIndice]}")
        subtotal = productosPrecio[productoIndice] * cantidad
        subtotal = int(subtotal)
        descuento = 0
        cuponElegido = False
        while not cuponElegido:
            print("================================================================")
            print(f"- - - - - CUPÓN - - - - -")
            usarCupon = input("¿Usar cupón? (S/N): ")
            if usarCupon == "S" or usarCupon == "s":
                ingresandoCupon = True
                while ingresandoCupon:
                    print("Ingrese 0 para cancelar ingreso de cupón")
                    codigo = input("Código del cupón: ")
                    print("================================================================")
                    if codigo == "0":
                        ingresandoCupon = False
                    else:
                        for i in range(len(cuponesCodigo)):
                            if codigo == cuponesCodigo[i]:
                                descuento = int(cuponesDescuento[i])
                                print(f"Cupón aplicado: {descuento}% descuento")
                                ingresandoCupon = False
                        if ingresandoCupon:
                            print("Cupón inválido")     
                cuponElegido = True
            elif usarCupon == "N" or usarCupon== "n":
                cuponElegido = True
            else:
                print("================================================================")
                print("❌ Opción inválida")
        total = subtotal * (100 - descuento) / 100
        print("================================================================")
        print(f"- - - - - CONFIRMACIÓN DE COMPRA - - - - -")
        print(f"Resumen: {productosNombre[productoIndice]} x{cantidad}")
        print(f"Subtotal: ${subtotal}")
        if descuento > 0:
            print(f"Descuento: {descuento}%")
        print(f"Total: ${total}")
        confirmar = input("Confirmar compra (S/N): ")
        if confirmar == "S" or confirmar == "s":
            registrarCompra(dni, productosId[productoIndice], cantidad, medioPago, total)
            print("================================================================")
            print("✅ Compra realizada")
        else:
            print("================================================================")
            print("Compra cancelada")
    else:
        print("================================================================")
        print("❌ DNI inválido")
        return Comprar()
    print("================================================================")
    input("Presione Enter para continuar...")

def verEstadisticas():
    print("================================================================")
    print("- - - - - 📈 ESTADÍSTICAS DE VENTAS 📊 - - - - -")
    print("[0] Volver")
    print("[1] Facturación total")
    print("[2] Facturación por producto")
    print("[3] Facturación por categoría")
    print("[4] Cliente con mayor compra")
    opcionNum = input("Seleccione una opción: ")
    if opcionNum == "0":
        return
    print("================================================================")
    if opcionNum == "1":
        dineroTotal = 0
        for producto in productosRecaudacion:
            dineroTotal += producto
        print(f"Facturación total: ${dineroTotal}")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "2":
        print("Facturación total por producto (Ordenado por Facturación):")
        recaudacionOrdenado = copiarLista(productosRecaudacion)
        idOrdenado = copiarLista(productosId)
        nombreOrdenado = copiarLista(productosNombre)
        ordenamientoSeleccion(recaudacionOrdenado,True,[idOrdenado,nombreOrdenado])
        recaudacionOrdenadoPorcent = calcularPorcentajes(recaudacionOrdenado)
        for i in range(len(productosId)):
            print(f"- {nombreOrdenado[i]} ({idOrdenado[i]}): ${recaudacionOrdenado[i]} ({recaudacionOrdenadoPorcent[i]}%)")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "3":
        print("Facturación total por categoría:")
        categorias = []
        facturacionCategoria = []
        for i in range(len(productosCategoria)):
            categoria = productosCategoria[i]
            recaudacion = productosRecaudacion[i]
            encontrado = False
            for j in range(len(categorias)):
                if categorias[j] == categoria:
                    facturacionCategoria[j] += recaudacion
                    encontrado = True
            if not encontrado:
                categorias.append(categoria)
                facturacionCategoria.append(recaudacion)
        recaudacionOrdenado = copiarLista(facturacionCategoria)
        categoriasOrdenado = copiarLista(categorias)
        ordenamientoSeleccion(recaudacionOrdenado, True, [categoriasOrdenado])
        recaudacionOrdenadoPorcent = calcularPorcentajes(recaudacionOrdenado)
        for i in range(len(categoriasOrdenado)):
            print(f"- {categoriasOrdenado[i]}: ${recaudacionOrdenado[i]} ({recaudacionOrdenadoPorcent[i]}%)")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    elif opcionNum == "4":
        if len(comprasDni) == 0:
            print("No hay clientes registrados")
            print("================================================================")
            input("Presione Enter para continuar...")
            return verEstadisticas()
        dniCompraMax = comprasDni[0]
        cantCompraMax = comprasTotal[0]
        for i in range(len(comprasId)):
            if comprasTotal[i] > cantCompraMax:
                cantCompraMax = comprasTotal[i]
                dniCompraMax = comprasDni[i]
        print("Cliente con la compra más alta:")
        print(f"- DNI: {dniCompraMax}")
        for i in range(len(comprasId)):
            if comprasDni[i] == dniCompraMax:
                print(f"- Producto: {comprasProductoId[i]} | Cantidad comprado: {comprasCantidad[i]} | Total Facturado: ${comprasTotal[i]} | Tipo de Pago: {comprasMedioPago[i]}")
        print("================================================================")
        input("Presione Enter para continuar...")
        return verEstadisticas()
    else:
        print("❌ Opción inválida")
        return verEstadisticas()

def verEstadisticaProducto():
    print("================================================================")
    print("- - - - - 📈 ESTADÍSTICAS POR PRODUCTO 📊 - - - - -")
    print("[0] Volver")
    for i in range(len(productosId)):
        print(f"[{i+1}] {productosNombre[i]} ({productosId[i]})")
    productoSel = input("Seleccione un producto: ")
    if esNumero(productoSel):
        productoNum = int(productoSel)-1
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return verEstadisticaProducto()
    if productoNum == (-1):
        return
    elif productoNum < (-1) or productoNum >= len(productosId):
        print("================================================================")
        print("❌ Opción inválida")
        return verEstadisticaProducto()
    print("================================================================")
    print(f"- - - - - ESTADÍSTICAS PARA {productosNombre[productoNum]} - - - - -")
    print(f"Facturación total: ${productosRecaudacion[productoNum]}")
    print(f"Cantidad de compras: {productosVendidos[productoNum]}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaProducto()

def verEstadisticaCategoria():
    print("================================================================")
    print("- - - - - 🗂️ ESTADÍSTICAS POR CATEGORÍA 🗂️ - - - - -")
    print("[0] Volver")
    categoriasUnicas = []
    for categoria in productosCategoria:
        if categoria not in categoriasUnicas:
            categoriasUnicas.append(categoria)
    for i in range(len(categoriasUnicas)):
        print(f"[{i+1}] {categoriasUnicas[i]}")
    categoriaSel = input("Seleccione una categoría: ")
    if esNumero(categoriaSel):
        categoriaNum = int(categoriaSel)-1
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return verEstadisticaCategoria()
    if categoriaNum == (-1):
        return
    elif categoriaNum < (-1) or categoriaNum >= len(categoriasUnicas):
        print("================================================================")
        print("❌ Opción inválida")
        return verEstadisticaCategoria()
    print("================================================================")
    categoriaSeleccionada = categoriasUnicas[categoriaNum]
    totalRecaudacion = 0
    totalVendidos = 0
    for i in range(len(productosId)):
        if productosCategoria[i] == categoriaSeleccionada:
            totalRecaudacion += productosRecaudacion[i]
            totalVendidos += productosVendidos[i]
    print(f"- - - - - ESTADÍSTICAS PARA {categoriaSeleccionada} - - - - -")
    print(f"Facturación total: ${totalRecaudacion}")
    print(f"Cantidad total de productos vendidos: {totalVendidos}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaCategoria()
    
def verEstadisticaCliente():
    print("================================================================")
    print("- - - - - 📈 VENTAS POR CLIENTE 📊 - - - - -")
    if len(comprasDni) == 0:
        print("No hay clientes registrados")
        print("================================================================")
        input("Presione Enter para continuar...")
        return
    print("[0] Volver")
    for i in range(len(clienteDni)):
        print(f"[{i+1}] {clienteDni[i]}")
    clienteSel = input("Seleccione un cliente: ")
    if esNumero(clienteSel):
        clienteNum = int(clienteSel)-1
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return verEstadisticaCliente()
    if clienteNum == (-1):
        return
    elif clienteNum < (-1) or clienteNum >= len(clienteDni):
        print("================================================================")
        print("❌ Opción inválida")
        return verEstadisticaCliente()
    dniSelect = clienteDni[clienteNum]
    print("================================================================")
    print(f"- - - - - Cliente ({dniSelect}) - - - - -")
    print(f"Pagos totales: ${clienteRecaudacion[clienteNum]}")
    print(f"Cantidad de compras: {clienteCompras[clienteNum]}")
    print("\nProductos comprados:")
    for i in range(len(comprasId)):
        if comprasDni[i] == dniSelect:
            print(f"- Producto: {comprasProductoId[i]} | Cantidad comprado: {comprasCantidad[i]} | Total Facturado: ${comprasTotal[i]} | Tipo de Pago: {comprasMedioPago[i]}")
    print("================================================================")
    input("Presione Enter para continuar...")
    return verEstadisticaCliente()

def gestionarProductos():
    print("================================================================")
    print("--- GESTIÓN DE INVENTARIO Y PRECIOS ---")
    print("[0] Volver")
    for i in range(len(productosNombre)):
        print(f"[{i+1}] {productosNombre[i]} ({productosId[i]}) | Precio: ${productosPrecio[i]} | Stock: {productosStock[i]}")
    seleccion = input("Seleccione el producto a modificar: ")
    if esNumero(seleccion):
        opcion = int(seleccion)
    else:
        print("================================================================")
        print("❌ Ingrese un número")
        return gestionarProductos()
    if opcion == 0:
        return
    elif opcion < 0 or opcion >= len(productosNombre):
        print("================================================================")
        print("❌ Opción inválida")
        return gestionarProductos()
    opcion = opcion-1
    print("================================================================")
    print( f"Edición del producto: {productosNombre[opcion]} | Stock: {productosStock[opcion]} | Precio: {productosPrecio[opcion]}")
    print("[0] Volver")
    print("[1] Modificar Stock")
    print("[2] Modificar Precio")
    ajuste = input("Ingrese el ajuste deseado: ")
    if ajuste == "0":
        return gestionarProductos()
    elif ajuste == "1":
        gestionarStock(opcion)
    elif ajuste == "2":
        gestionarPrecio(opcion)
    else:
        print("================================================================")
        print("⛝ OPCION NO VALIDA ⛝")
        print("================================================================")
        input("Presione Enter para continuar...")
        return gestionarProductos()

def gestionarCupones():
    print("================================================================")
    print("- - - - - 🎟️ GESTIÓN DE CUPONES 🎟️ - - - - -")
    print("[0] Volver")
    print("[1] Ver cupones")
    print("[2] Borrar cupón")
    print("[3] Modificar cupón")
    print("[4] Agregar cupón")
    opcionNum = input("Seleccione una opción: ")
    if opcionNum == "0":
        return
    elif opcionNum == "1":
        verCupones()
    elif opcionNum == "2":
        borrarCupon()
    elif opcionNum == "3":
        modificarCupon()
    elif opcionNum == "4":
        agregarCupon()
    else:
        print("================================================================")
        print("❌ Opción no válida")
        return gestionarCupones()

def salir():
    """Función para salir del programa con confirmación del usuario"""
    print("================================================================")
    print("- - - - -❌ Salir ❌- - - - -")
    print("¿Está seguro que quiere salir (S/N)?: ", end="")
    confirmacion = input()
    if confirmacion == 'S' or confirmacion == 'SI' or confirmacion == 's' or confirmacion == 'S':
        print("\n================================================================")
        print("Exit⦿")
        print("¡Gracias por visitar nuestra tienda! 👋")
        print("================================================================")
        return True
    else:
        print("\n✅ Regresando al menú principal...")
        input("Presione Enter para continuar...")
        return False

def mostrarMenu(admin, ID):
    """Función que muestra el menú principal y gestiona la navegación"""
    seguirPrograma = True
    while seguirPrograma:
        if admin:
            print("=======================================================================")
            print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
            print("=======================================================================")
            print("Bienvenido a la tienda virtual 🏪 ADMIN", ID)
            print("[1] Comprar 💲")
            print("[2] Ver estadísticas totales 📈")
            print("[3] Ver estadísticas por producto 📊")
            print("[4] Ver estadísticas por categoría 🗂️")
            print("[5] Ver estadísticas por cliente 🙋")
            print("[6] Gestionar Productos 📦")
            print("[7] Gestionar Cupones 🎟️")
            print("[8] Log Out 😞")
            print("[9] Salir ❌")
            opcion = input("Seleccione opción: ")
            if opcion == "1":
                Comprar(admin, ID)
            elif opcion == "2":
                verEstadisticas()
            elif opcion == "3":
                verEstadisticaProducto()
            elif opcion == "4":
                verEstadisticaCategoria()
            elif opcion == "5":
                verEstadisticaCliente()
            elif opcion == "6":
                gestionarProductos()
            elif opcion == "7":
                gestionarCupones()
            elif opcion == "8":
                if salir():
                    return verificarID()
            elif opcion == "9":
                if salir():
                    seguirPrograma = False
            else:
                print("================================================================")
                print("❌ Opción inválida. Por favor, seleccione una opción del 1 al 8.")
                print("================================================================")
                input("Presione Enter para continuar...")         
        else:
            print("=======================================================================")
            print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
            print("=======================================================================")
            print("Bienvenido a la tienda virtual 🏪", ID)
            print("[1] Comprar 💲")
            print("[2] Log Out 😞")
            print("[3] Salir ❌")
            opcion = input("Seleccione opción: ")
            if opcion == "1":
                Comprar(admin, ID)
            elif opcion == "2":
                if salir():
                    return verificarID()
            elif opcion == "3":
                if salir():
                    seguirPrograma = False
            else:
                print("================================================================")
                print("❌ Opción inválida. Por favor, seleccione una opción del 1 al 8.")
                print("================================================================")
                input("Presione Enter para continuar...")
            
print("Iniciando E-Commerce...")
verificarID() 
