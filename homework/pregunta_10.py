"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        letras = [str(line.split("\t")[0]) for line in data]
        col4 = [line.split("\t")[3].split(",") for line in data]
        col5 = [line.split("\t")[4].split(",") for line in data]
        resultado = []  
        for i in range(len(data)):
            resultado.append((letras[i], len(col4[i]), len(col5[i])))
    return resultado