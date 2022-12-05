from Personaje import Personaje

class Humano(Personaje):
    def __init__(self, nombre, raza, arma, vida, daño, bonificacion, familia):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__familia=familia
    
    def SetFamilia(self, familia):
        self.__familia=familia
    def GetFamilia(self):
        return self.__familia
    def __str__(self):
        return super().__str__(+"/// Familia: {}".format(self.__familia))

# Atributo único
    def SuperBono():
        pass

# Atributos generales
    def Historia(self):
        return super().Historia("Historia de humano")
    def Victoria(self):
        return super().Victoria("Humano gana")
    def Derrota(self):
        return super().Derrota("Los humanos se han hecho con el título de la civilización\ncon la tecnología más avanzada, junto a que nunca necesitaron\nhacer uso de magias raras. Esta vez, las magias raras vencieron.")
    def MSJInic(self):
        return super().MSJInic()