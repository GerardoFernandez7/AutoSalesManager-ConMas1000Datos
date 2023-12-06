# Gerardo Andre Fernandez Cruz      Carne 23763
# Este programa se encarga de llevar un control de las ventas de un dueño de varias tiendas de autos en el cual podras ver y agregar informacion
# Al igual que ver ciertos reportes y graficas

# Importar modulos
import pandas as pd
import Func_Ev2 as ev2

# Declarar variables
df = pd.read_csv('ventas_autos.csv')
seguir_en_programa = True

# Programa principal
while seguir_en_programa == True: 
    print("") 
    print("### BIENVENIDO ###") 
    print("Que desea hacer?") 
    print("1. Agregar una nueva venta") 
    print("2. Ver listado de las marcas con autos vendidos") 
    print("3. Ver listado de los clientes que no han pagado su totalidad ") 
    print("4. Ver el top 10 de los mejores vendedores con mayor monto de comisiones ") 
    print("5. Ver las 10 marcas con mayor precio de venta, mostrando la marca, el modelo y el año") 
    print("6. Graficar las ventas mensuales de una marca ") 
    print("7. Salir") 

    opcion = input("Seleccione una opción válida ") 

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú 
    if opcion.isdigit() == False: 
        print("Seleccione un tipo de valor válido") 
    else: 
        opcion = int(opcion) 

    if opcion == 1: 
        datos_venta = {
            'Fecha': input("Ingrese la fecha en la que se efectuo la venta en este formato mm/dd/yy: "),
            'Mes_V': int(input("Ingrese el mes en el que se efectuo la venta: ")),
            'Dia_V': int(input("Ingrese el dia en el que efectuo la venta: ")),
            'Vendedor': input("Ingrese el nombre del vendedor que se encargo de realizar la venta: "),
            'Cliente': input("Ingrese el nombre del cliente que compro un vehiculo: "),
            'Marca': input("Ingrese la marca que compro el cliente: "),
            'Modelo': input("Ingrese el modelo que compro el cliente: "),
            'Anio': int(input("Ingrese el año del vehiculo: "))
        }

        precio_usd = input("Ingrese el precio del vehiculo: ")
        if '-' in precio_usd or int(precio_usd) < 0:
            print('Error: el precio debe ser un número positivo')
        else:
            datos_venta.update({
                'Precio_USD': int(precio_usd),
                'Porciento_Comision': float(input("Ingrese el porciento de la comision en decimales que se llevara el vendedor: ")),
                'Comision_USD': float(input("Ingrese la cantidad de la comision del vendedor: ")),
                'Cant_Cuotas': int(input("Ingrese la cantidad de cuotas en la que el cliente desea pagar: ")),
                'Cuotas_pagadas': int(input("Ingrese la cantidad de cuotas que el usuario ha pagado: ")),
            })
        ev2.new_sale(datos_venta)        

    elif opcion == 2: 
        ev2.marcas_con_ventas() 

    elif opcion == 3: 
        ev2.moroso() 

    if opcion == 4: 
        ev2.top10_vendedores() 

    elif opcion == 5: 
        ev2.top10_marcas() 

    elif opcion == 6: 
        marca = input('Ingrese la marca de auto: ')
        ev2.ventas_marcas_mes(marca) 

    elif opcion == 7: 
        seguir_en_programa = False 
        print("Eso ha sido todo, vuelva pronto!")         
    else: 
        print("Seleccione una opción válida.") 
