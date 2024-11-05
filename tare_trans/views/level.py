import reflex as rx
from tare_trans.styles.styles import TextColor, Color
from tare_trans.state import State


def maturity_level() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.vstack(
                rx.heading(
                    f"Nivel de Madurez: {State.maturity_level}",
                    color=Color.TERTIARY.value,
                    size="8",
                    align="center"
                ),
                rx.heading(
                    f"{State.sector}",
                    color=TextColor.PRIMARY.value,
                    size="6",
                    align="center"
                ),
                rx.foreach(
                    State.areas.items(),
                    lambda item: rx.vstack(
                        rx.heading(item[1]["name"], size="5", align="center"),
                        rx.text(
                            State.area_feedbacks[item[0]],
                            color=TextColor.TERTIARY.value
                        ),
                        padding="1em",
                        width="100%"
                    ),
                ),
                rx.button(
                    "Volver al Inicio",
                    bg_color=Color.ACCENT.value,
                    color=TextColor.PRIMARY.value,
                    _hover={"opacity": 0.8},
                    # Use rx.redirect to go to root path <sup><a href="#">1</a></sup><sup><a href="#">2</a></sup>
                    on_click=rx.redirect("/"),
                    font_size=["1em", "1.1em", "1.2em", "1.2em"],
                    padding="1em 2em",
                ),
                justify_content="center",
                align_items="center",
                spacing="2em",
                width="80%",
                padding="2em",
                z_index="1",
            ),
            width="100%",
            height="auto",
            padding_y="2em"
        ),
        width="100%",
        position="relative",
    )
