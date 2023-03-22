import random

#input
jugador2=random.randint(1,3)
jugador1=int(input("ingrese su tiro,1=piedra,2=papel,3=tijera: "))

#processing

if jugador2==1 and jugador1==3:
    print("jugador2 gana:piedra le gana a tijeras")
elif jugador2==2 and jugador1==1:
    print("jugador2 gana:papel le gana a piedra")
elif jugador2==3 and jugador1==2:
    print("jugador2 gana:tijrtas le gana a papel")    
elif jugador1==1 and jugador2==3:
    print("jugador1 gana:piedra le gana a tijeras")
elif jugador1==2 and jugador2==1:
    print("jugador1 gana:papel le gana a piedra")
elif jugador1==3 and jugador2==2:
    print("jugador1 gana:tijeras le gana a papel")
elif jugador1==1 and jugador2==1:
    print("empate")
elif jugador1==2 and jugador2==2:
    print("empate")
elif jugaddor1==3 and jugador2==3:
    print("empate")
elif jugador1>3:
    print("no valido")                               