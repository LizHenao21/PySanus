# -*- coding: utf-8 -*-
"""Original file is located at
    https://colab.research.google.com/drive/1sHwxhmn1dM_nP7Jc7KBeCMIIXiOcR8ag

<div align="center">
<table>
    <thead>
        <tr>
            <td rowspan="3">
                <img alt="UdeA" height="200px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/Escudo-UdeA.svg" hspace="10px" vspace="0px">
            </td>
            <td align="center">
                <h1><b>Programación y Algoritmia</b></h1>
            </td>
            <td rowspan="3">
                <img alt="II" height="200px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Ingenier%C3%ADa_Industrial_UdeA.png/1026px-Ingenier%C3%ADa_Industrial_UdeA.png" hspace="0px" vspace="0px">
            </td>
        </tr>
        <tr>
            <td>
                <h1><b>Trabajo Final</b></h1>
            </td>
        </tr>
        <tr>
            <td>
                <img align="center" alt="I&S" height="135px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/IS.png" hspace="10px" vspace="0px">
            </td>
        </tr>
    </thead>
</table>

</div>

<hr size=10 noshade color="green">
<p>
<img alt="CC" height="70px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/by.xlarge.png" align="left" hspace="0px" vspace="0px">
<img alt="Attribution" height="70px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/nc.xlarge.png" align="left" hspace="0px" vspace="0px">
<img alt="NC" height="70px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/sa.xlarge.png" align="left" hspace="0px" vspace="0px">
<img alt="SA" height="70px" src="https://raw.githubusercontent.com/juliancastillo-udea/2024-1-ProgramacionPosgrados/main/images/cc-icons.png" align="left" hspace="0px" vspace="0px">
</p>

<div align="right">
<h2> <b> Por: Julián Andrés Castillo G. </b> </h2>
<a href="mailto:jandres.castillo@udea.edu.co"> ✉ Julian Andres Castillo Grisales </a>
<h2> <b> Por: Yony Fernando Ceballos. </b> </h2>
<a href="mailto:yony.ceballos@udea.edu.co"> ✉ Yony Fernando Ceballos </a>
</div>

<br>

# **Descripción del problema a solucionar -Software gestión turnos**

La EPS PailaSalud está interesada en crear un programa para la gestión de turnos y atenciones debido a que actualmente el procedimiento se realiza manualmente en donde los pacientes deben estar sentados y esperando el servicio, sin ningún tipo de atención preferencial o clasificada. Este procedimiento afecta el rendimiento del servicio y afecta el desempeño de la atención.

Para solucionar este problema los estudiantes en grupos de máximo tres integrantes, deberán crear un programa que se encargue de gestionar las personas que llegan a la EPS, producto de las citas programadas que dispone el servicio de la EPS. El software debe encargarse tanto de su llegada como de su recorrido por el sistema. El listado de las personas será proporcionado por un programa creado por la EPS (el docente entrega este programa para su uso) en un repositorio de GitHub sobre el cual los estudiantes deben hacer un clon del repositorio y continuar con su proyecto desde este punto de partida.

# **El software de la EPS para las citas**

La EPS Paila Salud, tiene un sistema de asignación de citas el cual recibe la solicitud de cita de los pacientes y registra su día, horario, tipo de cita, médico y la información personal del paciente. Este listado será proporcionado por una función del repositorio inicial.

# **Objetivo**

Crear un programa de consola visualmente amigable al usuario, en donde permita gestionar la atención de los pacientes y registrar los datos en un dataframe , para posteriormente exportar la atención en un archivo plano (CSV) usando Python y la gestión de dos documentos. Uno proporcionado por el repositorio inicial y otro creado por el estudiante para entregar una carpeta con los listados de pacientes.

# **Reglas**

## Actas de entendimiento y compromiso.

Los integrantes del grupo deben definir su participación y responsabilidad mediante actas de entendimiento. Estas se describen a continuación:
*   ### Objetivo de entendimiento y compromiso
>Este procedimiento tiene como objetivo establecer las normas y directrices para la creación de actas de entendimiento, colaboración y responsabilidad en trabajos grupales académicos. Busca promover un ambiente de trabajo colaborativo y respetuoso, asegurando que todos los miembros del grupo comprendan y acuerden sus roles y responsabilidades.

*   ### Alcance
>Este procedimiento aplica a todos los estudiantes vinculados a un equipo para la entrega del trabajo final.
>*  #### Definiciones (Entregables)
>>*   Acta de Entendimiento: Documento que detalla los objetivos comunes del grupo y las expectativas de cada miembro respecto al proyecto.
>>*   Acta de Colaboración: Documento que especifica las metodologías de trabajo en equipo, incluyendo estrategias de comunicación y resolución de conflictos.
>>*   Acta de Responsabilidad: Documento que asigna tareas específicas a cada miembro del grupo, estableciendo plazos y criterios de evaluación.
Procedimientos (Entregables)
>>*   Convocatoria de Reunión: El grupo deberá convocar a una reunión inicial para discutir los objetivos del proyecto y elaborar el Acta de Entendimiento.
>>*   Elaboración del Acta de Entendimiento: Durante la reunión, los miembros del grupo discutirán y acordarán los objetivos y expectativas del proyecto. Esta acta será redactada por un miembro designado y luego revisada y firmada por todos los integrantes.
>>*   Elaboración del Acta de Colaboración: Posteriormente, se redactará el Acta de Colaboración, donde se definirán las normas de trabajo en equipo, incluyendo los canales y frecuencia de comunicación.
>>*   Asignación de Responsabilidades: Finalmente, se creará el Acta de Responsabilidad, detallando las tareas específicas de cada miembro, así como los plazos de entrega. Cada miembro del grupo deberá firmar este documento, aceptando sus responsabilidades.
>*  #### Seguimiento y Evaluación (Entregables)
>>*   Reuniones de Seguimiento: El grupo deberá realizar reuniones periódicas para evaluar el progreso del proyecto y hacer ajustes necesarios en las actas.
>>*   Revisión de Actas: Las actas pueden ser revisadas y modificadas con el consentimiento de todos los miembros del grupo, según sea necesario para reflejar cambios en el proyecto o en la dinámica del equipo.
>*  #### Resolución de Conflictos
>>*   En caso de desacuerdos o conflictos, el grupo deberá referirse al Acta de Colaboración para resolver la situación mediante los mecanismos previamente acordados. Si no se llega a una resolución, se consultará con el del curso para mediación.

# **Entregables**

El entregable debe ser realizado en un repositorio de GitHub y debidamente organizado con todos los elementos de Markdown necesarios para establecer una jerarquía como un documento escrito.
El repositorio debe tener lo siguientes procesos debidamente reportados.

## **1.   Integrantes**
En el repositorio del proyecto debe existir un archivo README.md en donde con Markdown detalle los nombres de los integrantes y una breve descripción.

Lizeth Natalia Henao Pinzon,
Juan José Passos Marín

## **2.	Vínculos académicos y descripción**

Todos los integrantes deben registrar el programa al cual pertenece, una descripción con habilidades y fortalezas de cada uno.

`Registrar los vínculos académicos y descripcion de cada uno aquí`

## **3.	Nombre del proyecto y detalles**

**PySanus:** Diseñar un programa que sirva para la asignación de citas medicas de los pacientes de la EPS Paila salud, donde se identifique el tipo de cita: si es con medico general o con especialista, el medico, información del paciente y además si este requiere atención preferencial o prioritaria.
"""

