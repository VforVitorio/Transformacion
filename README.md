# Proyecto de Transformación Digital

Este proyecto es una aplicación web desarrollada con el framework Reflex en Python. La aplicación permite realizar un cuestionario de transformación digital y muestra los resultados obtenidos.

Se trata de un proyecto académico, realizado por el Grupo 05 de la asignatura de Tecnologías de Automatización y Robotización Empresarial (TAyRE).

Se evaluará próximamente el despliegue de la aplicación en una página web. No obstante, se deben de hacer las valoraciones necesarias del servicio de hosting de Reflex en cuanto a la seguridad, acceso, etc. que tendrán los usuarios finales a la web.

Todo el código, con sus respectivas versiones y cambios, se encuentra en el repositorio de GitHub mencionado en el paso número 1 de instalación.

En la entrega del proyecto, donde se encuentra el archivo zip, se encuentran los archivos subidos al repositorio. Para crear este zip, se ha usado el siguiente comando de terminal:

```sh
git archive --format zip --output herramienta_grupo_05.zip main
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- git (herramienta de gestión de versiones de código)

## Instalación

1. Clona el repositorio en tu máquina local:

   ```sh
   git init
   git clone https://github.com/VforVitorio/Transformacion.git
   cd Transformacion
   ```

2. Crear un entorno virtual (opcional pero recomendado):

   ```sh
   python -m venv nombre_entorno
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instalar las dependencias del proyecto:

   ```sh
   pip install -r requirements.txt
   ```

## Ejecución

1. Iniciar la aplicación con Reflex:

   ```sh
   reflex run
   ```

2. Abra el navegador y navega a `http://localhost:3000` para ver la aplicación en funcionamiento. Este puerto puede cambiar segun la máquina y el propio compilador de reflex notifica el puerto donde se está corriendo la aplicación. En el primer run, es probable que tarde un tiempo mayor al normal, debido a que por debajo estará instalando todas las dependencias necesarias para el correcto funcionamiento de Reflex.

## Actualización

Para mantener tu repositorio actualizado con los últimos cambios, usa los siguientes comandos:

```sh
git pull origin main
```
