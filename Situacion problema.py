"""
Situación Problema
Santiago Acosta Niño y Juan Pablo Cervantes Velarde
     A01986171                  A01986318
"""

#import
import pandas as pd
import matplotlib.pyplot as plt

#Variables


#Funciones
def mp():
    opcion = 0

    while opcion != 7:
        print("\n====== Car Data Analyzer ======")
        print("Menú Principal:")
        print("1.- Análisis por Precios")
        print("2.- Análisis por Marca")
        print("3.- Análisis de Millaje")
        print("4.- Análisis por Año de Fabricación")
        print("5.- Análisis por Tipo de Combustible")
        print("6.- Análisis por Tamaño de Motor")
        print("7.- Salir")

        opcion = int(input("Seleccione una opción (1-7): "))

        if opcion > 7 or opcion < 1:
            print("\n!!Seleccione una opción válida!!")

        elif opcion == 7:
            print("\nCerrando programa...")


#Main
datos = pd.read_csv("car_sales_data.csv")

mp()

        
