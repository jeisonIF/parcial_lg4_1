from re import I
from config.db import CONECTION
import re
newUser ={
  'nombre' :'',
  'email' :'',
  'contrasena' :''}
def crearUsuario(nombre, email, contrasena):
    cursor = CONECTION.cursor()
    
    cursor.execute('''insert into 
        usuarios(nombre_user, email_user, contrasenaa_user)
        values(%s, %s, %s)''', (
          nombre,
          email,
          contrasena,
        ))
    
    #Creacion, modificacion, eliminacion de datos
    CONECTION.commit()
    
    cursor.close()
def registro():
  print('Registro de usuarios')
  newUser ={
    'nombre' :ingresoValidar('Nombre'),
    'email' :ingresoValidar('Email'),
    'contrasena' : ingresoValidar('Contraseña')
    }



def ingresoValidar(info):
  
  if(info=='Nombre'):
    print('nombre')   
  elif (info=='Email'):
    print('email')
  elif (info=='Contraseña'):
    print('contra') 
    contra()          
  
def contra():
  def valip(contra):
    regex = re.compile('^(?=\S{0,8}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
    return bool(regex.search(contra))
  contrasena =''
  bandera = False
  while bandera!=True:
    contrasena = input('Ingrese Contraseña: ')
    if(valip(contrasena)==True):
      bandera = True        
    


def validarNombre(info):
    dato =""
    bandera = 1
                
    while bandera!=0:
        dato = input('Ingrese '+info+': ')
        if not dato:
            print("Porfavor ingrese")        
        else:
            print("Se registro "+info)
            return dato
'''Crear una aplicación de consola en Python, 
que me permita registrar e iniciar usuarios. 
La aplicación debe tener un menú con dos opciones: 
La primera opcion, sera la de registrar usuarios, 
para lo cual el sistema solicitará 
el nombre (Requerido), 
email (Email) y 
una contraseña (Mínimo 8 caracteres, una mayúscula y un carácter especial), 
es importante mencionar 
que la contraseña se debe guardar 
de forma encriptada (hashlib). 
La segunda opción, sería el inicio de sesión. 
Para lo cual se solicitará el correo electrónico y 
la contraseña, el sistema validará las credenciales y 
dará un feedback al usuario, si el inicio es correcto, 
le mostrará un mensaje: Bienvenido Nombre del usuario; 
si las credenciales no incorrectas, mostrará el mensaje: Credenciales incorrectas.'''