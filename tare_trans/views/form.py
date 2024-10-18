import reflex as rx
from tare_trans.styles.colors import Color, TextColor


def form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.heading("Antes de empezar...", size="2xl",
                               text_align="center", margin_bottom="6"),
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text("Nombre", color=TextColor.PRIMARY.value,
                                        font_size="sm", font_weight="medium"),
                                rx.input(
                                    placeholder="Ingrese su nombre",
                                    border_color=Color.ACCENT.value,
                                    _focus={
                                        "border_color": Color.ACCENT.value},
                                    width="100%",
                                    id="nombre",
                                ),
                                align_items="start",
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("¿En qué sector se encuentra tu empresa?",
                                        color=TextColor.PRIMARY.value, font_size="sm", font_weight="medium"),
                                rx.select(
                                    ["Sector primario", "Sector secundario",
                                     "Sector terciario"],
                                    placeholder="Selecciona un sector",
                                    color=TextColor.PRIMARY.value,
                                    bg=Color.SECONDARY.value,
                                    border_color=Color.ACCENT.value,
                                    _focus={
                                        "border_color": Color.ACCENT.value},
                                    width="100%",
                                    id="sector",
                                ),
                                rx.text(
                                    "Por favor, selecciona un sector",
                                    color="red.500",
                                    font_size="sm",
                                    display=rx.cond(
                                        rx.select("sector") == "", "block", "none"),
                                ),
                                align_items="start",
                                spacing="2",
                                width="100%",
                            ),
                            rx.hstack(
                                rx.button(
                                    "Volver",
                                    variant="outline",
                                    border_color=Color.ACCENT.value,
                                    color=Color.ACCENT.value,
                                    _hover={"bg": Color.ACCENT.value,
                                            "color": TextColor.PRIMARY.value},
                                    on_click=rx.redirect("/"),
                                ),
                                rx.button(
                                    "Next",
                                    bg=Color.ACCENT.value,
                                    color=TextColor.PRIMARY.value,
                                    _hover={"opacity": 0.8},
                                    on_click=rx.redirect("/next_section"),
                                    is_disabled=rx.select("sector") == "",
                                ),
                                justify_content="space-between",
                                width="100%",
                                padding_top="5",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                    ),
                    padding="8",
                ),
                # Ajustado para pantallas grandes (relativo al viewport)
                width="50vw",
                max_width="600px",  # Máximo ancho para pantallas grandes
                min_width="300px",  # Ancho mínimo para pantallas pequeñas
                height="auto",  # Dejar la altura adaptable al contenido
                margin_top="5vh",
                background=f"rgba(127, 86, 217, 0.1)",
                backdrop_filter="blur(10px)",
                border="1px solid rgba(127, 86, 217, 0.2)",
                border_radius="15px",
                box_shadow="0 8px 32px 0 rgba(127, 86, 217, 0.2)",
            ),
            width="100%",
            height="auto",  # Ajustable en altura
            align_items="center",
            justify_content="flex-start",
            padding_top="5vh",
        ),
        width="100%",
        height="100vh",
    )
