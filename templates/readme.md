# Calculador de Comisiones

Este proyecto es un calculador de comisiones simple que consta de un front-end en HTML y un back-end en Flask. Permite calcular la comisión basada en un monto de ventas y un porcentaje de comisión proporcionado por el usuario.

## Descripción

El sistema recibe el monto de ventas y el porcentaje de comisión a través de una interfaz web y envía estos datos al servidor Flask. El servidor realiza el cálculo de la comisión y devuelve el resultado al front-end, donde se muestra al usuario.

## Estructura del Proyecto


- **app.py**: Contiene el código del servidor Flask que maneja las solicitudes y calcula las comisiones.
- **/templates/index.html**: El archivo HTML que sirve como front-end del proyecto.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/calculador-comisiones.git

Navega al directorio del proyecto:
cd calculador-comisiones

Instala las dependencias necesarias:
pip install flask flask-cors

USO:Inicia el servidor Flask:
python app.py

Abre tu navegador web y navega a http://127.0.0.1:5000.

Ingresa el monto de ventas y el porcentaje de comisión en el formulario y haz clic en "Calcular Comisión" para ver el resultado.

Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request para cualquier mejora o corrección.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.