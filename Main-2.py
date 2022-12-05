from Enano import Enano
from Elfo import Elfo
from Humano import Humano
import time

enano=Enano("", "", "", "", "", "", "")
elfo=Elfo("", "", "", "", "", "", "")
humano=Humano("", "", "", "", "", "", "")

J1L=[]
J2L=[]

def Visualizador():
        for i in range(len(J1L)):
            print(J1L[i])

def Ejecutar():
    CapturadorJ1()

def CapturadorJ1():
    nombre=input("Jugador 1, escribe tu nombre:\n>>> ")
    print("Tu nombre se declarado como "+nombre+".\n")
    raza=input("Jugador 1, selecciona tu raza:\n[1] 'Enano'\n[2] 'Elfo'\n[3] 'Humano'\n>>> ")
    while raza!= "1" and raza != "2" and raza != "3":
        print("¡El caracter que has ingresado no es válido!\n¡Inténtalo nuevamente!\n")
        raza=input("Jugador 1, selecciona tu raza\n[1] 'Enano'\n[2] 'Elfo'\n[3] 'Humano'\n>>> ")
    if raza=="1":
        enano.SetNombre(nombre)
        print("¡Jugador 1 ha elegido ser Enano!")
        Visualizador()
        enano.SetVida(5000)
        enano.SetDaño(300)
        enano.SetBonif("")
        enano.SetClan("Ehkleoss")
        J1L.append(enano.GetRaza)
        J1L.append(enano.GetNombre)
        J1L.append(enano.GetVida)
        J1L.append(enano.GetBonif)
        J1L.append(enano.GetClan)
        print("¡Jugador 1, tu vida es "+str(enano.GetVida())+" y tu ATK es "+str(enano.GetDaño())+"!\n")
        enano.SetArma=SelectorArmasJ1()

    if raza=="2":
        elfo.SetNombre(nombre)
        print("¡Jugador 1 ha elegido ser Elfo!")
        elfo.SetRaza(raza)
        elfo.SetVida(6000)
        elfo.SetDaño(500)
        J1L.append(elfo.GetRaza)
        J1L.append(elfo.GetNombre)
        J1L.append(elfo.GetVida)
        J1L.append(elfo.GetBonif)
        J1L.append(elfo.GetReino)
        elfo.SetBonif("")
        elfo.SetReino("Luscinias")
        print("¡Jugador 1, tu vida es "+str(elfo.GetVida())+" y tu ATK es "+str(elfo.GetDaño())+"!\n")
        elfo.SetArma=SelectorArmasJ1()

    if raza=="3":
        humano.SetNombre(nombre)
        print("¡Jugador 1 ha elegido ser Humano!")
        humano.SetRaza(raza)
        humano.SetVida(4000)
        humano.SetDaño(600)
        J1L.append(humano.GetRaza)
        J1L.append(humano.GetNombre)
        J1L.append(humano.GetVida)
        J1L.append(humano.GetBonif)
        J1L.append(humano.GetFamilia)
        humano.SetBonif("")
        humano.SetFamilia("Ominous Inscription")
        print("¡Jugador 1, tu vida es "+str(humano.GetVida())+" y tu ATK es "+str(humano.GetDaño())+"!\n")
        humano.SetArma=SelectorArmasJ1()

def SelectorArmasJ1():
    arma=input("Ahora, selecciona tu arma\n[1] 'Arco'\n[2] 'Espada'\n[3] 'Lanza'\n[4] 'Mandoble'\n>>> ")
    cantatks=""
    dañobase=""
    while arma != "1" and arma != "2" and arma != "3" and arma != "4":
        print("¡El caracter que has ingresado no es válido!\n¡Inténtalo nuevamente!\n")
        arma=input("Ahora, selecciona tu arma\n[1] 'Arco'\n[2] 'Espada'\n[3] 'Lanza'\n[4] 'Mandoble'\n>>> ")
    if arma=="1":
        arma="Arco"
        cantatks=4
        dañobase=150*cantatks
        arma=("Arco", arma + str(dañobase))
        print("¡Jugador 1 eligió el arco!")
        CapturadorJ2()
    elif arma=="2":
        arma="Espada"
        cantatks=5
        dañobase=120*cantatks
        arma=("Espada", arma + str(dañobase))
        print("¡Jugador 1 eligió la espada!")
        CapturadorJ2()
    elif arma=="3":
        arma="Lanza"
        cantatks=8
        dañobase=75*cantatks
        arma=("Lanza", arma + str(dañobase))
        print("¡Jugador 1 eligió la lanza!")
        CapturadorJ2()
    elif arma=="4":
        arma="Mandoble"
        cantatks=2
        dañobase=300*cantatks
        arma=("Arco", arma + str(dañobase))
        print("¡Jugador 1 eligió el mandoble!")
        CapturadorJ2()

