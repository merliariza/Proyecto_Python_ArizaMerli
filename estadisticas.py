import json

MY_DATABASE = 'puntajes.json'

def cargarDatos():
    try:
        with open(MY_DATABASE, "r") as rf:
            datos = json.load(rf)
    except FileNotFoundError:
        datos = {"puntajes": {}}
    return datos

def listarTresMejores():
    datos = cargarDatos()
    puntajes = datos.get("puntajes", {})
    
    mejoresJugadores = sorted(puntajes.items(), key=lambda x: x[1]['puntos'], reverse=True)[:3]
    
    print("Tres mejores jugadores:")
    for nickname, info in mejoresJugadores:
        print(f"{nickname}: {info['puntos']} puntos")

def listarUltimoPuesto():
    datos = cargarDatos()
    puntajes = datos.get("puntajes", {})
    

    if not puntajes:
        print("No hay jugadores registrados.")
        return

    ultimo_jugador = min(puntajes.items(), key=lambda x: x[1]['puntos'])
    
    print("Último puesto:")
    print(f"{ultimo_jugador[0]}: {ultimo_jugador[1]['puntos']} puntos")

def listarPerdedoresContraIA():
    datos = cargarDatos()
    puntajes = datos.get("puntajes", {})
    
    perdedores = {nickname: info for nickname, info in puntajes.items() if info['puntos'] < 0}

    print("Jugadores que han perdido contra la IA:")
    if not perdedores:
        print("No hay jugadores que hayan perdido contra la IA.")
    else:
        for nickname, info in perdedores.items():
            print(f"{nickname}: {info['puntos']} puntos")

def promedioJugadoresGanaronIA():
    datos = cargarDatos()
    puntajes = datos.get("puntajes", {})
    
    ganadores = [info['puntos'] for info in puntajes.values() if info['puntos'] > 0]
    
    if not ganadores:
        print("No hay jugadores que hayan ganado a la IA.")
        return

    promedio = sum(ganadores) / len(ganadores)
    print(f"Promedio de puntos de jugadores que ganaron a la IA: {promedio:.2f}")