"""
Archivo que define los botones de la barra de la aplicacion
Componentes personalizados usando de base los de reflex
"""

import reflex as rx


def button(text: str, url: str) -> rx.Component:
    """
    Componente que crea botones personalizados para ser usados en algunas partes 
    de la aplicacion

        - Link de redireccion a una pagina exterior

    Returns: componente de boton que al pinchar sobre el redirige a una pagina fuera de la app

    """
    return rx.link(
        rx.button(
            text,
            color_scheme="violet"
        ),

        href=url,
        is_external=True
    )
