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
                medico(id_usuario)
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
    correctNumber = False
    while not correctNumber:
        print(f"{Colors.GREEN}{'*' * 80}")
        print(f"{'*' * 27} {Colors.RESET} MENU ADMINISTRADOR  {Colors.GREEN}{'*' * 31}")
        print(f"{'*' * 80}{Colors.RESET}")
        print(f"{Colors.GREEN}{'*' *80}")
        print(f"{'*' * 23} {Colors.RESET}1.- Ver datos de pacientes      {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}2.- Buscar paciente por ID      {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}3.- Editar datos de un paciente {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}4.- Agregar nuevo paciente      {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}5.- Ver datos de médicos        {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}6.- Buscar médico por ID        {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}7.- Editar datos de un médico   {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}8.- Agregar nuevo médico        {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}9.- Ver especialidades          {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}10.- Buscar especialidad por ID {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}11.- Editar una especialidad    {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}12.- Agregar una especialidad   {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}13.- Ver horarios               {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}14.- Buscar horario por ID      {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}15.- Editar un horario          {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}16.- Agregar nuevo horario      {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}17.- Ver todas las citas        {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}18.- Buscar cita por ID         {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}19.- Editar una cita            {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 23} {Colors.RESET}20.- Agregar nueva cita         {Colors.GREEN}{'*' * 24}")
        print(f"{'*' * 80}{Colors.RESET}\n")

        selectOption = input(f"Selecciona la opción que deseas: {Colors.RESET}")

        if selectOption == "1":
            admin_ver_datos_pacientes()
        elif selectOption == "2":
            admin_buscar_paciente_por_id()
        elif selectOption == "3":
            admin_editar_datos_paciente()
        elif selectOption == "4":
            admin_agregar_nuevo_paciente()
        elif selectOption == "5":
            admin_ver_datos_medicos()
        elif selectOption == "6":
            admin_buscar_medico_por_id()
        elif selectOption == "7":
            admin_editar_datos_medico()
        elif selectOption == "8":
            admin_agregar_nuevo_medico()
        elif selectOption == "9":
            admin_ver_especialidades()
        elif selectOption == "10":
            admin_buscar_especialidad_por_id()
        elif selectOption == "11":
            admin_editar_especialidad()
        elif selectOption == "12":
            admin_agregar_especialidad()
        elif selectOption == "13":
            admin_ver_horarios()
        elif selectOption == "14":
            admin_buscar_horario_por_id()
        elif selectOption == "15":
            admin_editar_horario()
        elif selectOption == "16":
            admin_agregar_horario()
        elif selectOption == "17":
            admin_ver_citas()
        elif selectOption == "18":
            admin_buscar_cita_por_id()
        elif selectOption == "19":
            admin_editar_cita()
        elif selectOption == "20":
            admin_agregar_cita()
        else:
            limpiar_consola()
            print(f"\n{Colors.RED}!!! Ingresaste un número incorrecto, intenta de nuevo.\n")

        if selectOption in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
            limpiar_consola()



def medico(id):
    correctNumber = False
    while correctNumber == False:
        print(f"{Colors.YELLOW}{'*' * 70}")
        print(f"{'*' * 27} {Colors.RESET}  MENU MÉDICO    {Colors.YELLOW}{'*' * 25}")
        print(f"{'*' * 70}{Colors.RESET}")
        print(f"{Colors.YELLOW}{'*' * 70}")
        print(f"{'*' * 23} {Colors.RESET}1.- Ver mis datos        {Colors.YELLOW}{'*' * 21}")
        print(f"{'*' * 23} {Colors.RESET}2.- Editar mis datos     {Colors.YELLOW}{'*' * 21}")
        print(f"{'*' * 23} {Colors.RESET}3.- Ver mis citas        {Colors.YELLOW}{'*' * 21}")
        print(f"{'*' * 23} {Colors.RESET}4.- Ver mis pacientes    {Colors.YELLOW}{'*' * 21}")
        print(f"{'*' * 23} {Colors.RESET}5.- Ver mi especialidad  {Colors.YELLOW}{'*' * 21}")
        print(f"{'*' * 70}{Colors.RESET}\n")

        selectOption = input(f"Selecciona la opción que deseas: {Colors.RESET}")

        if selectOption == "1":
            medico_verdatos(id)
        elif selectOption == "2":
            medico_editardatos(id)
        elif selectOption == "3":
            medico_vercitas(id)
        elif selectOption == "4":
            medico_verpacientes(id)
        elif selectOption == "5":
            medico_verespecialidad(id)
        else:
            limpiar_consola()
            print(f"\n{Colors.RED}!!! Ingresaste un número incorrecto, intenta de nuevo.\n")
        if selectOption in ["1", "2", "3", "4", "5"]:
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
                paciente_agendarcita(id)
        elif(selectOption=="4"):
                paciente_verconsulta(id)
        else:
                limpiar_consola()
                print(f"\n{Colors.RED}!!! Ingresaste un numero incorrecto, intenta de nuevo.\n")
        if (selectOption=="1" or selectOption=="2" or selectOption=="3" or selectOption=="4"):
                limpiar_consola()


