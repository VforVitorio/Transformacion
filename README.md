# Proyecto de Transformación Digital

Este proyecto es una aplicación web desarrollada con el framework Reflex en Python. La aplicación permite realizar un cuestionario de transformación digital y muestra los resultados obtenidos.

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

2. Crea un entorno virtual (opcional pero recomendado):

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias del proyecto:

   ```sh
   pip install -r requirements.txt
   ```

## Ejecución

1. Inicia la aplicación con Reflex:

   ```sh
   reflex run
   ```

2. Abre tu navegador y navega a `http://localhost:3000` para ver la aplicación en funcionamiento. Este puerto puede cambiar segun la maquina y el propio compilador de reflex notifica el puerto donde se está corriendo la aplicación. En el primer run, es probable que tarde un tiempo mayor al normal, debido a que por debajo estará instalando todas las dependencias necesarias para el correcto funcionamiento de Reflex.

## Actualización

Para mantener tu repositorio actualizado con los últimos cambios, usa los siguientes comandos:

```sh
git pull origin main
```
