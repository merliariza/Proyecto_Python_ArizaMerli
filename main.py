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
                                    print(nn.ingresar)
                                    os.system('pause')
                                case 2:
                                    pass
                        except ValueError:
                            print('error en el dato ingresado')
                            os.system ('pause')
                case 2:
                    pass
                case 3: 
                    pass
        except ValueError:
            print('Error en el dato ingresado')
            os.system('pause') 
