"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open("data.csv","r") as file:
    data = file.readlines()

data = [line.replace("\n","") for line in data ] 
data = [line.split("\t") for line in data]

dicc = {}
for line in data:
    letras=line[3].split(",")
    for i in letras:
        if i not in dicc:
            dicc[i]=int(line[1])
        else:
            dicc[i]+=int(line[1])
lista = [(letra, v) for letra, v in dicc.items()]
lista.sort(key = lambda x:x[0])
a = {k:v for (k,v) in lista} 

print (a)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum(int(line[1]) for line in data)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """ 
    columna = [line[0] for line in data]
    letras = set(columna)
    a=[(letra, columna.count(letra)) for letra in letras]
    a.sort(key = lambda x:x[0])
    return a


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    columna = [line[0] for line in data]
    columna.sort()
    letras = {}
    for i in columna:
        letras[i]=0
    for line in data:
        letras[line[0]]+=int(line[1])
    lista = [(letra, suma) for letra, suma in letras.items()]
    return (lista)

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses =[['%02d' % (i+1), 0] for i in range(12)]
    for line in data:
        meses[int(line[2][5:7]) - 1][1]+=1
    meses=[(k,v) for [k,v] in meses]
    print(meses)

    return meses


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    columna = [line[0] for line in data]
    columna.sort()
    dicc = {}
    for i in columna:
        dicc[i]=[0,10]
    for line in data:
        if int(line[1]) > dicc[line[0]][0]:
            dicc[line[0]][0]=int(line[1])
        if int(line[1]) < dicc[line[0]][1]:
            dicc[line[0]][1]=int(line[1])
    lista = [(letra, v[0], v[1]) for letra, v in dicc.items()]
    return (lista)
    

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    dicc = {}
    for line in data:
        campo=line[4].split(",")
        for i in campo:
            texto, numero = i.split(":")[0],int(i.split(":")[1])
            if texto not in dicc:
                dicc[texto]=[numero,numero]
            else:
                if numero > dicc[texto][1]:
                    dicc[texto][1]=numero
                elif numero < dicc[texto][0]:
                    dicc[texto][0]=numero
    lista = [(letra, v[0], v[1]) for letra, v in dicc.items()]
    lista.sort(key = lambda x:x[0])
    return lista

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    dicc = {}
    for i in range(10):
        dicc[i]=[]
    for line in data:
            dicc[int(line[1])].append(line[0])
    lista = [tuple(i) for i in dicc.items()]
    return (lista)
    
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    dicc = {}
    for i in range(10):
        dicc[i]=set()
    for line in data:
            dicc[int(line[1])].add(line[0])
    for k in dicc.keys():
        dicc[k]=list(dicc[k])
        dicc[k].sort()
    lista = [tuple(i) for i in dicc.items()]
    return (lista)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    dicc = {}
    for line in data:
        campo=line[4].split(",")
        for i in campo:
            texto = i.split(":")[0]
            if texto not in dicc:
                dicc[texto]=1
            else:
                dicc[texto]+=1
    lista = [(letra, v) for letra, v in dicc.items()]
    lista.sort(key = lambda x:x[0])
    a= {k:v for (k,v) in lista}
    return a


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """

    lista=[]
    for line in data:
        a = line[0]
        b = len(line[3].split(","))
        c = len(line[4].split(","))
        lista.append((a,b,c))
    return (lista)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """

    dicc = {}
    for line in data:
        letras=line[3].split(",")
        for i in letras:
            if i not in dicc:
                dicc[i]=int(line[1])
            else:
                dicc[i]+=int(line[1])
    lista = [(letra, v) for letra, v in dicc.items()]
    lista.sort(key = lambda x:x[0])
    a = {k:v for (k,v) in lista} 

    return a


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
