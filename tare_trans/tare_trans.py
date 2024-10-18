import reflex as rx
import tare_trans.styles.styles as styles
from tare_trans.styles.styles import Size
from tare_trans.views.navbar import navbar
from tare_trans.views.header import header
from tare_trans.components.glassy import glassy_background
from tare_trans.views.form import form

def index() -> rx.Component:
    return rx.box(
        glassy_background(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        )
    )

def page_form() -> rx.Component:
    return rx.box(
        glassy_background(),
        navbar(),
        rx.center(
            rx.vstack(
                form(),
                spacing=Size.VERY_BIG.value
            ),
            width="100%"
        )
    )

def sector_primario() -> rx.Component:
    return rx.box(
        glassy_background(),
        navbar(),
        rx.center(
            rx.text("Contenido para el Sector Primario"),
            width="100%"
        )
    )

def sector_secundario() -> rx.Component:
    return rx.box(
        glassy_background(),
        navbar(),
        rx.center(
            rx.text("Contenido para el Sector Secundario"),
            width="100%"
        )
    )

def sector_terciario() -> rx.Component:
    return rx.box(
        glassy_background(),
        navbar(),
        rx.center(
            rx.text("Contenido para el Sector Terciario"),
            width="100%"
        )
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
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
    description="Contenido específico para el sector primario",
    route="/sector_primario"
)

app.add_page(
    sector_secundario,
    title="Sector Secundario",
    description="Contenido específico para el sector secundario",
    route="/sector_secundario"
)

app.add_page(
    sector_terciario,
    title="Sector Terciario",
    description="Contenido específico para el sector terciario",
    route="/sector_terciario"
)