"""
Archivo que crea un cursor personalizado para la aplicacion
"""

import reflex as rx
from reflex_animated_cursor import AnimatedCursor
from tare_trans.styles.colors import Color


def custom_cursor() -> rx.Component:
    """
    Componente que crea un cursor personalizado

    Returns: instancia de AnimatedCursor, creando un cursor de punto blanco rodeado de un circulo morado

    """
    return AnimatedCursor(
        color=Color.ACCENT.value,
        inner_scale=0.7,
        outer_scale=1.0,
        outer_alpha=0.3,
        inner_size=8,
        outer_size=35,
        inner_style={"backgroundColor": Color.TERTIARY.value},
        outer_style={"border": f"2px solid {Color.ACCENT.value}"},
        clickables=["a", "input[type='text']", "button", "select", "textarea"],
        show_system_cursor=False,
        trailing_speed=8
    )
