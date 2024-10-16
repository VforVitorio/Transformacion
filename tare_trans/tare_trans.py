import reflex as rx
import tare_trans.styles.styles as styles
from tare_trans.styles.styles import Size
from tare_trans.views.navbar import navbar
from tare_trans.views.header import header
from tare_trans.components.glassy import glassy_background


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


app = rx.App(
    # Cargamos las dos hojas de estilo definidas en styles.py
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="Proyecto de Transformación Digital",
             description="Se implementará un cuestionario de evaluación en relación a la transformación digital")
