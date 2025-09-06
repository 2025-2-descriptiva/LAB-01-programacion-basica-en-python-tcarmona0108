"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        col2 = [int(line.split("\t")[1]) for line in data]
        col4 = [line.split("\t")[3].split(",") for line in data]
        for i in range(len(col4)):
            col4[i] = [letra.lower() for letra in col4[i]]
        diccionario = {}
        for i in range(len(col4)):
            for letra in col4[i]:
                if letra in diccionario:
                    diccionario[letra] += col2[i]
                else:
                    diccionario[letra] = col2[i]
    return dict(sorted(diccionario.items()))