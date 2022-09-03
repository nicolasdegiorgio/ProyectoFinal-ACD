# Entrega-De-Giorgio
## Proyecto ACD (All Cars Detailing) para el proyecto final del curso de Python

Bienvenido a mi entrega del proyecto final!

Te cuento un poco de que se trata:
Este en la entrega de mi segunda aplicación creada con python y django, las cuales estoy aprendiendo actualmente.
Para este proyecto, plantee un ecommerce donde se pueden encontrar productos de detailing de vehiculos y distintos servicios que brindara la "empresa cliente".

La app web, cuenta a su vez con 2 "django-apps" las cuales administran los 2 punteros del servicio:

Usuarios
Productos

En la página de inicio muestra la cara de la pagina, con las ultimas entradas en productos (2) y las opciones de iniciar sesion o registrarse. A su vez, se podran ver todos los productos, sin poder realizar más acciones que intentar acceder al detalle del mismo, en el cual te pedirá loguearte.

En la parte superior, una vez logueado, se podrán ver los botones para navegar a través de la página (el navbar cambia a partir del logueo).
Aqui tambien se separa en tipos de usuarios, por un lado los superuser o administradores del local, que podran cargar, modificar o borrar entradas o produtos, además de realizar comentarios en cada uno. Por otro lado, los usuarios comunes solo podrán acceder a los detalles del mismo.

Al dar click en el boton "ver más" ("detalle/id") de cada producto (en el boton Productos-->Todos "todos/"), se podra acceder al detalle del prducto en donde se indica: Nombre del producto, stock, precio, fecha de carga, vendedor (usuario que lo cargó) y una breve descripción del mismo.
Además de ver más, siendo administrador del sitio se podra editar ("actualizar/id")el producto, modificando todos sus campos donde la descripción posee un editor de texto avanzado para darle el formato que el vendedor desee. También puede borrar los mismos utilizando el boton de elminar ("borrar/id"). Todos los ususarios pueden emitir comentarios en cualquier producto.
En el boton Productos también se encuentra el acceso a la carga de estos ("cargar"), que funciona de manera similar a la modificación pero crea una nueva entrada en el DB.
En el boton de Buscar o en "busqueda/", se puede acceder a la busqueda simple de productos.

Apartado "accounts/":
    Este es la app que gestiona los usuarios creados.
    Al momento de registrarse se crea un nuevo usuario el cual tomará como datos un username, email, contraseña, nombre y apellido.("registrate/")
    Para loguearse, se necesitará username y contraseña. ("inicio_sesion/")
    Algunas vistas protegidas llevarán directamente a la pagina de login para acceder.
    Menu desplegable "Hola user!": aqui se encuentran tres opciones.
        Ver los datos personales, que dentro de este se pueden modificar.("profile/")
        Cargar un avatar o imágen de perfil que se mostrará al lado de este menú y en el apartado anterior.("agregar_avatar/")
        Cerrar sesión. ("cerrar_sesion/")

Por ultimo, en el footer de la página, se puede acceder al apartado "About me" ("about_me")donde cuento un poc de mí y de como se creó el proyecto, y a su vez un formulario de contacto para postularse como vendedor o ser comprador indicando los items solicitados, mensajes que llegan al admin del sitio.

