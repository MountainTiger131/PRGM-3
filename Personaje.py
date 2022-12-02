
class Personaje():
    def __init__(self, nombre, raza, arma, vida, daño, bonificacion):
        self.__nombre=nombre
        self.__raza=raza
        self.__arma=arma
        self.__vida=vida
        self.__daño=daño
        self.__bonif=bonificacion

    def __str__(self):
        return "Nombre: {} /// Raza: {} /// Arma: {} /// Vida: /// {} Daño: {} /// Bonificación: {}".format(self.__nombre, self.__raza, self.__arma, self.__vida, self.__daño, self.__bonif) 
    
    def SetNombre(self, nombre):
        self.__nombre=nombre
    def GetNombre(self):
        return self.__nombre
    
    def SetRaza(self, raza):
        self.__raza=raza
    def GetRaza(self):
        return self.__raza
    
    def SetArma(self, arma):
        self.__arma=arma
    def GetArma(self):
        return self.__arma

    def SetVida(self, vida):
        self.__vida=vida
    def Get(self):
        return self.__vida

    def SetDaño(self, daño):
        self.__daño=daño
    def GetDaño(self):
        return self.__daño

    def SetBonif(self, bonificacion):
        self.__bonif=bonificacion
    def GetBonif(self):
        return self.__bonif

    def Combate(self):
        pass
    def Historia(self):
        pass
    def Victoria(self):
        pass
    def Derrota(self):
        pass
    def MSJInic(self):
        pass