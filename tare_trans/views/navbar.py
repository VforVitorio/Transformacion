"""
Archivo que renderiza el componente superior de la aplicacion
    - Barra delimitadora 
    - Logo de la universidad
    - Titulo descriptivo del proyecto academico
    - Botones con enlaces correspondientes a Linkedin, Github y página principal de la universidad


"""


import reflex as rx
import tare_trans.constants as constants
from tare_trans.styles.styles import Size, Color
from tare_trans.components.link_icon import link_icon


def navbar() -> rx.Component:
    # hstack se pinta de forma horizontal
    # vstack pone una linea debajo de la barra
    """
    Componente que renderiza la parte superior de la aplicacion

        - Imagen con el logo de la universidad
        - Titulo descriptivo de proyecto academico
        - Botones con enlaces referentes a Linkedin, Github y pagina principal de la UIE

    Returns: componente que renderiza la parte superior de la aplicacion con esas 3 vistas
    """
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/uie.png",
                alt="Imagen de la universidad en modo oscuro",
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value,
            ),
            rx.text("Proyecto Transformación Digital",
                    align="center",
                    size="6",
                    margin_top=Size.DEFAULT.value,),

            rx.spacer(),  # Empuja todo hacia la izquierda
            link_icon(
                "building",
                constants.UIE_URL
            ),

            link_icon(
                "linkedin",
                constants.LINKEDIN_URL
            ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.ACCENT.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,  # Para asegurar que pueden pasar las cosas por debajo
        top="0",
        width="100%"
    )