from google.colab import drive
from IPython.display import Image

# Montar Google Drive
drive.mount('/content/drive')

# Especificar la ruta completa de la imagen en Google Drive
ruta_imagen = "/content/drive/My Drive/3 SEMESTRE/Algoritmia y Programación/ENTREGA 1/Logo.jpg"

# Mostrar la imagen
Image(ruta_imagen, width=300)

"""## **4.	Licencia del software**

Definir la licencia con la cual registra el software. https://chooser-beta.creativecommons.org/

<p xmlns:cc="http://creativecommons.org/ns#" >Este trabajo está licenciado bajo <a href="https://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0<img style="height:22px!¡importante;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!¡importante;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!importante;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.¿svg?ref=chooser-v1" alt=""></a></p>

## **5.	Reporte de visión**

Proporciona una descripción general del software, sus objetivos y beneficios.

`Ingresar el reporte de visión aquí`

## **6.	Especificación de requisitos**

Describe los requisitos funcionales y no funcionales del software.
*   Los requisitos funcionales definen las acciones específicas, comportamientos, y operaciones que el software debe ejecutar para satisfacer las necesidades del usuario final.
*   Los requisitos no funcionales especifican criterios que pueden usarse para juzgar la operación del sistema, más allá de los comportamientos específicos. Esto incluye aspectos como el rendimiento, seguridad, usabilidad, fiabilidad, y compatibilidad.

`Ingresar la especificación de requisitos aquí`

## **7.	Plan de proyecto**

Describe las actividades, el cronograma (Diagrama de Gantt) y el presupuesto del proyecto.
*   El presupuesto debe tener en cuenta que no se pagará en dinero sino en tiempo de práctica de formación. Es decir, si el grupo del trabajo final lo componen tres estudiantes e invierten un total de 50 horas, estas serán pagadas a valor de práctica profesional. 1 SMLV.

`Ingresar el plan del proyecto aquí`
"""

