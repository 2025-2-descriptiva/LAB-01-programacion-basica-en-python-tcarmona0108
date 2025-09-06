"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('./files/input/data.csv', mode='r', encoding='utf-8') as f:
        data = f.readlines()

        letras = [str(line.split("\t")[0]) for line in data]
        Numeros = [int(line.split("\t")[1]) for line in data]
        letras_unicas = sorted(set(letras))
        resultado = []
        for letra in letras_unicas:
            suma = sum(num for l, num in zip(letras, Numeros) if l == letra)
            resultado.append((letra, suma))

    return resultado

