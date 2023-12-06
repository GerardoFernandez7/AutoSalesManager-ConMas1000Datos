# Importar modulos
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Declarar variables
df = pd.read_csv('ventas_autos.csv')

# Funciones
def new_sale(datos_venta):
    if datos_venta['Cuotas_pagadas'] >= datos_venta['Cant_Cuotas']:
            datos_venta['Tipo_cliente'] = 1
    else:
        datos_venta['Tipo_cliente'] = 0

    nueva_venta = [
        datos_venta['Fecha'],
        datos_venta['Mes_V'],
        datos_venta['Dia_V'],
        datos_venta['Vendedor'],
        datos_venta['Cliente'],
        datos_venta['Marca'],
        datos_venta['Modelo'],
        datos_venta['Anio'],
        datos_venta['Precio_USD'],
        datos_venta['Porciento_Comision'],
        datos_venta['Comision_USD'],
        datos_venta['Cant_Cuotas'],
        datos_venta['Cuotas_pagadas'],
        datos_venta['Tipo_cliente']
        ]

    with open('ventas_autos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nueva_venta)

def marcas_con_ventas():
    ventas = df.groupby('Marca').size()
    print("")
    print(ventas)
    print("")

def moroso():
    morosos = df.query('Tipo_cliente == 0')['Cliente'].unique()
    print("")
    print(morosos)
    print("")

def top10_vendedores():
    top_v = df.sort_values('Comision_USD', ascending=False).head(10)[['Vendedor', 'Comision_USD']]
    print("")
    print(top_v)
    print("")

def top10_marcas():
    top_m = df.sort_values('Precio_USD', ascending=False).head(10)[['Precio_USD', 'Marca', 'Modelo', 'Anio']]
    print("")
    print(top_m)
    print("")

def ventas_marcas_mes(marca):
    ventas = df.query(f'Marca == "{marca}"').groupby('Mes_V')['Precio_USD'].sum()
    ventas.plot(kind = 'bar')
    plt.title(f'Ventas por mes de la marca {marca}')
    plt.xlabel('Mes')
    plt.ylabel('Ventas (USD)')
    plt.show()