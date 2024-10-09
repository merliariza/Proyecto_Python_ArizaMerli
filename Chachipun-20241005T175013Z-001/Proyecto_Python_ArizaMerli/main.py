import os
import json
import modules.menu as mn
import modules.mensajes as msg
import modules.nickname as nn
import modules.validate as val
import modules.datos as da
import modules.estadisticas as es
from modules import historial as hi

if (__name__ == "__main__"):

    isActive = True
    
    while isActive:
        try:
            os.system('cls')
            print(msg.titulo)
            print(mn.menu)
            opcMenu = int(input(':)_')) #Permite digitar una opción del menú inicial.
            
            match opcMenu:
                case 1:
                    isIngresar = True
                    while isIngresar:
                        try:
                            os.system('cls')
                            print(msg.tituloIngresar)
                            print(mn.menuIngresar)
                            opcIngresar = int(input(':)_')) #Permite digitar una opción del menú ingresar.
                            
                            match opcIngresar:
                                case 1:  
                                    historial = nn.cargarHistorial() #Carga el historial dentro de la función historial.
                                    nn.ingresarUno(historial) #Ingresa a un usuario y juega vs pc.
                                    da.jugarConEscudoPC(historial) #Valida si hay un escudo y lo pone en funcionamiento.
                                    os.system('pause')

                                case 2: 
                                    historial = nn.cargarHistorial() #Carga el historial dentro de la función historial.
                                    resultado = nn.ingresarDos(historial) #Carga el ingreso de juegos y partida Uno vs Uno
                                    if resultado is not None: #Si el resultado no pertenece a None, significa que se guardaron
                                        nickname1, nickname2 = resultado 
                                        da.jugarConEscudoDosJugadores(nickname1, nickname2)
                                case 3:
                                    isActive = val.validateReturn(msg.msgVolver)
                                    if isActive:
                                        isIngresar = False  
                                    else:
                                        isIngresar = True
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 2:
                    isHistorial = True
                    while isHistorial:
                        try:
                            os.system('cls')
                            print(msg.tituloHistorial)
                            print(mn.menuHistorial)
                            opcHistorial = int(input(':)_')) #Permite digitar una opción del menú Historial.

                            match opcHistorial:
                                case 1:
                                    hi.mostrarHistorialJugadores() #Carga el historial de jugadores y sus roles.
                                    os.system('pause')
                                case 2:
                                    hi.mostrarTablaPuntos() #Carga el tablero de puntos por jugador ingresado.
                                    os.system('pause')
                                case 3:
                                    hi.mostrarHistorialIA() #Muestra el historial de juego de la IA
                                    os.system('pause')
                                case 4: 
                                    isActive = val.validateReturn(msg.msgVolver)
                                    if isActive:
                                        isHistorial = False  
                                    else:
                                        isHistorial = True
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 3: 
                    isEstadisticas=True
                    while isEstadisticas:
                        try:
                            os.system('cls')
                            print(msg.tituloEstadisticas)
                            print(mn.menuEstadisticas)
                            opcEstadisticas = int(input(':)_')) #Permite digitar una opción del menú Estadisticas.

                            match opcEstadisticas:
                                case 1:
                                    es.listarTresMejores() #Carga el listado de los tres mejores jugadores.
                                    os.system('pause')
                                case 2:
                                    es.listarUltimoPuesto() #Carga ultimo puesto por puntos.
                                    os.system('pause')
                                case 3:
                                    es.listarPerdedoresContraIA() #Carga perdedores contra IA.
                                    os.system('pause')
                                case 4:
                                    es.promedioJugadoresGanaronIA() #Carga promedio de ganadores vs IA
                                    os.system('pause')
                                case 5:
                                    isActive = val.validateReturn(msg.msgVolver)
                                    if isActive:
                                        isEstadisticas = False  
                                    else:
                                        isEstadisticas = True
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 4:
                    isActive = val.validateData(msg.msgSalir)
        except ValueError:
            print('Error en el dato ingresado')
            os.system('pause') 