import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Tarea="Versiones del programa", FechaInicio='2024-08-01', FechaFin='2024-11-08', Responsable="Juan Passos"),
    dict(Tarea="Carpeta de repositorio", FechaInicio='2024-09-18', FechaFin='2024-09-21', Responsable="Lizeth Henao"),
    dict(Tarea="Código de programa", FechaInicio='2024-09-26', FechaFin='2024-11-08', Responsable="Lizeth y Juan"),
    dict(Tarea="Revisiones y correcciones", FechaInicio='2024-09-26', FechaFin='2024-11-08', Responsable="Lizeth y Juan"),
    dict(Tarea="Criterios de Manual", FechaInicio='2024-10-09', FechaFin='2024-10-12', Responsable="Lizeth Henao"),
    dict(Tarea="Redacción de Manual", FechaInicio='2024-10-13', FechaFin='2024-10-18', Responsable="Lizeth y Juan"),
    dict(Tarea="Revisión de Manual", FechaInicio='2024-11-18', FechaFin='2024-11-20', Responsable="Juan Passos"),
    dict(Tarea="Última prueba de programa", FechaInicio='2024-11-21', FechaFin='2024-11-22', Responsable="Juan Passos"),
    dict(Tarea="Entrega de Proyecto", FechaInicio='2024-11-23', FechaFin='2024-11-23', Responsable="Lizeth Henao")
])

fig = px.timeline(df, x_start="FechaInicio", x_end="FechaFin", y="Responsable", color="Responsable")
fig.show()

