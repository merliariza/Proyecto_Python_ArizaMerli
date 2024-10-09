import json

MY_DATABASE = 'puntajes.json'
HISTORIAL_DATABASE = 'nickname.json'

def cargarDatos():
    try:
        with open(MY_DATABASE, "r") as rf:
            datos = json.load(rf)
    except FileNotFoundError:
        datos = {"puntajes": {}}
    return datos

def cargarHistorial():
    try:
        with open(HISTORIAL_DATABASE, "r") as rf:
            historial = json.load(rf)
    except FileNotFoundError:
        historial = {}
    return historial

def guardarDatos(datos):
    try:
        with open(MY_DATABASE, "w") as wf:
            json.dump(datos, wf, indent=4)
            print("Datos guardados correctamente.")  
    except Exception as e:
        print("Error al guardar datos:", e)

def mostrarHistorialJugadores():
    historial = cargarHistorial()
    if not historial:
        print("No hay historial de jugadores registrado.")
        return

    print("\n--- Historial de Jugadores ---")
    for nickname, rol in historial.items():
        print(f"Nickname: {nickname}, Rol: {rol}")

def mostrarTablaPuntos():
    try:
        with open(MY_DATABASE, 'r') as rf:
            puntajes = json.load(rf)
            print("Tabla de Puntos:")
            for nickname, datos in puntajes.items():
                print(f"Nickname: {nickname}, Puntos: {datos['puntos']}, Escudos: {datos['escudos']}")
    except FileNotFoundError:
        print("Error: El archivo de puntajes no se encuentra.")
    except json.JSONDecodeError:
        print("Error: No se pudo leer el archivo JSON. Asegúrate de que esté correctamente formateado.")
 
def actualizarPuntosIA(nickname_ia, rondas_ganadas):
    datos = cargarDatos()
    

    if "jugadores" not in datos:
        datos["jugadores"] = {}  

    if nickname_ia not in datos["jugadores"]:
        datos["jugadores"][nickname_ia] = {"puntos": 0, "escudos": 0}

    datos["jugadores"][nickname_ia]["puntos"] += 2 * rondas_ganadas 

    print(f"Datos antes de guardar: {datos}")

    guardarDatos(datos)

def mostrarHistorialIA():
    datos = cargarDatos()
    print("Historial de Puntos de la IA:")
    
    if "jugadores" not in datos:
        print("No hay datos de jugadores disponibles.")
        return

    jugadores = datos["jugadores"]
    for nickname, datos_jugador in jugadores.items():
        if "IA_" in nickname: 
            print(f"Nickname: {nickname}, Puntos: {datos_jugador['puntos']}, Escudos: {datos_jugador['escudos']}")

    for nickname, datos_jugador in datos["jugadores"].items():
        if nickname.startswith("IA_"): 
            puntos = datos_jugador.get('puntos', 0)
            escudos = datos_jugador.get('escudos', 0)
            print(f"Nickname: {nickname}, Puntos: {puntos}, Escudos: {escudos}")

