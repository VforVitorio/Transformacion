import reflex as rx
from tare_trans.styles.styles import Color


def ProgressBar(progress: float) -> rx.Component:
    return rx.box(
        rx.box(
            width=f"{progress}%",
            height="10px",
            bg_color=Color.ACCENT.value,
            border_radius="5px",
        ),
        width="100%",
        height="10px",
        bg_color=Color.SECONDARY.value,
        border_radius="5px",
        overflow="hidden",
    )
