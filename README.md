# 🚨 Redar
Es una plataforma en linea creada con el framework Django de prevencion de desatre natural pensada en enviar una alerta preventiva a las entidades de rescate correspondientes para una reaccion mas rapida por parte de los mismos y asi evitar el mayor numero de victimas en el municipio.

El objetivo de la app es pensada en que el funcionario municipal encargado en caso de ser avisado de una posible alerta de desastre natural con su usuario registrado generara el reporte de riesgo de desastre natural en el cual contiene el tipo de alerta, el nivel y una breve descripcion sobre el potencial riesgo y marca la fecha directa del reporte. Se envia el reposte por medio de correo electronico a la entidad o al funcionario encargado en la ciudad principal del departamento para una respuesta inmediata y acudir lo mas rapido posible al municipio 

---

## 📑 Caracteristicas
### 🪟 Interfaces
- Interfaz de login
- Dashboard Interfaz principal para la creacion de alertas
- Interfaz de historial de reportes por usuario
- Interfaz de usuario administrador
### 🎚 Funcionalidades
- Desde la interfaz del admisnitrador se registran los datos de los usuarios que van a utilizar la app.
- Los datos desde la interfaz de administrador se envian a base de datos ya que a partir del framework permite la migracion de datos y la creacion de la bd siempre y cuando ya se haya establecido comunicacion a la base de datos.
- El usuario al iniciar sesion en la interfaz principal con los datos acordados, desde el nombre de usuario como la contraseña designada.
- Las alertas y los niveles son editables desde el admisnitrador ya que se le da la facilidad de edicion a partir de las alertas en caso de uan revision tecnica o monitorear las alertas de los usuarios.
- En la interfaz del usuario normal ya tiene el menu con las opciones de alerta y sus niveles designados teniendo en cuanta que cada alerta que registre se le asignará la fecha designada en el dispositivo.
- Maneja cuadros emergentes en las interfaces como guia de respuesta al usuario tanto para inicio de sesion como registro de alerta
- Las alerta al crearlas se envian tipo correo electronico Gmail a los usuarios asignados desde el codigo fuente por motivos de seguridad como metodo SMTP diseñado para que llegue con una interfaz acorde a la plataforma
---

## Tecnologias 
### 🖥 Frontend
HTML5: Estructurado de templates
CSS: Estilos y presentacion del template 
Bootstrap: Iconografia y estilizados del template

### 🗄 Backend
- Django: Estructura raiz del backend como framework
- PostgreSQL: Base de datos
---

## 💼 Dependencias
Registor de dependencias y sus validaciones
- asgiref==3.10.0
- Django==5.2.7
- pillow==12.0.0
- psycopg2-binary==2.9.11
- python-decouple==3.8
- python-dotenv==1.2.2
- sqlparse==0.5.3
- tzdata==2025.2


### 😺 CLonar Repositorio

- El framework trabaja exclusivamente con python v.3.13.13:
https://www.python.org/downloads/

- Recomendable crear el entorno virtual (env) para evitar errores de compatibilidad para otros proyectos que manejen otras versiones de algun programa

- Descargar Framework Django: 
``python -m pip install Django==5.2.7``

- Se debe conectar su base de datos y siguiente realizar las respectivas migraciones para que pueda crear las tablas en la base de datos

- Enlace para clonar repo: https://github.com/MateoIsazaZapata/appDagran.git