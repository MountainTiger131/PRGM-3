from Enano import Enano
from Elfo import Elfo
from Humano import Humano
import time

def Capturador():
    razaj1=""
    print("|[*]| ¡J1, selecciona tu raza! |[*]|\n")
    raza=input("[Enano]---[1]\n[Elfo]---[2]\n[Humano]---[3]\n>>> ")

    # Selección de raza
    while raza != "1" and raza != "2" and raza != "3":
        print("|[!]| ¡La raza seleccionada no existe! |[!]|")
        print("|[*]| Inténtalo nuevamente. |[*]|\n")
        raza=input("|[!]| ¡J1, selecciona tu raza! |[!]|")
        print("[Enano]---[1]\n[Elfo]---[2]\n[Humano]---[3]\n>>> ")

    if raza=="1":
        print("|[!]| ¡J1 ha seleccionado la raza 'Enano'! |[!]|\n")
        Enano.SetRaza(razaj1)
        razaj1="Enano"
    elif raza=="2":
        print("|[!]| ¡J1 ha seleccionado la raza 'Elfo'! |[!]|\n")
        razaj1="Elfo"
    elif raza=="3":
        print("|[!]| ¡J1 ha seleccionado la raza 'Humano'! |[!]|\n")
        razaj1="Humano"
    
    SeleccionArma()

# Selección de arma
def SeleccionArma():
    arma=""
    print("|[*]| ¡J1, selecciona tu arma! |[*]|\n")
    arma=input("[Arco: +200 ATK]---[1]\n[Espada: +350 ATK]---[2]\n[Dagas: +250 ATK]---[3]\n>>> ")
    while arma != "1" and arma!= "2" and arma !="3":
        print("|[!]| ¡La arma seleccionada no existe! |[!]|")
        print("|[*]| Inténtalo nuevamente. |[*]|\n")
        arma=input("[Arco: +200 ATK]---[1]\n[Espada: +350 ATK]---[2]\n[Dagas: +250 ATK]---[3]\n>>> ")

    if arma=="1":
        print("|[*]| ¡J1 ha seleccionado el Arco! |[*]|\n")
    elif arma=="2":
        print("|[*]| ¡J1 ha seleccionado la Espada! |[*]|\n")
    elif arma=="3":
        print("|[*]| ¡J1 ha seleccionado las Dagas! |[*]|\n")


    

    

    

def Main():
    print("Proceso iniciado.")
    time.sleep(0.1)
    print("Cargando...")
    time.sleep(0.1)
    key=0
    while key==0:
        Capturador()
        


Main()