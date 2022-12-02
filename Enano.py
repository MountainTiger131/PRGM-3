from Personaje import Personaje

class Enano(Personaje):
    def __init__(self, nombre, raza, arma, vida, daño, bonificacion, clan):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__clan=clan
    
    def SetClan(self, clan):
        self.__clan=clan
    def GetClan(self):
        return self.__clan
    def __str__(self):
        return super().__str__(+"/// Clan: {}".format(self.__clan))

# Atributo único
    def AumentaVida():
        NuevaVida=input(int("Ingrese el aumento de vida (Entre 50-100)"))
        if NuevaVida<50 or NuevaVida>100:
            print("Error de tipeo")
    '''AumentaVida, este método se invoca antes de la ronda 1 en la que participe un objeto de la clase
    Enano, este debe solicitar al usuario que ingrese el aumento de la vida, este aumento debe ser
    un número entero entre 50 y 100
    '''
# Atributos generales
    def Historia(self):
        return super().Historia("Historia de enano")
    def Victoria(self):
        return super().Victoria("Enano gana")
    def Derrota(self):
        return super().Derrota("Enano pierde")
    