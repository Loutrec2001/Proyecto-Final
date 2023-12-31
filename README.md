# **Entendimiento de la situación actual**

QuakeAlert es una aplicación móvil diseñada para brindarte información precisa y oportuna sobre las alertas sísmicas en tu zona. Con nuestra aplicación, podrás recibir notificaciones instantáneas sobre la actividad sísmica cercana, permitiéndote estar preparado y tomar medidas preventivas adecuadas. Además de proporcionar alertas confiables, QuakeAlert también ofrece valiosos consejos y recomendaciones sobre cómo responder de manera segura y efectiva en caso de un terremoto. Nuestra aplicación te brindará la tranquilidad de saber que estás informado y preparado, ayudándote a proteger a ti mismo y a tus seres queridos durante los momentos críticos. Descarga QuakeAlert y mantente un paso adelante frente a los sismos

La propuesta de QuakeAlert surge como respuesta a una problemática significativa y recurrente en el Cinturón de Fuego del Pacífico: la alta incidencia de terremotos. Esta región geográfica, caracterizada por su intensa actividad sísmica, alberga a numerosas poblaciones expuestas a los riesgos y peligros asociados a los sismos.

QuakeAlert se propone como una solución integral para abordar la problemática de la alta actividad sísmica en el Cinturón de Fuego del Pacífico. Nuestra aplicación busca proveer información contextualizada, análisis actualizados y una red confiable de alerta temprana, con el objetivo de empoderar a las comunidades para que estén preparadas y puedan responder de manera segura ante los terremotos.


# **Objetivos**

## General

Crear una interfaz que permita visualizar la actividad sísmica general en la Costa Oeste de Estados Unidos, Mexico, Perú y Japón informando a los usuarios sobre la magnitud, localización y tiempo del suceso sismico, con el fin de brindar una ayuda oportuna por parte de los organismos de respuesta.

##Especificos:

1. Recopilar, analizar y extraer datos de los ultimos 15 años sobre la actividad sísmica de la Costa Oeste de Estados Unidos, Mexico, Perú y Japón, incluyendo la fecha, ubicación, magnitud y profundidad de los sismos.

2. Organizar la información obtenida y normalizada en un Data Warehouse.

3. Realizar un análisis estadístico de los datos haciendo énfasis en la frecuencia de sismos según localización y rangos de tiempo, profundidad, magnitudes máximas y mímimas.

4. Limpiar y transformar los datos sismicos para su posterior uso
en el modelo machine learning

5. Desarrollar un modelo de clasificacion de la peligrosidad del sismo utilizando k-vecinos

6. Crear una aplicación movil que maneje los datos que se les suministrará al usuario.

7. Crear una página web donde se realice el Deploy de la aplicación y se muestre su funcionamiento.


# **Alcance del trabajo**

Recopilación y análisis de datos sísmicos de fuentes confiables y actualizadas de los paises de Estados Unidos, Japón, México y Perú.

Al mismo tiempo desarrollaremos algoritmos y modelos para detectar y clasificar sismos de acuerdo al grado de magnitud.

Crearemos una base de datos actualizada que brinde informacion en tiempo real y sea facil de entender para el usuario.

Además se implementara una interfaz que indicará, si se deberá tomar medidas previsionales añadiendo mínimos detalles técnicos del fenómeno ocurrido.

Crear una Pagina web explicando el funcionamiento de la app.


# **Planteamiento de KPIs y sus objetivos asociados**

1. Cantidad de países en el cinturón de fuego:
Objetivo: Aumentar la capacidad de la aplicación para brindar información a más regiones.
Meta: Representar un aumento del 4% semestral en la cobertura geográfica de la aplicación.

2. Análisis de variables:
Objetivo: Ampliar el análisis de variables relacionadas con los sismos.
Meta: Incrementar en un 10% semestral la cantidad de variables analizadas.

3. Emisión de alerta:
Objetivo: Mejorar el tiempo de ejecucion desde que se genera el codigo de mensaje y se dispara el sistema de alerta a traves de mensajes via telegram.
Meta: Reducir el tiempo de ejecucion a un 50 seg para brindar una experiencia más rápida a los usuarios.

