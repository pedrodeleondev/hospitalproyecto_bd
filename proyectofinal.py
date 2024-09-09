import mysql.connector
from mysql.connector import Error
import os

id_usuario=0

try:
    conexion = mysql.connector.connect(
        host="bfl7kmhuq9ogo30q3i8m-mysql.services.clever-cloud.com", 
        user="uqdtymkfvmbrvylj",       
        password="T52jdkHft7iepQcAgD4y", 
        database="bfl7kmhuq9ogo30q3i8m" 
    )
    if conexion.is_connected():
        print("¡Conexión exitosa a la base de datos!")

        cursor = conexion.cursor()
        
except Error as e:
    print(f"Error al conectarse a MySQL: {e}")


class Colors:
    # Bold
    BOLD = '\033[1m'
    # Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[38;5;21m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    ORANGE = '\033[38;5;208m'  # Color naranja
    PURPLE = '\033[38;5;129m'  # Color morado
    GRAY = '\033[90m'          # Color gris
    # Reset
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
                paciente(id_usuario)
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
        global id_usuario
        id_usuario=id
        return True
    
def administrador():
    print()

def medico(id):
    correctNumber=False
    while(correctNumber==False):
        print(f"{Colors.BLUE}{'*' * 70}")
        print(f"{'*' * 27} {Colors.RESET}MENU PACIENTE {Colors.BLUE}{'*' * 28}")
        print(f"{'*' * 70}{Colors.RESET}")
        print(f"{Colors.BLUE}{'*' * 70}")
        print(f"{'*' * 23} {Colors.RESET}1.- Ver mis datos     {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}2.- Editar mis datos  {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}3.- Ver mis citas     {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 70}{Colors.RESET}\n")


        selectOption=input(f"Selecciona la opcion que deseas: {Colors.RESET}")

        if(selectOption=="1"):
                paciente_verdatos(id)
        elif(selectOption=="2"):
                paciente_editardatos(id)
        elif(selectOption=="3"):
                paciente_verconsulta(id)
        else:
                limpiar_consola()
                print(f"\n{Colors.RED}!!! Ingresaste un numero incorrecto, intenta de nuevo.\n")
        if (selectOption=="1" or selectOption=="2" or selectOption=="3"):
                limpiar_consola()

def paciente(id):
    correctNumber=False
    while(correctNumber==False):
        print(f"{Colors.BLUE}{'*' * 70}")
        print(f"{'*' * 27} {Colors.RESET}MENU PACIENTE {Colors.BLUE}{'*' * 28}")
        print(f"{'*' * 70}{Colors.RESET}")
        print(f"{Colors.BLUE}{'*' * 70}")
        print(f"{'*' * 23} {Colors.RESET}1.- Ver mis datos     {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}2.- Editar mis datos  {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}3.- Agendar cita      {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}4.- Ver mis citas     {Colors.BLUE}{'*' * 24}")
        print(f"{'*' * 70}{Colors.RESET}\n")


        selectOption=input(f"Selecciona la opcion que deseas: {Colors.RESET}")

        if(selectOption=="1"):
                paciente_verdatos(id)
        elif(selectOption=="2"):
                paciente_editardatos(id)
        elif(selectOption=="3"):
                paciente_editardatos(id)
        elif(selectOption=="4"):
                paciente_verconsulta(id)
        else:
                limpiar_consola()
                print(f"\n{Colors.RED}!!! Ingresaste un numero incorrecto, intenta de nuevo.\n")
        if (selectOption=="1" or selectOption=="2" or selectOption=="3"):
                limpiar_consola()


##FUNCIONES DE LA OPCION DE MEDICOS


