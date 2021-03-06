# Tienda de Mascotas
Desarrollo de una Aplicación Web de tipo “Tienda para Mascotas” que ofrecerá productos (inventario y venta de productos entre otros) y servicios (consulta veterinaria, vacunación, urgencias entre otros) relacionados con el tema.

Esta aplicación está escrita en python usando el framework Django, se hace uso de los crud predefinidos en el framework, pero también se implementó request en json desde Vuejs usando la librería axios.

# Tecnología

* Python 3.8
* Django-admin 4.0
* Bootstrap 4.0
* Vue2
* MySql (MariaDB)
* Servidor Ubuntu 20.04 (Instancia en AWS) - [http://mascotas.lexisvar.me:8000/](http://mascotas.lexisvar.me:8000/)

# Patrón

* MVC aúnque como aclaración, al controlador se le llama vista y a la vista plantilla. 

# Módulos del proyecto

* Dashboard - estadísticas [x]
* CRUD Clientes [x]
* CRUD Mascotas [x]
* CRUD Productos [x]
* CRUD Servicios [x]
* Configuraciones []
* Ventas [x]
* Sistema de usuarios []
* Compras []
* Reportes [x] -> Módulo de clientes, ventas, ambos se consiguen con un click en dashboard
* Diagrama de clases [x]
* Modelo ER [x]
* Casos de Uso []

# NOTA

Los módulos que quedan sin desarrollar, se pueden agregar más adelante. Pero para esta primera etapa se considera que la aplicación ya es funcional.