# @markdown ### Usar el código a continuación para crear el diagrama de Gantt por Tarea
df = pd.DataFrame([
    dict(Tarea="1.Versiones del programa", FechaInicio='2024-09-26', FechaFin='2024-11-08', Responsable="Juan Passos"),
    dict(Tarea="2.Carpeta de repositorio", FechaInicio='2024-09-18', FechaFin='2024-09-21', Responsable="Lizeth Henao"),
    dict(Tarea="3.Código de programa", FechaInicio='2024-09-26', FechaFin='2024-11-08', Responsable="Lizeth y Juan"),
    dict(Tarea="4.Pruebas y correcciones", FechaInicio='2024-09-26', FechaFin='2024-11-08', Responsable="Lizeth y Juan"),
    dict(Tarea="5.Criterios de Manual", FechaInicio='2024-11-09', FechaFin='2024-11-12', Responsable="Lizeth Henao"),
    dict(Tarea="6.Redacción de Manual", FechaInicio='2024-11-13', FechaFin='2024-11-18', Responsable="Lizeth y Juan"),
    dict(Tarea="7.Revisión de Manual", FechaInicio='2024-11-18', FechaFin='2024-11-20', Responsable="Juan Passos"),
    dict(Tarea="8.Última prueba de programa", FechaInicio='2024-11-21', FechaFin='2024-11-22', Responsable="Juan Passos"),
    dict(Tarea="9.Entrega de Proyecto", FechaInicio='2024-11-23', FechaFin='2024-11-24', Responsable="Lizeth Henao")
])
df = df.sort_values(by='Tarea')
fig = px.timeline(
    df,
    x_start="FechaInicio",
    x_end="FechaFin",
    y="Tarea",
    color='Responsable',
    category_orders={'Tarea': sorted(df['Tarea'].tolist(), reverse=True)}  # Ordenar las tareas alfabéticamente
)
fig.update_yaxes(autorange="reversed")
fig.show()

"""## **8.	Versionado del software**

Describe las versiones del software y su avance cada que se realice un procedimiento relevante en días desde el inicio hasta la entrega final.

`Ingresar el plan del versionado aquí`

## **9.	Algoritmo**

Una carpeta en el repositorio en GitHub con todos los archivos y código utilizados en el proyecto.

`Describir el algoritmo aquí`

## **10.	Manual de usuario**

Una carpeta en el repositorio en GitHub registrar el manual de uso del programa.

`Escribir el manual de usuario aquí`

# **GitHub**
El líder del equipo debe crear una cuenta en GitHub y cargar los documentos previamente detallados en la entrega vincular a los compañeros en un repositorio compartido (Lo necesario para cargar en GitHub será explicado en clase).

## **Fechas y documentos**
*   Entrega 1: Para la primera entrega se debe enviar los puntos 1 a 7 --> Semana 8 (29 de septiembre).
*   Entrega 2: Todo lo descrito en el presente documento. --> Semana 16

---

# **Solución**

## **Librerías necesarias**
"""

# @markdown ## **Ejecutar esta celda (►)**
# @markdown
# @markdown Doble clic en mí y podrás ver mi código.
# =====================================================================================================================
# REGION: Congiguración de la consola
# =====================================================================================================================
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
TemaAnalisisDatos = Theme({
    "info": "bold navy_blue on grey82",
    "url": "underline blue",
    "warning": "dark_orange",
    "danger": "bold red",
    "normalb": "bold black",
    "normal": "black"
}, inherit=False)
console = Console(theme=TemaAnalisisDatos)
# =====================================================================================================================
# REGION: Librerías
# =====================================================================================================================
with console.status("Cargando Librerías", spinner="clock"):
    import os
    import random as rnd
    import pandas as pd
    import time
    import logging
    import tqdm
    import rich
    import numpy as np
    import matplotlib.pyplot as plt
    import statistics as st
    import math as mt
    # from google.colab import drive
    import sys
    import datetime
    import time
    from tqdm import tqdm
    #import ace_tools as tools
    from collections import Counter
    inicio = time.time()
    import warnings
    # Ignorar todos los warnings
    warnings.filterwarnings("ignore")
# =====================================================================================================================
# REGION: Librerías
# =====================================================================================================================
console.print("Librerías cargadas satisfactoriamente", style="info")

"""## **Funciones utilizadas en la configuración inicial**"""

