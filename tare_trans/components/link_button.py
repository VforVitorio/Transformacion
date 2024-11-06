"""
Archivo donde se construye un boton con enlace
"""

import reflex as rx

# Recibe el título del botón junto a la url de la página


def link_button(title: str, url: str) -> rx.Component:
    """
    Boton con enlace

    Returns: componente personalizado de boton que lleva al enlace alojado en el
    """
    return rx.link(
        rx.button(
            title
        ),
        href=url
    )
