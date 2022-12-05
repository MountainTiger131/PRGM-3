from Personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre, raza, arma, vida, daño, bonificacion, reino):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__reino=reino
    
    def SetReino(self, reino):
        self.__reino=reino
    def GetReino(self):
        return self.__reino
    def __str__(self):
        return super().__str__(+"/// Reino {}".format(self.__reino))

# Atributo único
    def QuitaVida():
        pass

# Atributos generales
    def Historia(self):
        return super().Historia(Elfo.GetNombre, Elfo.GetArma, Elfo.GetVida, Elfo.GetDaño)
    def Victoria(self):
        return super().Victoria("Elfo gana!")
    def Derrota(self):
        return super().Derrota("Los elfos son una raza antiquísima y\ncon mucha experiencia en combate")
    def MSJInic(self):
        return super().MSJInic()