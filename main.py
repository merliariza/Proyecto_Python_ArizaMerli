import os
import json
import modules.menu as mn
import modules.mensajes as msg
import modules.nickname as nn
if (__name__ == "__main__"):
    
    isActive = True
    chachipun = {}

    while (isActive):
        try:
            os.system('cls')
            print(msg.titulo)
            print(mn.menu)
            opcMenu = int(input(':)_'))
            
            match opcMenu:
                case 1:
                    isIngresar = True
                    while (isIngresar):
                        try:
                            os.system('cls')
                            print(msg.tituloIngresar)
                            print(mn.menuIngresar)
                            opcIngresar = int(input(':)_'))
                            
                            match opcIngresar:
                                case 1:
                                    print(nn.ingresarUno)
                                    os.system('pause')
                                case 2:
                                    print(nn.ingresarDos)
                                    os.system('pause')
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 2:
                    isHistorial = True
                    while (isHistorial):
                        try:
                            os.system('cls')
                            print(msg.tituloHistorial)
                            print(mn.menuHistorial)
                            match opcIngresar:
                                case 1:
                                    print()
                                    os.system('pause')
                                case 2:
                                    print()
                                    os.system('pause')
                                case 3:
                                    print()
                                    os.system('pause')
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 3: 
                    isEstadisticas=True
                    while (isEstadisticas):
                        try:
                            os.system('cls')
                            print(msg.tituloHistorial)
                            print(mn.menuHistorial)
                            match opcIngresar:
                                case 1:
                                    print()
                                    os.system('pause')
                                case 2:
                                    print()
                                    os.system('pause')
                                case 3:
                                    print()
                                    os.system('pause')
                                case 4:
                                    print()
                                    os.system('pause')
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
        except ValueError:
            print('Error en el dato ingresado')
            os.system('pause') 
    