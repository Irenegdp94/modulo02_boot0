# objeto perro

class Perro():
    #funcion constructora
    def __init__(self,n,e,p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        print("Guau,guau")
    
    def __str__(self):
        return "Soy un perro y me llamo {}".format(self.nombre)

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)

    def pasear(self):
        print("guau,guau, estoy paseando con {}".format(self.amo))
        