##FUNCIONES DE LA OPCION DE PACIENTES
def paciente_verdatos(id):
    print(f"\n{Colors.BOLD}Tus datos son los siguientes:\n{Colors.RESET}")
    cursor.execute(f'SELECT * FROM pacientes where id_paciente="{id}"')
    resultado = cursor.fetchall()
    print(f"Tu {Colors.CYAN}nombre{Colors.RESET} es {resultado[0][1]} {resultado[0][2]} {resultado[0][3]}.")
    print(f"Tu {Colors.CYAN}telefono{Colors.RESET} es {resultado[0][4]}.")
    print(f"Tu {Colors.CYAN}email{Colors.RESET} es {resultado[0][5]}.")
    print(f"Tu {Colors.CYAN}direccion{Colors.RESET} es {resultado[0][6]}.")
    print(f"Tu {Colors.CYAN}fecha de nacimiento{Colors.RESET} es {resultado[0][7]}.")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presionar la tecla ENTER para continuar...\n{Colors.RESET}")

def paciente_editardatos(id):
    print(f"\n{Colors.BOLD}Editar tus datos:\n{Colors.RESET}")
    
    cursor.execute(f'SELECT * FROM pacientes where id_paciente="{id}"')
    resultado = cursor.fetchall()
    
    print(f"Nombre actual: {resultado[0][1]}")
    nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener el actual): ")
    if nuevo_nombre == "":
        nuevo_nombre = resultado[0][1]

    print(f"Apellido paterno actual: {resultado[0][2]}")
    nuevo_apellido_paterno = input("Nuevo apellido paterno (dejar vacío para mantener el actual): ")
    if nuevo_apellido_paterno == "":
        nuevo_apellido_paterno = resultado[0][2]

    print(f"Apellido materno actual: {resultado[0][3]}")
    nuevo_apellido_materno = input("Nuevo apellido materno (dejar vacío para mantener el actual): ")
    if nuevo_apellido_materno == "":
        nuevo_apellido_materno = resultado[0][3]

    print(f"Teléfono actual: {resultado[0][4]}")
    nuevo_telefono = input("Nuevo teléfono (dejar vacío para mantener el actual): ")
    if nuevo_telefono == "":
        nuevo_telefono = resultado[0][4]

    print(f"Email actual: {resultado[0][5]}")
    nuevo_email = input("Nuevo email (dejar vacío para mantener el actual): ")
    if nuevo_email == "":
        nuevo_email = resultado[0][5]

    print(f"Dirección actual: {resultado[0][6]}")
    nueva_direccion = input("Nueva dirección (dejar vacío para mantener el actual): ")
    if nueva_direccion == "":
        nueva_direccion = resultado[0][6]

    # Ejecuta la consulta de actualización
    cursor.execute(f'''
        UPDATE pacientes 
        SET nombre="{nuevo_nombre}", apellido_paterno="{nuevo_apellido_paterno}", apellido_materno="{nuevo_apellido_materno}", 
        telefono="{nuevo_telefono}", email="{nuevo_email}", direccion="{nueva_direccion}"
        WHERE id_paciente="{id}"
    ''')
    conexion.commit()  # Aplica los cambios a la base de datos
    print(f"\n{Colors.GREEN}Datos actualizados correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def paciente_verconsulta(id):
    print(f"\n{Colors.BOLD}Editar tus datos:\n{Colors.RESET}")
    c=0
    cursor.execute(f'SELECT * FROM citas where id_paciente="{id}"')
    resultados = cursor.fetchall()
    for fila in resultados:
        c+=1
        idCita=fila[0]
        idMedico=fila[1]
        fechaCita=fila[4]
        horaCita=fila[5]
        descripcion=fila[6]
        estadoCita=fila[7]
        cursor.execute(f'SELECT * FROM medicos where id_medico="{idMedico}"')
        resultadoMedico = cursor.fetchall()
        nombreMedico=f"{resultadoMedico[0][1]} {resultadoMedico[0][2]} {resultadoMedico[0][3]}"
        print(f"Consulta N-{c}: La fecha de la cita está programada para el día {fechaCita} a la hora {horaCita}, la descripción de la cita es {descripcion}, el medico es {nombreMedico} y el estado de la cita es {estadoCita}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def paciente_agendarcita(id):
    

##LLAMADO DE FUNCIONES
menu()