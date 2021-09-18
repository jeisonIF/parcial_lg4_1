import os
from config.db import CONECTION
from usuarios.crear_usuario import registro
menu =''''
Menu de opciones__
1. Registrar
2. Inciar sesion'''
opcion =1 


while opcion !=5:
        print(menu)
        try:
            opcion = int(input('Seleccione: '))
            os.system ("cls")
                
        except ValueError:
            print('Seleccione una opcion valida')
        else:
                
                if  opcion> 0 and opcion < 3:
                    if opcion == 1:
                        
                        print('Registrarse')
                        registro()       
                    elif opcion == 2:
                        print('Inicio de sesion')
                            
                               
                else:
                    print('Seleccione una opcion valida')
                    os.system ("cls") 
                     