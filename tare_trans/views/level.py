# level.py
import reflex as rx
from tare_trans.styles.styles import TextColor
from tare_trans.state import State


def maturity_level() -> rx.Component:
    return rx.vstack(

        rx.heading(
            f"Nivel de Madurez: {State.maturity_level}",
            color=TextColor.PRIMARY.value,
        ),
    )
