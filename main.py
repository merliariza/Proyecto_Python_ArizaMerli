import os
import json
import modules.menu as mn
import modules.mensajes as msg


isActive = True

if __name__ == "__main__":
    chachipun = {}

    while isActive:
        try:
            os.system('cls')
            print(msg.titulo)
            print(mn.menu)
            opcMenu = int(input(':)_'))
            match opcMenu:
                case 1:
                    isIngresar = True
                    while isIngresar:
                        try:
                            os.system('cls')
                            print(msg.tituloIngresar)
                            print(mn.menuIngresar)
                            opcIngresar = int(input(':)_'))
                            match opcIngresar:
                                case 1:
                                    pass
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
