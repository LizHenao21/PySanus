# Manual de Uso del Sistema de Gestión de Citas - Pysanus

## 1. Introducción
El **Sistema de Gestión de Citas - Pysanus** es un programa diseñado para gestionar las citas médicas de los usuarios. Ofrece una interfaz intuitiva para administradores y usuarios, permitiendo:
- Confirmar y cancelar citas programadas.
- Gestionar cuentas de administrador.
- Generar reportes detallados sobre las actividades del sistema.

El programa utiliza un archivo de datos (`Citas.csv`) para registrar y gestionar las citas.

---

## 2. Inicio del Programa
Cuando inicias el programa, se presenta un menú principal con tres opciones:
1. **Administrador 💻**: Accede a funcionalidades como gestionar usuarios y generar reportes.
2. **Usuario 👩‍⚕️**: Permite confirmar o cancelar citas programadas.
3. **Salir 🚪**: Cierra el programa.

---

## 3. Funcionalidades del Programa
### **3.1 Opciones del Administrador**
1. **Reportes 📋**:
   - Muestra:
     - Usuarios registrados.
     - Total de citas confirmadas.
     - Total de citas canceladas.
2. **Añadir Administrador ➕**:
   - Permite añadir un administrador ingresando un nombre único y una contraseña.
3. **Eliminar Administrador ❌**:
   - Permite eliminar un administrador existente por su nombre de usuario.
4. **Salir 🚪**:
   - Regresa al menú principal.

### **3.2 Opciones del Usuario**
1. **Confirmar Cita ✅**:
   - Solicita el nombre del usuario y confirma su cita registrada.
2. **Cancelar Cita ❌**:
   - Solicita el nombre del usuario y elimina su cita del sistema.
3. **Salir 🚪**:
   - Regresa al menú principal.

---

## 4. Estructura de Datos
El programa utiliza un archivo CSV para registrar las citas:
- **Nombre**: Nombre del usuario.
- **CitaAtencion**: Fecha y hora de la cita (`YYYY-MM-DD|HH:MM`).

---

## 5. Reportes y Estadísticas
Los reportes generados incluyen:
- **Usuarios registrados**.
- **Citas confirmadas**.
- **Citas canceladas**.

---

## 6. Contacto
📧 Correo electrónico: soporte@pysanus.com  
📞 Teléfono: +57 123 456 7890

