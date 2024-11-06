"""
Archivo que define tamaños, para simplificar y hacer mas intuitivo la construccion
del frontend de la aplicacion con valores manejados a traves de variables mas intuitivas

"""


import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"  # La web no debe pasar nunca de 1000 pixeles


class Size(Enum):
    """
    Clase con los diferentes tamaños usados entre y en los elementos de la app
    """
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"  # 1 em es el valor de la fuente por defecto
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"


# Componentes de css que usa la aplicacion
STYLESHEETS = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css",  # Agrega esto
    "https://fonts.googleapis.com/css?family=Inter&display=swap"

]

# Estilo base de la aplicacion
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}

# Definicion del estilo de la aplicacion cuando se dispone de su maximo tamaño
max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