# @markdown ## **Ejecutar esta celda (►)**
# @markdown
# @markdown Doble clic en mí y podrás ver mi código.
# =====================================================================================================================
# REGION: Funciones Útiles para Taller Proyecto Integrador
# NOTA: Las funciones fueron comentadas con GitHub Copilot
# =====================================================================================================================
def GenerarNombre(Nombres: list, Apellidos: list) -> str:
    """
    Genera un nombre completo seleccionando aleatoriamente un nombre y un apellido de las listas proporcionadas.

    Args:
        Nombres (list): Lista de nombres posibles.
        Apellidos (list): Lista de apellidos posibles.

    Returns:
        str: Un nombre completo en el formato 'Nombre Apellido'.
    """
    Nombre = rnd.choice(Nombres)
    Apellido = rnd.choice(Apellidos)
    return f'{Nombre} {Apellido}'

def GenerarEdad() -> int:
    """
    Genera una edad aleatoria basada en probabilidades predefinidas.

    Returns:
        int: Una edad aleatoria en uno de los siguientes rangos:
             - 16 a 25 años (50% de probabilidad)
             - 26 a 33 años (25% de probabilidad)
             - 34 a 40 años (15% de probabilidad)
             - 41 a 105 años (10% de probabilidad)
    """
    r = rnd.random()
    if r < 0.5:
        return rnd.randint(16, 25)
    elif r < 0.75:
        return rnd.randint(26, 33)
    elif r < 0.9:
        return rnd.randint(34, 40)
    else:
        return rnd.randint(41, 105)

def GenerarHoraAtencion_Lista() -> list:
    """
    Genera una lista de posibles horas de atención en intervalos de 20 minutos.

    Returns:
        list: Una lista de listas, donde cada sublista contiene una hora y un minuto en el formato [hora, minuto].
              Las horas van de 7 a 18 (inclusive) y los minutos pueden ser 0, 20 o 40.
    """
    horas = [x for x in range(7,19)]
    minutos = [0,20,40]
    citas_list = []
    for hora in horas:
        for minuto in minutos:
            citas_list.append([hora,minuto])
    return citas_list

def GenerarHoraAtencion_str() -> list:
    """
    Genera una lista de posibles horas de atención en formato de cadena.

    Returns:
        list: Una lista de cadenas, donde cada cadena representa una hora de atención en el formato "HH:MM".
              Las horas van de 7 a 18 (inclusive) y los minutos pueden ser 0, 20 o 40.
    """
    horas = [x for x in range(7,19)]
    minutos = [0,20,40]
    citas_list = []
    citas_str = []
    for hora in horas:
        for minuto in minutos:
            citas_list.append([hora,minuto])
    for hora, minuto in citas_list:
        citas_str.append(datetime.time(hora, minuto).strftime("%H:%M"))
    return citas_str

def SiguienteSemana():
    """
    Calcula las fechas de la próxima semana (de lunes a domingo) a partir de la fecha actual.

    Returns:
        list: Una lista de cadenas, donde cada cadena representa una fecha de la próxima semana en el formato "YYYY-MM-DD".
    """
    hoy = datetime.date.today()
    dia_semana = hoy.weekday()
    diferencia = (0 - dia_semana) % 7
    # Sumamos la diferencia a la fecha actual
    semana = []
    semana.append(str(hoy + datetime.timedelta(days=diferencia)))
    for i in range(1,7):
        semana.append(str(hoy + datetime.timedelta(days=diferencia+i)))
    return semana

"""## **Gestión de datos, log de eventos, creación de dataframe y exportar**"""



