import reflex as rx

from tare_trans.styles.styles import Size
from tare_trans.styles.colors import Color, TextColor


def header() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Digital. Data. Innovation.",
                size="9",
                weight="bold",
                color=TextColor.PRIMARY.value,
            ),
            rx.text(
                "El cuestionario de transformación digital para tu empresa.",
                font_size="7",
                color=TextColor.SECONDARY.value,
                margin_top=Size.DEFAULT.value,
                margin_bottom=Size.DEFAULT.value,
            ),
            rx.link(
                rx.button(
                    "Comenzar el cuestionario",
                    bg_color=Color.ACCENT.value,
                    color="white",
                    padding="1.75em 3em",
                    font_size="1.1em",
                    border_radius="1em",
                    _hover={"bg_color": "#6d28d9"},
                ),
                href="/form",  # URL a la que redirige el botón
            ),
            spacing="5",
            align_items="center",
            padding=Size.VERY_BIG.value,
            width="100%",
            min_height="60vh",
            justify_content="center",
            position="relative",
            z_index="1",
        ),
        position="relative",
        width="100%",
        min_height="60vh",
        overflow="hidden",
        before=rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=f"linear-gradient(to right, {Color.SECONDARY.value}CC, {Color.SECONDARY.value}99)",  # noqa
            backdrop_filter="blur(3px)",
            z_index="0",
        )
    )
