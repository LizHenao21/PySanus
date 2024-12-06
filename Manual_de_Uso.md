# Manual de Uso del Software: Sistema de Gestión de Citas Pysanus

## 1. Introducción

El Sistema de Gestión de Citas - **Pysanus** es un programa diseñado para gestionar las citas médicas de los usuarios. Ofrece una interfaz intuitiva para administradores y usuarios, permitiendo realizar las siguientes tareas:

- Confirmar y cancelar citas programadas.
- Gestionar cuentas de administrador.
- Generar reportes detallados sobre las actividades del sistema.

El programa utiliza un archivo de datos (`Citas.csv`) para registrar y gestionar las citas de los usuarios.

---

## 2. Inicio del Programa

Cuando inicias el programa, se presenta un menú principal con tres opciones:

1. **Administrador 💻**: Accede a las funcionalidades de administrador, como gestionar usuarios y generar reportes.
2. **Usuario 🧑‍⚕️**: Permite confirmar o cancelar citas programadas.
3. **Salir 🚪**: Cierra el programa.

### Funcionalidad de las opciones:

#### Opción 1: Administrador

Al elegir esta opción, el programa solicita un nombre de usuario y una contraseña. Si las credenciales son correctas, accedes al Menú del Administrador con las siguientes opciones:

1. **Reportes 📋**: Muestra información sobre los usuarios registrados y el estado de las citas (confirmadas y canceladas).
2. **Añadir Admin ➕**: Agrega un nuevo administrador al sistema ingresando un nombre de usuario único y una contraseña.
3. **Eliminar Admin ❌**: Elimina a un administrador existente proporcionando su nombre de usuario.
4. **Salir 🚪**: Regresa al menú principal.

#### Opción 2: Usuario

Al elegir esta opción, el programa presenta un menú con las siguientes funcionalidades:

1. **Confirmar Cita ✅**: Solicita el nombre del usuario, luego busca la cita programada y la marca como "confirmada".
2. **Cancelar Cita ❌**: Solicita el nombre del usuario, muestra la cita programada, elimina la cita del sistema y la marca como "cancelada".
3. **Salir 🚪**: Regresa al menú principal.

---

## 3. Estructura de Datos

El programa utiliza un archivo en formato CSV para registrar y administrar las citas. Este archivo debe contener tres columnas principales:

- **Nombre**: Nombre del usuario registrado.
- **Edad**: Edad del usuario registrado.
- **CitaAtencion**: Fecha y hora de la cita, en el formato `YYYY-MM-DD|HH:MM`.

### Notas:

- Si no existe el archivo `Citas.csv`, el sistema generará automáticamente uno nuevo con datos ficticios.
- El archivo de citas se almacena en la carpeta `CarpetaArchivosTrabajoFinal`, creada automáticamente en el directorio de trabajo.

---

## 4. Funciones Administrativas

### **Reportes**

El administrador puede generar reportes con los siguientes datos:

- **Usuarios registrados**: Muestra el número de administradores registrados en el sistema.
- **Citas confirmadas**: Muestra cuántas citas han sido confirmadas.
- **Citas canceladas**: Muestra cuántas citas han sido canceladas.

### **Añadir un Administrador**

La funcionalidad de añadir un administrador permite incrementar el equipo de usuarios con privilegios administrativos en el sistema. El proceso es el siguiente:

#### Acceso:

1. Desde el Menú Principal, selecciona la opción de "Administrador".
2. Ingresa las credenciales de un administrador existente para autenticarte.

#### Proceso de Adición:

1. Una vez autenticado, selecciona la opción **Añadir Admin ➕** en el Menú del Administrador.
2. El sistema solicitará el nombre de usuario del nuevo administrador.
   - **Requisito**: El nombre debe ser único y no estar registrado previamente en el sistema. Si el nombre ya existe, el sistema mostrará el mensaje:
     > El usuario {nombre} ya existe.
3. A continuación, se pedirá establecer una contraseña para el nuevo administrador.
   - **Recomendación**: Usa una contraseña segura, combinando letras, números y símbolos.
4. Si el nombre y contraseña son válidos, el sistema registrará al nuevo administrador y mostrará el mensaje:
   > Usuario {nombre} añadido correctamente.

#### Consideraciones:

- Este nuevo administrador tendrá acceso a todas las funcionalidades administrativas, incluyendo añadir y eliminar otros administradores.
- Es responsabilidad del equipo asegurar que solo personas autorizadas accedan a esta funcionalidad.

### **Eliminar un Administrador**

La funcionalidad de eliminar un administrador permite retirar los privilegios de administración a un usuario. El proceso es el siguiente:

#### Acceso:

1. Desde el Menú Principal, selecciona la opción de "Administrador".
2. Ingresa las credenciales de un administrador existente para autenticarte.

#### Proceso de Eliminación:

1. Una vez autenticado, selecciona la opción **Eliminar Admin ❌** en el Menú del Administrador.
2. El sistema solicitará el nombre de usuario del administrador que deseas eliminar.
   - **Requisito**: El nombre debe existir en el sistema. Si no existe, el sistema mostrará el mensaje:
     > El usuario {nombre} no existe.
3. Si el nombre es válido, el sistema eliminará al administrador y mostrará el mensaje:
   > Usuario {nombre} eliminado correctamente.

#### Restricciones y Consideraciones:

- **Restricción**: No puedes eliminar al administrador con el que estás autenticado en ese momento.
- Antes de eliminar, asegúrate de que el administrador a retirar no esté gestionando tareas críticas.

---

## 5. Funciones de Usuario

### **Confirmar Cita**

Permite a los usuarios asegurar su asistencia a una cita previamente programada. El proceso es el siguiente:

1. Desde el Menú Principal, selecciona la opción **Usuario**.
2. Una vez dentro del Menú del Usuario, selecciona la opción **Confirmar Cita ✅**.
3. El sistema solicitará ingresar el nombre del usuario. Este debe coincidir exactamente con el registrado en el archivo `Citas.csv`.
   - **Ejemplo**: Si tu nombre es "Bulma", debes ingresarlo tal como está registrado.
4. El sistema buscará la cita correspondiente en la base de datos. Si encuentra la cita, mostrará los detalles en el siguiente formato:
   > Confirmando cita para {nombre}: {fecha} a las {hora}.
5. Si no encuentra una cita registrada, mostrará el mensaje:
   > No hay cita programada para {nombre}.

### **Cancelar Cita**

Permite a los usuarios liberar un espacio previamente reservado. El proceso es el siguiente:

1. Desde el Menú Principal, selecciona la opción **Usuario**.
2. Una vez dentro del Menú del Usuario, selecciona la opción **Cancelar Cita ❌**.
3. El sistema solicitará ingresar el nombre del usuario. Este debe coincidir exactamente con el registrado en el archivo `Citas.csv`.
   - **Ejemplo**: Si tu nombre es "Krilin", debes ingresarlo tal como está registrado.
4. El sistema buscará la cita correspondiente en la base de datos. Si encuentra la cita, mostrará los detalles en el siguiente formato:
   > Cancelando cita para {nombre}: {fecha} a las {hora}.
5. Si no encuentra una cita registrada, mostrará el mensaje:
   > No hay cita programada para {nombre}.
6. Si la cancelación es exitosa, el sistema eliminará la cita del registro y mostrará un mensaje de éxito. Además, incrementará el contador de citas canceladas.

---

## 6. Contacto

Si necesitas asistencia técnica o tienes preguntas sobre el uso del sistema, contáctanos:

- 📧 **Correo electrónico**: soporte@pysanus.com
- 📞 **Teléfono**: +57 123 456 7890
