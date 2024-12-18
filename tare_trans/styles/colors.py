from enum import Enum
"""
Archivo donde se definen 3 clases para simplificar 
la estetica de diferentes zonas de la aplicacion
 
    - Paleta de colores para botones, fondo y diversos elementos
    - Colores de los textos de la aplicacion

"""


class Color(Enum):
    """
    Clase con 4 colores diferentes usados en elementos de la aplicacion
    """
    ACCENT = "#7F56D9"  # Morado más suave para los botones
    PRIMARY = "#0D121D"  # Gris muy oscuro para el fondo principal
    # Un gris algo menos oscuro para los fondos de elementos secundarios
    SECONDARY = "#111827"
    TERTIARY = "#F1F1F1"  # Blanco ligeramente grisáceo para contrastar mejor con el fondo


class TextColor(Enum):
    """
    Clase con 4 colores diferentes para los diversos textos de la aplicacion
    """
    ACCENT = "#7F56D9"      # Morado claro para resaltar textos importantes
    PRIMARY = "#FFFFFF"     # Blanco puro para los textos principales
    SECONDARY = "#B3B3B3"   # Gris claro para los textos secundario
    TERTIARY = "#8A8A8A"    # Gris intermedio para textos aún más sutiles
