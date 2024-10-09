import modules.mensajes as msg
def validateData(message: str):
    opciones = ('N', 'n', 'S', 's')
    while True:
        accion = input(f'{message} ') 
        if accion not in opciones:
            print('La opción que ingresó no está permitida, por favor ingrese N (No) o S (Sí).')
        else:
            break 
    return accion.lower() == 'n'

def validateReturn(message: str):
    while True:
        accion = input(f'{message} ')  
        if accion.lower() == 's': 
            return True  
        elif accion.lower() == 'n': 
            return False 
        
def validateResponse(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que ud ingreso no esta permitida.......')
            validateData()
        elif (accion== 'S' ):
            flagFunction = True
        elif  ((accion) == 'N'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateResponse(message)