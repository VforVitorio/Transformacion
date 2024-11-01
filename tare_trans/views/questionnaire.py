import reflex as rx
from tare_trans.components.progressbar import ProgressBar
from tare_trans.styles.styles import Color, TextColor
from tare_trans.state import State


def questionnaire() -> rx.Component:
    return rx.cond(
        State.is_loading,
        rx.text("Cargando..."),
        rx.box(
            rx.vstack(
                rx.heading("Transformación Digital",
                           color=TextColor.PRIMARY.value,
                           font_size=["2em", "2.5em", "3em", "3.25em"],
                           text_align="center",
                           width="100%",
                           ),
                rx.text(State.current_question_number,
                        color=TextColor.SECONDARY.value,
                        font_size=["1em", "1.2em", "1.3em", "1.5em"],
                        text_align="center",
                        width="100%",
                        ),
                ProgressBar(progress=State.progress_percentage),
                rx.card(
                    rx.text(
                        State.current_question_data["question"],
                        color=TextColor.PRIMARY.value,
                        font_size=["1em", "1.1em", "1.2em", "1.25em"],
                        text_align="center"
                    ),
                    bg_color=Color.SECONDARY.value,
                    width="100%",
                    padding="1.5em",
                ),
                rx.radio(
                    State.current_question_data["options"],
                    value=State.current_answer,
                    on_change=State.answer_question,
                    direction="column",
                    size="3",
                ),
                rx.hstack(
                    rx.button(
                        "Anterior",
                        variant="outline",
                        border_color=Color.ACCENT.value,
                        color=Color.ACCENT.value,
                        _hover={"bg": Color.ACCENT.value,
                                "color": TextColor.PRIMARY.value},
                        on_click=State.previous_question,
                        is_disabled=State.is_first_question,
                        font_size=["1em", "1.1em", "1.2em", "1.2em"],
                        padding="1em 2em",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Siguiente",
                        bg_color=Color.ACCENT.value,
                        color=TextColor.PRIMARY.value,
                        _hover={"opacity": 0.8},
                        on_click=State.next_question,
                        is_disabled=State.is_last_question,
                        font_size=["1em", "1.1em", "1.2em", "1.2em"],
                        padding="1em 2em",
                    ),
                    width="100%",
                    margin_top="2em",
                ),
                spacing="7",
                align_items="flex_start",
                padding="3em",
                width="100%",
                min_height="70vh",
                justify_content="flex_start",
                position="relative",
                z_index="1",
            ),
            position="relative",
            width="100%",
            min_height="70vh",
            overflow="hidden",
            before=rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background=f"linear-gradient(to right, {Color.SECONDARY.value}CC, {
                    Color.SECONDARY.value}99)",
                backdrop_filter="blur(3px)",
                z_index="0",
            )
        )
    )
