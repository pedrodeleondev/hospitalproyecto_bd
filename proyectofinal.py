import mysql.connector
from mysql.connector import Error
import os

try:
    # Conexión a la base de datos MySQL
    conexion = mysql.connector.connect(
        host="bfl7kmhuq9ogo30q3i8m-mysql.services.clever-cloud.com",        # Cambia esto si tu servidor está en otro host
        user="uqdtymkfvmbrvylj",        # Tu usuario de MySQL
        password="T52jdkHft7iepQcAgD4y", # La contraseña de tu usuario
        database="bfl7kmhuq9ogo30q3i8m"  # El nombre de tu base de datos
    )
    if conexion.is_connected():
        print("¡Conexión exitosa a la base de datos!")

        # Crear un cursor para ejecutar las consultas
        cursor = conexion.cursor()


        

except Error as e:
    print(f"Error al conectarse a MySQL: {e}")


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def limpiar_consola():
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix
        os.system('clear')

def menu():
    correctNumber=False
    idExists=False
    while(correctNumber==False):
        print(f"{Colors.MAGENTA}**********************************************************************")
        print(f"*********** {Colors.RESET}BIENVENID@ AL SISTEMA DEL HOSPITAL MUGUERZA {Colors.MAGENTA}**************")
        print(f"**********************************************************************{Colors.RESET}")
        print(f"{Colors.MAGENTA}**********************************************************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}1.- Administrador{Colors.RESET} {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}2.- Medico{Colors.RESET}        {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}3.- Paciente{Colors.RESET}      {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}**********************************************************************{Colors.RESET}\n")
        roleNumber=input("Selecciona tu rol: ")
        if (roleNumber=="1" or roleNumber=="2" or roleNumber=="3"):
                limpiar_consola()
                correctNumber=True
        if (roleNumber=="2" or roleNumber=="3"):
            while(idExists==False):
                if(verificarID(roleNumber,input("\nIngresa tu ID: "))==True):
                    idExists=True
                else:
                    limpiar_consola()
                    print(f"\n{Colors.RED}!!! Ingresaste una id inexistente, intenta de nuevo.{Colors.RESET}")
            limpiar_consola()


        
        if(roleNumber=="1"):
                administrador()
        elif(roleNumber=="2"):
                medico()
        elif(roleNumber=="3"):
                paciente()
        else:
                limpiar_consola()
                print(f"\n{Colors.RED}!!! Ingresaste una opción incorrecta, intenta de nuevo.\n")
                
        
def verificarID(rolN,id):
    if(rolN=="2"):
        cursor.execute(f'SELECT * FROM medicos where id_medico="{id}"')
    else:
        cursor.execute(f'SELECT * FROM pacientes where id_paciente="{id}"')
    resultado = cursor.fetchall()
    if len(resultado)==0:
        return False
    else:
        return True
    input()
def administrador():
    print()

def medico():
    print()

def paciente(id):
    correctNumber=False
    while(correctNumber==False):
        print(f"{Colors.MAGENTA}**********************************************************************")
        print(f"************************* {Colors.RESET}MENU PACIENTE {Colors.MAGENTA}******************************")
        print(f"**********************************************************************{Colors.RESET}")
        print(f"{Colors.MAGENTA}**********************************************************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}1.- Ver mis datos{Colors.RESET} {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}2.- Editar mis datos{Colors.RESET}        {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}*********************** {Colors.RESET}3.- Ver mis consultas{Colors.RESET}      {Colors.MAGENTA}****************************")
        print(f"{Colors.MAGENTA}**********************************************************************{Colors.RESET}\n")
        roleNumber=input("Selecciona tu rol: ")
        print(roleNumber)
        if (roleNumber=="1" or roleNumber=="2" or roleNumber=="3"):
                limpiar_consola()
                correctNumber=True

        if(roleNumber=="1"):
                administrador()
        elif(roleNumber=="2"):
                medico()
        elif(roleNumber=="3"):
                paciente()
        else:
                limpiar_consola()
                print(f"\n{Colors.RED}!!! Ingresaste un numero incorrecto, intenta de nuevo.\n")
    print()

def paciente_verdatos():
    paciente()

##LLAMADO DE FUNCIONES
menu()