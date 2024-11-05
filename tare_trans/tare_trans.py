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


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    frontend_packages=[
        "react-countup",
    ]
)

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
