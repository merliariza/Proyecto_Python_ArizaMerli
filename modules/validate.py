def validateData(message:str):
    global isAllow
    flagFunction = True
    opciones = ('','N','n','S','s')
    accion = input(f'{message}')
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        validateData()
    elif (bool(accion)== False):
        flagFunction = False
    elif  (bool(accion) == True):
        flagFunction = True
    return flagFunction