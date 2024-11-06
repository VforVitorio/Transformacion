"""
GRUPO 05: PROYECTO DE TRANSFORMACIÓN DIGITAL

Este archivo define la aplicacion de la pagina web.
En ella se usan todos los componentes definidos en el resto de archivos para generar
varias paginas de la aplicacion:
    - Pagina principal
    - Pagina de formulario antes de empezar
    - Pagina del cuestionario
    - Una pagina por cada sector
    - Pagina de los resultados

Se trata del frontend de la aplicacion. El backend puede ser encontrado en el archivo 
state.py

"""


import reflex as rx
import tare_trans.styles.styles as styles
from tare_trans.styles.styles import Size
from tare_trans.views.navbar import navbar
from tare_trans.views.header import header
from tare_trans.components.glassy import glassy_background
from tare_trans.views.form import form
from tare_trans.components.cursor import custom_cursor
from tare_trans.views.questionnaire import questionnaire
from tare_trans.views.results import results
from tare_trans.views.level import maturity_level
from tare_trans.views.footer import footer  # Importar el footer
from tare_trans.components.avatars import card_v2


def index() -> rx.Component:
    """
    Representa la pagina principal de la aplicacion, usando los componentes
    definidos en el resto de archivos: 
        - glassy_background()
        - navbar()
        - custom_cursor()
        - header()
    Los tres primeros son utilizados en el resto de componentes

    Returns: componente de Reflex que renderiza la página principal

    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                header(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
    )


def page_form() -> rx.Component:
    """
    Representa la pagina de formulario de la aplicacion.
    Usa el componente form() renderizado en un espacio vertical centrado
        -rx.center: centra el contenido
        -rx.vstack: renderiza el contenido en un contenedor vertical
        -form(): componente que contiene el frontend del formulario

    Returns: componente de Reflex que renderiza la página del formulario

    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                form(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
        footer()  # Añadir el footer aquí
    )


def results_page() -> rx.Component:
    """
    Componente que se encarga de crear la pagina de los resultados adquiridos en el cuestionario
        - results(): componente que contiene la logica y frontend para mostrar los resultados
        - maturity_level(): componente que muestra el grado de madurez digital de la empresa
        - card_v2(): componente que muestra la información referente a los creadores de la pagina



    Returns: componente de reflex que renderiza la pagina de los resultados del final del cuestionario
    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                results(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
        maturity_level(),
        card_v2(),
        footer()  # Añadir el footer aquí
    )


def sector_primario() -> rx.Component:
    """
    Pagina encargada del cuestionario referente al sector primario
    -questionnaire(): componente encargado de renderizar un cuestionario segun el sector elegido en form()


    Returns: componente que renderiza el cuestionario del sector primario
    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                questionnaire(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
        footer()  # Añadir el footer aquí
    )


def sector_secundario() -> rx.Component:
    """
    Pagina encargada del cuestionario referente al sector primario
    -questionnaire(): componente encargado de renderizar un cuestionario segun el sector elegido en form()


    Returns: componente que renderiza el cuestionario del sector secundario
    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                questionnaire(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
        footer()  # Añadir el footer aquí
    )


def sector_terciario() -> rx.Component:
    """
    Pagina encargada del cuestionario referente al sector primario
    -questionnaire(): componente encargado de renderizar un cuestionario segun el sector elegido en form()


    Returns: componente que renderiza el cuestionario del sector terciario
    """
    return rx.box(
        glassy_background(),
        navbar(),
        custom_cursor(),
        rx.center(
            rx.vstack(
                questionnaire(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        ),
        footer()  # Añadir el footer aquí
    )


# Creación de la aplciacioón de reflex mediante el instanciamiento de la clase rx.App
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,

)

# Con add_page se añaden las paginas creadas anteriormente a la aplicacion

app.add_page(index,
             title="Proyecto de Transformación Digital",
             description="Se implementará un cuestionario de evaluación en relación a la transformación digital",
             route="/"
             )

app.add_page(
    page_form,
    title="Formulario principio",
    description="formulario para determinar el sector al que se dedica la empresa y puesto que ocupa el usuario",
    route="/form"
)

app.add_page(
    sector_primario,
    title="Sector Primario",
    description="Página para el sector primario",
    route="/sector-primario"
)

app.add_page(
    sector_secundario,
    title="Sector Secundario",
    description="Página para el sector secundario",
    route="/sector-secundario"
)

app.add_page(
    sector_terciario,
    title="Sector Terciario",
    description="Página para el sector terciario",
    route="/sector-terciario"
)

app.add_page(
    results_page,
    title="Resultados",
    description="Resultados de la evaluación de madurez digital",
    route="/results"
)
