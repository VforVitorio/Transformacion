"""
Archivo donde se crea el componente footer, mostrado abajo de todo de las paginas 
de la app



"""


import reflex as rx
import tare_trans.styles.styles as styles
import tare_trans.constants as constants
from tare_trans.styles.styles import Size, TextColor


def footer() -> rx.Component:
    """
    Componente del footer de la pagina
        - Informacion de framework utilizado
        - Creadores de la aplicacion

    Returns: componente de Reflex que renderiza el footer
    """
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Pagina web hecha en reflex",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value

            ),
            rx.link(
                "Creado por Victor Vega y Hugo Iglesias",
                rx.box(class_name="bi bi-shield-check"),

                href=constants.GITHUB_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value


            ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),

        padding_bottom=Size.BIG.value,
        style=styles.max_width_style
    )
