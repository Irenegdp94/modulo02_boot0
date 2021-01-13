
def max(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] > m:
            m = l[ix]
    return m

def min(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for ix in l:
        suma += ix
    return suma / len(l)


funciones = {
    "max" : max,
    "min" : min,
    "med" : media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]

print(returnF("max")(1,3,-1,15,27))
print(returnF("min")(1,3,-1,15,27))
print(returnF("med")(1,3,-1,15,27))