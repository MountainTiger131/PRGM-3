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
        aumentoDaño=input("¡Ingresa tu bonificación de ATK! (Entre 5 y 15)\n>>> ")
        if aumentoDaño > 15 or aumentoDaño < 5:
            print("Salirse de los límites no es bueno.\nIntenta ingresar un valor válido.")
            aumentoDaño=input("¡Ingresa  bonificación de ATK! (Entre 5 y 15)")
            nuevoDaño=Humano.GetDaño+aumentoDaño


# Atributos generales
    def Historia(self):
        return super().Historia("Historia de humano")
    def Victoria(self):
        return super().Victoria("Humano gana")
    def Derrota(self):
        return super().Derrota("Los humanos se han hecho con el título de la civilización\ncon la tecnología más avanzada, junto a que nunca necesitaron\nhacer uso de magias raras. Esta vez, las magias raras vencieron.")
    def MSJInic(self):
        return super().MSJInic()