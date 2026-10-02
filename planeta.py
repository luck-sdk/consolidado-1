class planeta:
    def intit (self, nombre,masa,radio,distacia_del_sol,tiene_vida= False ):
        self.nombre =nombre
        self.masa=masa
        self.radio=radio
        self.distacia_del_sol=distacia_del_sol
        self.tiene_vida=tiene_vida

def calcular_densidad(self):
    pi = 3.1416
    volumen = (4/3)*pi*(self.radio*self.radio*self.radio)
    return self.masa/volumen

def es_planeta_exterior(self):
    if self.distancia_al_sol > 5.2:
        return True
    else:
        return False

def   str  (self):
    return "planeta:"+self.nombre+"-distancia al sol:"+str(self.distancia_al_sol)
p1=planeta("tierra",597200,637100,1.0,True)