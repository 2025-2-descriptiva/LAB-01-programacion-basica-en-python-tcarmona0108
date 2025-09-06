"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()

        claves_valores = [line.split("\t")[4].split(",") for line in data]  
        for i in range(len(claves_valores)):
            claves_valores[i] = [clave.split(":")[0] for clave in claves_valores[i]]
        diccionario = {}
        for claves in claves_valores:
            for clave in claves:
                if clave in diccionario:
                    diccionario[clave] += 1
                else:
                    diccionario[clave] = 1
    return diccionario