def ingresar(historial):
    nickname1= input('Ingrese el apodo del jugador #1')
    if nickname1 not in historial:
        print(f'Bienvenido {nickname1}, es el jugador #1')
        nickname2= input('Ingrese el apodo del jugador #2')
        if nickname2 not in historial:
            print(f'Bienvenido {nickname2}, es el jugador #2')
        elif nickname2 in historial:
            print('Este apodo ya fue usado, ingrese un nuevo apodo')
            return
    elif nickname1 in historial:
        print('Este apodo ya fue usado, ingrese un nuevo apodo')
        return
    