4. Alcance poblacional de usuarios de la app:
Objetivo: Aumentar la cantidad de registros en nuestro canal de telegram.
Meta: Incrementar en un 5% semestral el número de usuarios de la app entre la población objetivo.

5. Defunciones por repuesta tardia:
Objetivo: mejorar el tiempo de respuesta de participación y compromiso de los organimos de socorros frente a los desastres ocurridos.
Meta: Dsiminuir en un xx% el número de defunciones en los pròximos 5 años teniendo en cuanta el analisis de peligrosidad en determinadas zonas y el tiempo de respuesta.

# **Herramientas usadas**

- Python = Extracción, EDA, Transformación, carga a base de datos (inicial e incremental). Se utilizarán librerías para agilizar los procesos de conexión a base de datos, preparación de modelos de ML y gráficos de geolocalización.

- Python y sus librerías y Sql = Para ETL automatizado (incluye conexión a BD).

- Github = Repositorio de GITHUB y control de versiones.

- Power BI = Presentación de tablero.

- Azure Synapse Analytics = Creacion de Data Warehouse.

- Ambiente nube = Azure.

- Azure DataBricks, Azure Synapse Analytics, Azure Data Factory, Azure File Storage. 


# **Metodología de trabajo**

Utilizaremos la metodología ágil Scrum para la gestión del proyecto. Tendremos reuniones diarias de seguimiento, asignaremos roles y responsabilidades a cada miembro del equipo y nos apoyaremos en herramientas de gestión de proyectos como Jira.

# **Diseño detallado - Entregables**

Documento de especificación de requisitos.
Diseño de la arquitectura del sistema.
Prototipo de la interfaz de usuario.
Código fuente del proyecto.
Documentación de instalación y uso.

# **Equipo de trabajo - Roles y responsabilidades**

- Desarrollador backend: responsable del desarrollo del backend de la aplicación y la integración con la base de datos.

- Desarrollador frontend: encargado del desarrollo de la interfaz de usuario y la interacción con el backend.

- Científico de datos: responsable de la recopilación y análisis de datos sísmicos, así como del desarrollo de algoritmos de clasificación de sismos.

- Gestor de proyecto: encargado de la coordinación del equipo, planificación y seguimiento del proyecto.

## **Análisis preliminar de calidad de datos**:

Realizaremos un análisis detallado de los datos sísmicos disponibles, incluyendo metadatos como fuentes, confiabilidad, representación de cada columna, tipos de datos, método de adquisición y fechas de adquisición y actualización.

Se reorganizan las variables, se depuran las bases se crea una base nueva unificada y se aloja en el DataWare House en Synapse Analytics. La base se autoalimenta con la nueva información sismica.

# Github Proyecto: 

https://github.com/Loutrec2001/Proyecto-Final.git

# Presentación Tecnológica:

https://docs.google.com/presentation/d/1yftWE6cM3cVsvGFkl_Do_KXYw_7c3Ty8qFXDasGT68I/edit?usp=sharing

# Presentación Final

https://docs.google.com/presentation/d/1FaIUXzxlxIk9qh0kynJ3Lt4HKPI06EBq/edit?usp=sharing&ouid=103189885318330115740&rtpof=true&sd=true

# Página Web de la Aplicación

https://graceb2b.com/quakealert/

# Google Colab

https://colab.research.google.com/drive/1whjtXBgahRkZjdIBZhuaswbKpxfXwNuZ#scrollTo=TnwmcuRvhW7U

# Video Presentación Final

https://youtu.be/d51wHbBBlXQ

# Codigo Machine Learning y Notificaciones Telegram, Whatsapp y App

https://github.com/Kevinbonilla1993/ProyectoFinal.git

## Integrantes del equipo

* Ana Lucia Muzzo Rangil - Data Analyst
* Edward E. Guzmán González - Data Scientist
* Israel Andrés Nieves - Data Scientist
* Jose Gabriel Casanova - Data Analyst
* Kevin Bonilla - Data Engineer 