##FUNCIONES DE LA OPCION ADMINISTRADOR
def admin_ver_datos_pacientes():
    cursor.execute('SELECT * FROM pacientes')
    resultados = cursor.fetchall()
    
    if resultados:
        print(f"\n{Colors.BOLD}Lista de todos los pacientes:\n{Colors.RESET}")
        for paciente in resultados:
            print(f"ID: {paciente[0]}")
            print(f"Nombre: {paciente[1]} {paciente[2]} {paciente[3]}.")
            print(f"Teléfono: {paciente[4]}.")
            print(f"Email: {paciente[5]}.")
            print(f"Dirección: {paciente[6]}.")
            print(f"Fecha de nacimiento: {paciente[7]}.")
            print(f"{Colors.BLUE}{'*' * 70}{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}No se encontraron pacientes en la base de datos.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_buscar_paciente_por_id():
    id = input(f"Introduce el ID del paciente: {Colors.RESET}")

    if not verificarID("2", id):
        print(f"\n{Colors.RED}El paciente con ID {id} no existe. Intenta de nuevo.{Colors.RESET}\n")
        return

    cursor.execute(f'SELECT * FROM pacientes WHERE id_paciente="{id}"')
    resultado = cursor.fetchall()

    if resultado:
        print(f"\n{Colors.BOLD}Datos del paciente:\n{Colors.RESET}")
        print(f"Nombre: {resultado[0][1]} {resultado[0][2]} {resultado[0][3]}.")
        print(f"Teléfono: {resultado[0][4]}.")
        print(f"Email: {resultado[0][5]}.")
        print(f"Dirección: {resultado[0][6]}.")
        print(f"Fecha de nacimiento: {resultado[0][7]}.")
    else:
        print(f"\n{Colors.RED}No se encontraron datos para el paciente con ID {id}.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_editar_datos_paciente():
    id = input(f"Introduce el ID del paciente: {Colors.RESET}")

    if not verificarID("2", id):
        print(f"\n{Colors.RED}El paciente con ID {id} no existe. Intenta de nuevo.{Colors.RESET}\n")
        return

    print(f"\n{Colors.BOLD}Editar datos del paciente:\n{Colors.RESET}")

    cursor.execute(f'SELECT * FROM pacientes WHERE id_paciente="{id}"')
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

    cursor.execute(f'''
        UPDATE pacientes 
        SET nombre="{nuevo_nombre}", apellido_paterno="{nuevo_apellido_paterno}", apellido_materno="{nuevo_apellido_materno}", 
        telefono="{nuevo_telefono}", email="{nuevo_email}", direccion="{nueva_direccion}"
        WHERE id_paciente="{id}"
    ''')
    conexion.commit()  # Aplica los cambios a la base de datos
    print(f"\n{Colors.GREEN}Datos actualizados correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_agregar_nuevo_paciente():
    print(f"\n{Colors.BOLD}Agregar nuevo paciente:\n{Colors.RESET}")
    
    nuevo_nombre = input("Nombre: ")
    nuevo_apellido_paterno = input("Apellido paterno: ")
    nuevo_apellido_materno = input("Apellido materno: ")
    nuevo_telefono = input("Teléfono: ")
    nuevo_email = input("Email: ")
    nueva_direccion = input("Dirección: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    
    # Inserta los datos en la base de datos
    cursor.execute(f'''
        INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, telefono, email, direccion, fecha_nacimiento) 
        VALUES ("{nuevo_nombre}", "{nuevo_apellido_paterno}", "{nuevo_apellido_materno}", "{nuevo_telefono}", "{nuevo_email}", "{nueva_direccion}", "{fecha_nacimiento}")
    ''')
    conexion.commit()  # Aplica los cambios a la base de datos
    print(f"\n{Colors.GREEN}Paciente agregado correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_ver_datos_medicos():
    print(f"\n{Colors.BOLD}Lista de todos los médicos:\n{Colors.RESET}")

    cursor.execute(f'SELECT * FROM medicos')
    resultados = cursor.fetchall()

    if resultados:
        for medico in resultados:
            print(f"ID: {medico[0]}")
            print(f"Nombre: {medico[1]} {medico[2]} {medico[3]}.")
            print(f"Teléfono: {medico[4]}.")
            print(f"Email: {medico[5]}.")
            print(f"{Colors.GREEN}{'-' * 50}{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}No se encontraron médicos en la base de datos.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_buscar_medico_por_id():
    id = input(f"Introduce el ID del médico: {Colors.RESET}")
    
    if not verificarID("2", id):
        print(f"\n{Colors.RED}El médico con ID {id} no existe. Intenta de nuevo.{Colors.RESET}\n")
        return
    
    cursor.execute(f'SELECT * FROM medicos WHERE id_medico="{id}"')
    resultado = cursor.fetchall()
    
    if resultado:
        print(f"\n{Colors.BOLD}Datos del médico:\n{Colors.RESET}")
        print(f"Nombre: {resultado[0][1]} {resultado[0][2]} {resultado[0][3]}.")
        print(f"Teléfono: {resultado[0][4]}.")
        print(f"Email: {resultado[0][5]}.")
    else:
        print(f"\n{Colors.RED}No se encontraron datos para el médico con ID {id}.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_editar_datos_medico():
    id = input(f"Introduce el ID del médico: {Colors.RESET}")
    
    if not verificarID("2", id):
        print(f"\n{Colors.RED}El médico con ID {id} no existe. Intenta de nuevo.{Colors.RESET}\n")
        return
    
    print(f"\n{Colors.BOLD}Editar los datos del médico:\n{Colors.RESET}")
    
    cursor.execute(f'SELECT * FROM medicos WHERE id_medico="{id}"')
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

    cursor.execute(f'''
        UPDATE medicos 
        SET nombre="{nuevo_nombre}", apellido_paterno="{nuevo_apellido_paterno}", apellido_materno="{nuevo_apellido_materno}", 
        telefono="{nuevo_telefono}", email="{nuevo_email}"
        WHERE id_medico="{id}"
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Datos actualizados correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_agregar_nuevo_medico():
    print(f"\n{Colors.BOLD}Agregar nuevo médico:\n{Colors.RESET}")
    
    nuevo_nombre = input("Nombre: ")
    nuevo_apellido_paterno = input("Apellido paterno: ")
    nuevo_apellido_materno = input("Apellido materno: ")
    nuevo_telefono = input("Teléfono: ")
    nuevo_email = input("Email: ")
    
    # Inserta los datos en la base de datos
    cursor.execute(f'''
        INSERT INTO medicos (nombre, apellido_paterno, apellido_materno, telefono, email) 
        VALUES ("{nuevo_nombre}", "{nuevo_apellido_paterno}", "{nuevo_apellido_materno}", "{nuevo_telefono}", "{nuevo_email}")
    ''')
    conexion.commit()  # Aplica los cambios a la base de datos
    print(f"\n{Colors.GREEN}Médico agregado correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_ver_especialidades():
    cursor.execute("SELECT * FROM especialidades")
    resultados = cursor.fetchall()

    if resultados:
        print(f"\n{Colors.BOLD}Especialidades disponibles:\n{Colors.RESET}")
        for especialidad in resultados:
            print(f"ID: {especialidad[0]}, Nombre: {especialidad[1]}")
    else:
        print(f"\n{Colors.RED}No hay especialidades registradas.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_buscar_especialidad_por_id():
    id = input(f"Introduce el ID de la especialidad: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM especialidades WHERE id_especialidad="{id}"')
    resultado = cursor.fetchall()

    if resultado:
        print(f"\n{Colors.BOLD}Datos de la especialidad:\n{Colors.RESET}")
        print(f"ID: {resultado[0][0]}")
        print(f"Nombre: {resultado[0][1]}")
    else:
        print(f"\n{Colors.RED}No se encontró la especialidad con ID {id}.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_editar_especialidad():
    id = input(f"Introduce el ID de la especialidad a editar: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM especialidades WHERE id_especialidad="{id}"')
    resultado = cursor.fetchall()

    if not resultado:
        print(f"\n{Colors.RED}La especialidad con ID {id} no existe.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    print(f"Nombre actual: {resultado[0][1]}")
    nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener el actual): ")
    if nuevo_nombre == "":
        nuevo_nombre = resultado[0][1]

    cursor.execute(f'''
        UPDATE especialidades 
        SET nombre_especialidad="{nuevo_nombre}"
        WHERE id_especialidad="{id}"
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Especialidad actualizada correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_agregar_especialidad():
    nombre = input("Introduce el nombre de la nueva especialidad: ")

    cursor.execute(f'''
        INSERT INTO especialidades (nombre_especialidad) 
        VALUES ("{nombre}")
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Especialidad agregada correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_ver_horarios():
    cursor.execute("SELECT * FROM horarios")
    resultados = cursor.fetchall()

    if resultados:
        print(f"\n{Colors.BOLD}Horarios disponibles:\n{Colors.RESET}")
        for horario in resultados:
            print(f"ID: {horario[0]}, Médico ID: {horario[1]}, Día: {horario[2]}, Inicio: {horario[3]}, Fin: {horario[4]}")
    else:
        print(f"\n{Colors.RED}No hay horarios registrados.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_buscar_horario_por_id():
    id = input(f"Introduce el ID del horario: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM horarios WHERE id_horario="{id}"')
    resultado = cursor.fetchall()

    if resultado:
        print(f"\n{Colors.BOLD}Datos del horario:\n{Colors.RESET}")
        print(f"ID: {resultado[0][0]}")
        print(f"Médico ID: {resultado[0][1]}")
        print(f"Día de la semana: {resultado[0][2]}")
        print(f"Hora inicio: {resultado[0][3]}")
        print(f"Hora fin: {resultado[0][4]}")
    else:
        print(f"\n{Colors.RED}No se encontró el horario con ID {id}.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_editar_horario():
    id = input(f"Introduce el ID del horario a editar: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM horarios WHERE id_horario="{id}"')
    resultado = cursor.fetchall()

    if not resultado:
        print(f"\n{Colors.RED}El horario con ID {id} no existe.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    print(f"Día actual: {resultado[0][2]}")
    nuevo_dia = input("Nuevo día (dejar vacío para mantener el actual): ")
    if nuevo_dia == "":
        nuevo_dia = resultado[0][2]

    print(f"Hora de inicio actual: {resultado[0][3]}")
    nueva_hora_inicio = input("Nueva hora de inicio (dejar vacío para mantener la actual): ")
    if nueva_hora_inicio == "":
        nueva_hora_inicio = resultado[0][3]

    print(f"Hora de fin actual: {resultado[0][4]}")
    nueva_hora_fin = input("Nueva hora de fin (dejar vacío para mantener la actual): ")
    if nueva_hora_fin == "":
        nueva_hora_fin = resultado[0][4]

    cursor.execute(f'''
        UPDATE horarios 
        SET dia_semana="{nuevo_dia}", hora_inicio="{nueva_hora_inicio}", hora_fin="{nueva_hora_fin}"
        WHERE id_horario="{id}"
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Horario actualizado correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_agregar_horario():
    id_medico = input("Introduce el ID del médico: ")
    dia_semana = input("Introduce el día de la semana: ")
    hora_inicio = input("Introduce la hora de inicio (formato HH:MM:SS): ")
    hora_fin = input("Introduce la hora de fin (formato HH:MM:SS): ")

    cursor.execute(f'''
        INSERT INTO horarios (id_medico, dia_semana, hora_inicio, hora_fin) 
        VALUES ("{id_medico}", "{dia_semana}", "{hora_inicio}", "{hora_fin}")
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Horario agregado correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_ver_citas():
    cursor.execute("SELECT * FROM citas")
    resultados = cursor.fetchall()

    if resultados:
        print(f"\n{Colors.BOLD}Citas programadas:\n{Colors.RESET}")
        for cita in resultados:
            print(f"ID: {cita[0]}, Paciente ID: {cita[1]}, Médico ID: {cita[2]}, Horario ID: {cita[3]}, Fecha: {cita[4]}, Hora: {cita[5]}, Descripción: {cita[6]}, Estado: {cita[7]}")
    else:
        print(f"\n{Colors.RED}No hay citas registradas.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def admin_buscar_cita_por_id():
    id = input(f"Introduce el ID de la cita: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM citas WHERE id_cita="{id}"')
    resultado = cursor.fetchall()

    if resultado:
        print(f"\n{Colors.BOLD}Datos de la cita:\n{Colors.RESET}")
        print(f"ID: {resultado[0][0]}")
        print(f"Paciente ID: {resultado[0][1]}")
        print(f"Médico ID: {resultado[0][2]}")
        print(f"Horario ID: {resultado[0][3]}")
        print(f"Fecha: {resultado[0][4]}")
        print(f"Hora: {resultado[0][5]}")
        print(f"Descripción: {resultado[0][6]}")
        print(f"Estado: {resultado[0][7]}")
    else:
        print(f"\n{Colors.RED}No se encontró la cita con ID {id}.{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")



def admin_editar_cita():
    id = input(f"Introduce el ID de la cita a editar: {Colors.RESET}")

    cursor.execute(f'SELECT * FROM citas WHERE id_cita="{id}"')
    resultado = cursor.fetchall()

    if not resultado:
        print(f"\n{Colors.RED}La cita con ID {id} no existe.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    print(f"Fecha actual: {resultado[0][4]}")
    nueva_fecha = input("Nueva fecha (dejar vacío para mantener la actual, formato YYYY-MM-DD): ")
    if nueva_fecha == "":
        nueva_fecha = resultado[0][4]

    print(f"Hora actual: {resultado[0][5]}")
    nueva_hora = input("Nueva hora (dejar vacío para mantener la actual, formato HH:MM:SS): ")
    if nueva_hora == "":
        nueva_hora = resultado[0][5]

    print(f"Descripción actual: {resultado[0][6]}")
    nueva_descripcion = input("Nueva descripción (dejar vacío para mantener la actual): ")
    if nueva_descripcion == "":
        nueva_descripcion = resultado[0][6]

    print(f"Estado actual: {resultado[0][7]}")
    nuevo_estado = input("Nuevo estado (dejar vacío para mantener el actual): ")
    if nuevo_estado == "":
        nuevo_estado = resultado[0][7]

    cursor.execute(f'''
        UPDATE citas 
        SET fecha_cita="{nueva_fecha}", hora_cita="{nueva_hora}", descripcion="{nueva_descripcion}", estado="{nuevo_estado}"
        WHERE id_cita="{id}"
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Cita actualizada correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


def admin_agregar_cita():
    id_paciente = input("Introduce el ID del paciente: ")
    id_medico = input("Introduce el ID del médico: ")
    id_horario = input("Introduce el ID del horario: ")
    fecha_cita = input("Introduce la fecha de la cita (formato YYYY-MM-DD): ")
    hora_cita = input("Introduce la hora de la cita (formato HH:MM:SS): ")
    descripcion = input("Introduce una descripción: ")
    estado = input("Introduce el estado de la cita: ")

    cursor.execute(f'''
        INSERT INTO citas (id_paciente, id_medico, id_horario, fecha_cita, hora_cita, descripcion, estado) 
        VALUES ("{id_paciente}", "{id_medico}", "{id_horario}", "{fecha_cita}", "{hora_cita}", "{descripcion}", "{estado}")
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Cita agregada correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")



##FUNCIONES DE LA OPCION DE MEDICOS
def medico_verdatos(id):
    print(f"\n{Colors.BOLD}Tus datos son los siguientes:\n{Colors.RESET}")
    cursor.execute(f'SELECT * FROM medicos WHERE id_medico="{id}"')
    resultado = cursor.fetchall()
    print(f"Tu {Colors.CYAN}nombre{Colors.RESET} es {resultado[0][1]} {resultado[0][2]} {resultado[0][3]}.")
    print(f"Tu {Colors.CYAN}telefono{Colors.RESET} es {resultado[0][4]}.")
    print(f"Tu {Colors.CYAN}email{Colors.RESET} es {resultado[0][5]}.")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presionar la tecla ENTER para continuar...\n{Colors.RESET}")
    
def medico_editardatos(id):
    print(f"\n{Colors.BOLD}Editar tus datos:\n{Colors.RESET}")
    
    cursor.execute(f'SELECT * FROM medicos WHERE id_medico="{id}"')
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

    # Ejecuta la consulta de actualización
    cursor.execute(f'''
        UPDATE medicos 
        SET nombre="{nuevo_nombre}", apellido_paterno="{nuevo_apellido_paterno}", apellido_materno="{nuevo_apellido_materno}", 
        telefono="{nuevo_telefono}", email="{nuevo_email}"
        WHERE id_medico="{id}"
    ''')
    conexion.commit()
    print(f"\n{Colors.GREEN}Datos actualizados correctamente.{Colors.RESET}")
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
    
def medico_vercitas(id):
    print(f"\n{Colors.BOLD}Tus citas programadas:\n{Colors.RESET}")
    cursor.execute(f'SELECT * FROM citas WHERE id_medico="{id}"')
    resultados = cursor.fetchall()

    if not resultados:
        print(f"{Colors.RED}No tienes citas programadas.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    for c, fila in enumerate(resultados, start=1):
        idPaciente = fila[2]
        fechaCita = fila[4]
        horaCita = fila[5]
        descripcion = fila[6]
        estadoCita = fila[7]

        cursor.execute(f'SELECT * FROM pacientes WHERE id_paciente="{idPaciente}"')
        resultadoPaciente = cursor.fetchone()
        nombrePaciente = f"{resultadoPaciente[1]} {resultadoPaciente[2]} {resultadoPaciente[3]}" if resultadoPaciente else "Desconocido"
        
        print(f"Cita N-{c}: Paciente: {nombrePaciente}, Fecha: {fechaCita}, Hora: {horaCita}, Descripción: {descripcion}, Estado: {estadoCita}")
    
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
    
def medico_verpacientes(id):
    print(f"\n{Colors.BOLD}Tus pacientes actuales:\n{Colors.RESET}")
    cursor.execute(f'SELECT DISTINCT id_paciente FROM citas WHERE id_medico="{id}"')
    resultados = cursor.fetchall()

    if not resultados:
        print(f"{Colors.RED}No tienes pacientes asignados.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    for c, fila in enumerate(resultados, start=1):
        idPaciente = fila[0]
        cursor.execute(f'SELECT * FROM pacientes WHERE id_paciente="{idPaciente}"')
        resultadoPaciente = cursor.fetchone()
        nombrePaciente = f"{resultadoPaciente[1]} {resultadoPaciente[2]} {resultadoPaciente[3]}" if resultadoPaciente else "Desconocido"

        print(f"Paciente N-{c}: {nombrePaciente}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
    
def medico_verespecialidad(id):
    
    # Realizamos una consulta con JOIN para obtener el nombre de la especialidad del médico
    cursor.execute(f'''
        SELECT especialidades.nombre_especialidad 
        FROM medicos 
        JOIN especialidades 
        ON medicos.id_especialidad = especialidades.id_especialidad 
        WHERE medicos.id_medico = "{id}"
    ''')
    
    resultado = cursor.fetchone()  # Usamos fetchone para obtener solo un resultado

    if resultado:
        print(f"\n{Colors.BOLD}Tu especialidad es: {Colors.CYAN}{resultado[0]}{Colors.RESET}")
    else:
        print(f"{Colors.RED}No se encontró especialidad registrada para este médico.{Colors.RESET}")
    
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


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
    print(f"\n{Colors.BOLD}Tus citas programadas:\n{Colors.RESET}")
    cursor.execute(f'SELECT * FROM citas WHERE id_paciente="{id}"')
    resultados = cursor.fetchall()

    if not resultados:
        print(f"{Colors.RED}No tienes citas programadas.{Colors.RESET}")
        input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")
        return

    c = 0
    for fila in resultados:
        c += 1
        idCita = fila[0]
        idMedico = fila[1]
        fechaCita = fila[4]
        horaCita = fila[5]
        descripcion = fila[6]
        estadoCita = fila[7]

        # Obtener información del médico
        cursor.execute(f'SELECT * FROM medicos WHERE id_medico="{idMedico}"')
        resultadoMedico = cursor.fetchone()
        if resultadoMedico:
            nombreMedico = f"{resultadoMedico[1]} {resultadoMedico[2]} {resultadoMedico[3]}"
        else:
            nombreMedico = "Información del médico no disponible"

        print(f"Consulta N-{c}: La fecha de la cita está programada para el día {fechaCita} a la hora {horaCita}, la descripción de la cita es {Colors.YELLOW}{descripcion}{Colors.RESET}, el médico es {nombreMedico} y el estado de la cita es {Colors.GREEN}{estadoCita}{Colors.RESET}")

    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")

def paciente_agendarcita(id):
    print(f"\n{Colors.BOLD}Agendar una nueva cita:\n{Colors.RESET}")

    # Listar médicos disponibles
    cursor.execute("SELECT id_medico, nombre, apellido_paterno FROM medicos")
    medicos = cursor.fetchall()
    print("\nMédicos disponibles:")
    for medico in medicos:
        print(f"{medico[0]} - Dr. {medico[1]} {medico[2]}")
    
    id_medico = input("\nIngresa el ID del médico con el que deseas agendar la cita: ")

    # Verificar si el médico existe
    cursor.execute(f"SELECT * FROM medicos WHERE id_medico = {id_medico}")
    if not cursor.fetchall():
        print(f"\n{Colors.RED}El ID del médico no es válido. Intenta de nuevo.{Colors.RESET}")
        return

    # Obtener los horarios del médico seleccionado
    cursor.execute(f"SELECT id_horario, dia_semana, hora_inicio, hora_fin FROM horarios WHERE id_medico = {id_medico}")
    horarios = cursor.fetchall()

    if not horarios:
        print(f"\n{Colors.RED}No hay horarios disponibles para el médico seleccionado.{Colors.RESET}")
        return

    print(f"\nHorarios disponibles para el médico {id_medico}:")
    for horario in horarios:
        print(f"{horario[0]} - {horario[1]} de {horario[2]} a {horario[3]}")
    
    id_horario = input("\nSelecciona el ID del horario que prefieras: ")

    # Verificar si el horario seleccionado es válido
    cursor.execute(f"SELECT * FROM horarios WHERE id_horario = {id_horario}")
    if not cursor.fetchall():
        print(f"\n{Colors.RED}El ID del horario no es válido. Intenta de nuevo.{Colors.RESET}")
        return

    # Verificar si ya existe una cita en ese horario
    fecha = input("\nFecha de la cita (YYYY-MM-DD): ")
    hora = input("Hora de la cita (HH:MM): ")

    # Verificar el formato de la fecha y hora
    try:
        import datetime
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        datetime.datetime.strptime(hora, "%H:%M")
    except ValueError:
        print(f"\n{Colors.RED}La fecha o la hora tienen un formato incorrecto.{Colors.RESET}")
        return

    cursor.execute(f"""
        SELECT * FROM citas 
        WHERE id_medico = {id_medico} 
        AND id_horario = {id_horario} 
        AND fecha_cita = '{fecha}' 
        AND hora_cita = '{hora}'
    """)
    cita_existente = cursor.fetchall()

    if cita_existente:
        print(f"\n{Colors.RED}Lo siento, ya existe una cita programada para este médico en este horario y fecha.{Colors.RESET}")
    else:
        descripcion = input("\nDescripción de la cita o condición del paciente: ")

        # Insertar la nueva cita en la base de datos
        try:
            cursor.execute(f'''
                INSERT INTO citas (id_paciente, id_medico, id_horario, fecha_cita, hora_cita, descripcion, estado)
                VALUES ("{id}", "{id_medico}", "{id_horario}", "{fecha}", "{hora}", "{descripcion}", "Pendiente")
            ''')
            conexion.commit()  # Aplicar los cambios en la base de datos
            print(f"\n{Colors.GREEN}Cita agendada correctamente para el {fecha} a las {hora} con el médico {id_medico}.{Colors.RESET}")
        except Error as e:
            print(f"\n{Colors.RED}Error al agendar la cita: {e}{Colors.RESET}")
    
    input(f"\n{Colors.GREEN}{Colors.BOLD}Presiona la tecla ENTER para continuar...\n{Colors.RESET}")


##LLAMADO DE FUNCIONES
menu()