# =====================================================================================================================
# REGION: Log
# =====================================================================================================================
console.print(f'{"Inicio del proceso"}', style="info")
console.print(f'\t{"Log"}', style="danger")
inicio = time.time() #Inicio contador de ejecucion
hoy = datetime.date.today().strftime('%Y%m%d') #Captura de fecha de ejecucion
nombre_archivo_log = f"log_{hoy}.log" # Inicializacion del log
#Configuracion de almacenamiento y niveles del log
logging.basicConfig(filename=nombre_archivo_log, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') #Podemos manipular el mensaje
#Primer registro del log
logging.info(f"Iniciando el proceso del log __{hoy}__ ")
# =====================================================================================================================
# REGION: Ubicacion y registro de archivos
# =====================================================================================================================
#Creamos el directorio (carpeta) en donde se crearan los archivos
console.print(f'\t{"Ubicacion y registro de archivos"}', style="danger")
DirectorioActual = os.getcwd() #Directorio actual de trabajo
textemp = f'El directorio actual de trabajo es: \n\t--> {DirectorioActual}, \nEsta carpeta contendrá los archivos del trabajo final'
logging.info(textemp) #Registro del directorio actual
#Creamos una carpeta donde almacenamos los resultados
CarpetaNueva = "CarpetaArchivosTrabajoFinal"
os.makedirs(CarpetaNueva, exist_ok=True) #Creamos la carpeta si no existe
logging.info("Se crea el directorio {}".format(CarpetaNueva)) #Registro de la creacion de la carpeta
# Nombre de la carpeta donde se crearán los archivos
carpeta = os.path.join(DirectorioActual, "CarpetaArchivosTrabajoFinal") #Ruta de la carpeta
logging.info("La ruta de trabajo será {}".format(carpeta)) #Registro de la ruta de trabajo
#Usamos los datos de GitHub con nombres y apellidos para leerlos.
RutaNombres = r'https://raw.githubusercontent.com/juliancastillo-udea/AlDiSi/main/Data/NombresArgentina.csv'
RutaApellidos = r'https://raw.githubusercontent.com/juliancastillo-udea/AlDiSi/main/Data/ApellidosArgentina.csv'
# =====================================================================================================================
# REGION: Creando datos genericos
# =====================================================================================================================
console.print(f'\t{"Creando datos genericos"}', style="danger")
logging.info("Cargando CSV con nombres")
dfNombres = pd.read_csv(RutaNombres, encoding='ISO-8859-1')
Nombres = dfNombres['name'].tolist()
logging.info("Reemplazando nombres y detalles del documento")
for i in tqdm(range(len(Nombres)), '\tProcesando nombres'):
    if ' ' in Nombres[i]:
        Nombres[i]=Nombres[i].replace(' ', '_')
logging.info("Cargando CSV con apellidos")
dfApellidos = pd.read_csv(RutaApellidos, encoding='ISO-8859-1')
Apellidos = dfApellidos['lastname'].tolist()
logging.info("Reemplazando apellidos y detalles del documento")
for i in tqdm(range(len(Apellidos)), '\tProcesando apellidos'):
    if ' ' in Apellidos[i]:
        Apellidos[i]=Apellidos[i].replace(' ', '_')
logging.info("Finalizado proceso de gestion de nombres y apellidos")
# endregion Gestion de archivos y ubicaciones
logging.info("Creando secuencia de citas")
horarioatencion = GenerarHoraAtencion_str()
semana = SiguienteSemana()
citas = []
for dia in semana:
    for cita in horarioatencion:
        citas.append(dia+'|'+cita)
# =====================================================================================================================
# REGION: Creacion del dataframe
# =====================================================================================================================
console.print(f'\t{"Creacion del dataframe"}', style="danger")
logging.info("Creando DataFrame con datos de citas y personas")
df = pd.DataFrame(columns=['Nombre', 'Edad', 'Fecha', 'CitaAtencion'])
for cita in citas:
    nombre = GenerarNombre(Nombres, Apellidos).upper()
    edad = GenerarEdad()
    fecha = datetime.date.today().strftime('%Y-%m-%d')
    atencion = cita
    vector = [nombre, edad, fecha, atencion]
    df.loc[len(df)] = vector
logging.info("finalizado proceso de creacion de dataframe")
fin = time.time()
delta = fin-inicio
console.print(f'\t{"Fin dataframe"}', style="danger")
minutos, segundos = divmod(delta, 60)

console.print(f'\tTiempo de ejecucion: {int(minutos)} minutos y {segundos:.2f} segundos', style="url")
logging.info("Exportar DataFrame a Excel y CSV")
df.to_excel(os.path.join(carpeta,'Citas.xlsx'))
df.to_csv(os.path.join(carpeta,'Citas.csv'))
logging.info("Finalizado")
console.print(f'{"Fin del proceso"}', style="info")
# =====================================================================================================================
# REGION: Fin
# =====================================================================================================================

from google.colab import drive
drive.mount('/content/drive')

df.to_excel('basedatos.xlsx')

"""Mi programa comienza aquí"""

import pandas as pd
from google.colab import drive

#Archivo de Drive
drive.mount('/content/drive')
archivo_csv = '/content/CarpetaArchivosTrabajoFinal/Citas.csv'
df = pd.read_csv(archivo_csv)

#Obtener citas de usuarios
citas_usuarios = {}
for index, row in df.iterrows():
    citas_usuarios[row['Nombre']] = {'fecha': row['CitaAtencion']}

#Menús
menuprincipal = [
    'Bienvenido a la EPS Paila Salud',
    'Por favor selecciona una de las opciones disponibles',
    ' ',
    '1. Administrador 💻',
    '2. Usuario 👩‍⚕️',
    '3. Salir 🚪'
]

menuadmin = [
    'Bienvenido administrador',
    '1. Reportes 📋',
    '2. Añadir admin ➕',
    '3. Eliminar admin ❌',
    '4. Añadir cita a usuario 📅',
    '5. Eliminar cita de usuario ❌',
    '6. Salir 🚪'
]

menusuario = [
    'Bienvenido usuario',
    '1. Confirmar cita ✅',
    '2. Cancelar cita ❌',
    '3. Salir 🚪'
]

#Diccionario de usuarios y contraseñas
usuarios = {
    'admin': '123',
    'goku': '777',
    'gohan': '444'
}

#Reportes admin
citas = {
    'confirmadas': 0,
    'canceladas': 0
}

#Intentos fallidos
intentos_fallidos = {
    'admin': 0,
    'goku': 0,
    'gohan': 0
}

#Función para imprimir el menú con formato
def imprimir_menu(menu):
    print('*' * 64)
    for opcion in menu:
        print(opcion.center(64))
    print('*' * 64)

#Función para el menú principal
def menu_principal():
    while True:
        imprimir_menu(menuprincipal)
        opcion = input('Ingresar la opción del menú: ')

        if opcion == '1':  # Administrador
            if autenticar_admin():  #Verificar el usuario y la contraseña
                menu_administrador()
        elif opcion == '2':  #Usuario
            menu_usuario()
        elif opcion == '3':  #Salir
            print('Gracias por usar nuestros servicios. ¡Esperamos su regreso!')
            break
        else:
            print('Opción no disponible, vuelva a intentarlo.')

#Función para autenticar al administrador
def autenticar_admin():
    print('Bienvenido administrador, por favor ingresar usuario y contraseña')
    usuario = input('Ingresar usuario: ')
    contrasenia = input('Ingresar contraseña: ')

    if usuario in usuarios and usuarios[usuario] == contrasenia:
        print('*' * 64)
        print(f'Bienvenido administrador {usuario}')
        print('*' * 64)
        return True
    else:
        print('Usuario o contraseña inválidos')
        return False

#Función para el menú del administrador
def menu_administrador():
    while True:
        imprimir_menu(menuadmin)
        opcion = input('Ingresar opción: ')

        if opcion == '1':  #Reportes
            print_reportes()
        elif opcion == '2':  # Añadir usuario admin
            añadir_admin()
        elif opcion == '3':  # Eliminar usuario admin
            eliminar_admin()
        elif opcion == '4':  # Añadir cita a usuario
            añadir_cita_usuario()
        elif opcion == '5':  # Eliminar cita de usuario
            eliminar_cita_usuario()
        elif opcion == '6':  # Salir
            print('Gracias, que tenga buen día.')
            break
        else:
            print('Opción inválida, intente nuevamente.')

#Función para mostrar los reportes
def print_reportes():
    print('*' * 64)
    print(f'Usuarios registrados: {len(usuarios)}')
    print(f'Citas confirmadas: {citas["confirmadas"]}')
    print(f'Citas canceladas: {citas["canceladas"]}')
    print('*' * 64)

#Función para añadir un usuario admin
def añadir_admin():
    nuevo_admin = input('Ingrese el nombre del nuevo admin: ')
    if nuevo_admin in usuarios:
        print(f'El usuario {nuevo_admin} ya existe.')
    else:
        nueva_contrasenia = input('Ingrese la contraseña para el nuevo admin: ')
        usuarios[nuevo_admin] = nueva_contrasenia
        print(f'Usuario {nuevo_admin} añadido correctamente.')

#Función para eliminar un usuario admin
def eliminar_admin():
    admin_a_eliminar = input('Ingrese el nombre del admin a eliminar: ')
    if admin_a_eliminar in usuarios:
        del usuarios[admin_a_eliminar]
        print(f'Usuario {admin_a_eliminar} eliminado correctamente.')
    else:
        print(f'El usuario {admin_a_eliminar} no existe.')

#Función para añadir una cita a un usuario
def añadir_cita_usuario():
    usuario = input('Ingrese el nombre del usuario: ')
    if usuario in citas_usuarios:
        print(f'El usuario {usuario} ya tiene una cita programada: {citas_usuarios[usuario]["fecha"]}')
    else:
        fecha_cita = input('Ingrese la fecha de la cita (formato YYYY-MM-DD): ')
        hora_cita = input('Ingrese la hora de la cita (formato HH:MM): ')
        citas_usuarios[usuario] = {'fecha': f'{fecha_cita}|{hora_cita}'}
        citas["confirmadas"] += 1
        print(f'Cita para {usuario} añadida correctamente: {fecha_cita} a las {hora_cita}')

#Función para eliminar la cita de un usuario
def eliminar_cita_usuario():
    usuario = input('Ingrese el nombre del usuario: ')
    if usuario in citas_usuarios:
        print(f'Cancelando cita para {usuario}: {citas_usuarios[usuario]["fecha"]}')
        citas["canceladas"] += 1
        del citas_usuarios[usuario]
        print(f'Cita de {usuario} eliminada correctamente.')
    else:
        print(f'El usuario {usuario} no tiene cita programada.')

#Función para el menú del usuario
def menu_usuario():
    while True:
        imprimir_menu(menusuario)
        opcion = input('Ingresar opción: ')

        if opcion == '1':  #Confirmar cita
            confirmar_cita()
        elif opcion == '2':  #Cancelar cita
            cancelar_cita()
        elif opcion == '3':  #Salir
            break
        else:
            print('Opción no disponible, vuelva a intentarlo.')

#Función para confirmar cita
def confirmar_cita():
    usuario = input('Ingrese su nombre de usuario: ')
    if usuario in citas_usuarios:
        print(f'Confirmando cita para {usuario}: {citas_usuarios[usuario]["fecha"]}')
        citas["confirmadas"] += 1
    else:
        print(f'No hay cita programada para {usuario}')

#Función para cancelar cita
def cancelar_cita():
    usuario = input('Ingrese su nombre de usuario: ')
    if usuario in citas_usuarios:
        print(f'Cancelando cita para {usuario}: {citas_usuarios[usuario]["fecha"]}')
        citas["canceladas"] += 1
        del citas_usuarios[usuario]
    else:
        print(f'No hay cita programada para {usuario}')

#Ejecución
menu_principal()