################################################################################################

def CapturadorJ2():
    print("¡Ahora es el turno del Jugador 2!")
    nombre=input("Jugador 2, escribe tu nombre:\n>>> ")
    print("Tu nombre se declarado como "+nombre+".\n")
    raza=input("Jugador 2, selecciona tu raza:\n[1] 'Enano'\n[2] 'Elfo'\n[3] 'Humano'\n>>> ")
    while raza!= "1" and raza != "2" and raza != "3":
        print("¡El caracter que has ingresado no es válido!\n¡Inténtalo nuevamente!\n")
        raza=input("Jugador 2, selecciona tu raza\n[1] 'Enano'\n[2] 'Elfo'\n[3] 'Humano'\n>>> ")
    if raza=="1":
        enano.SetNombre(nombre)
        print("¡Jugador 2 ha elegido ser Enano!")
        Visualizador()
        enano.SetVida(5000)
        enano.SetDaño(300)
        enano.SetBonif("")
        enano.SetClan("Ehkleoss")
        J1L.append(enano.GetRaza)
        J1L.append(enano.GetNombre)
        J1L.append(enano.GetVida)
        J1L.append(enano.GetBonif)
        J1L.append(enano.GetClan)
        print("¡Jugador 2, tu vida es "+str(enano.GetVida())+" y tu ATK es "+str(enano.GetDaño())+"!\n")
        enano.SetArma=SelectorArmasJ2()
    
    if raza=="2":
        elfo.SetNombre(nombre)
        print("¡Jugador 2 ha elegido ser Elfo!")
        elfo.SetRaza(raza)
        elfo.SetVida(6000)
        elfo.SetDaño(500)
        J1L.append(elfo.GetRaza)
        J1L.append(elfo.GetNombre)
        J1L.append(elfo.GetVida)
        J1L.append(elfo.GetBonif)
        J1L.append(elfo.GetReino)
        elfo.SetBonif("")
        elfo.SetReino("Luscinias")
        print("¡Jugador 2, tu vida es "+str(elfo.GetVida())+" y tu ATK es "+str(elfo.GetDaño())+"!\n")
        elfo.SetArma=SelectorArmasJ2()

    if raza=="3":
        humano.SetNombre(nombre)
        print("¡Jugador 2 ha elegido ser Humano!")
        humano.SetRaza(raza)
        humano.SetVida(4000)
        humano.SetDaño(600)
        J1L.append(humano.GetRaza)
        J1L.append(humano.GetNombre)
        J1L.append(humano.GetVida)
        J1L.append(humano.GetBonif)
        J1L.append(humano.GetFamilia)
        humano.SetBonif("")
        humano.SetFamilia("Ominous Inscription")
        print("¡Jugador 2, tu vida es "+str(humano.GetVida())+" y tu ATK es "+str(humano.GetDaño())+"!\n")
        humano.SetArma=SelectorArmasJ2()

def SelectorArmasJ2():
    arma=input("Ahora, selecciona tu arma\n[1] 'Arco'\n[2] 'Espada'\n[3] 'Lanza'\n[4] 'Mandoble'\n>>> ")
    cantatks=""
    dañobase=""
    while arma != "1" and arma != "2" and arma != "3" and arma != "4":
        print("¡El caracter que has ingresado no es válido!\n¡Inténtalo nuevamente!\n")
        arma=input("Ahora, selecciona tu arma\n[1] 'Arco'\n[2] 'Espada'\n[3] 'Lanza'\n[4] 'Mandoble'\n>>> ")
    if arma=="1":
        arma="Arco"
        cantatks=4
        dañobase=150*cantatks
        arma=("Arco", arma + str(dañobase))
        print("¡Jugador 2 eligió el arco!")
        Combate()
    elif arma=="2":
        arma="Espada"
        cantatks=5
        dañobase=120*cantatks
        arma=("Espada", arma + str(dañobase))
        print("¡Jugador 2 eligió la espada!")
        Combate()
    elif arma=="3":
        arma="Lanza"
        cantatks=8
        dañobase=75*cantatks
        arma=("Lanza", arma + str(dañobase))
        print("¡Jugador 2 eligió la lanza!")
        Combate()
    elif arma=="4":
        arma="Mandoble"
        cantatks=2
        dañobase=300*cantatks
        arma=("Arco", arma + str(dañobase))
        print("¡Jugador 2 eligió el mandoble!")
        Combate()

################################################################################################

def Combate():
    print("¡Ahora empieza el combate!")
    
def Main():
    print("Proceso iniciado.")
    Ejecutar()

Main()