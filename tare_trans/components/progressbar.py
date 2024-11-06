"""
Archivo que define las diferentes barras de progreso de la aplicacion
"""

import reflex as rx
from tare_trans.styles.styles import Color


def ProgressBar(progress: float) -> rx.Component:
    """
    Componente que define una barra de progreso

    Returns: barra de progreso horizontal, con porcentaje en interior y pintado de morado
    """
    return rx.box(
        rx.box(
            width=f"{progress}%",
            height="10px",
            bg_color=Color.ACCENT.value,
            border_radius="5px",
        ),
        width="100%",
        height="10px",
        bg_color=Color.SECONDARY.value,
        border_radius="5px",
        overflow="hidden",
    )
