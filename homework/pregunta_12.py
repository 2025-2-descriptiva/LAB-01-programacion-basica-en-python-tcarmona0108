"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        col1 = [line.split("\t")[0] for line in data]
        col5 = [line.split("\t")[4].split(",") for line in data]
        for i in range(len(col5)):
            col5[i] = [int(clave.split(":")[1]) for clave in col5[i]]
        diccionario = {}
        for i in range(len(col1)):
            if col1[i] in diccionario:
                diccionario[col1[i]] += sum(col5[i])
            else:
                diccionario[col1[i]] = sum(col5[i])
    return dict(sorted(diccionario.items()))
