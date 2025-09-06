"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()

        letras = [str(line.split("\t")[0]) for line in data]
        Numeros = [int(line.split("\t")[1]) for line in data]
        letras_unicas = sorted(set(letras))
        resultado = []
        for letra in letras_unicas:
            nums = [num for l, num in zip(letras, Numeros) if l == letra]
            resultado.append((letra, max(nums), min(nums)))
    return resultado