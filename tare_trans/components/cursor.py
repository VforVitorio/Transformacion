import reflex as rx
from reflex_animated_cursor import AnimatedCursor
from tare_trans.styles.colors import Color


def custom_cursor() -> rx.Component:
    return AnimatedCursor(
        color=Color.ACCENT.value,           # RGB value for the cursor color
        inner_scale=0.7,                    # Scale factor for the inner cursor
        outer_scale=1.0,                    # Scale factor for the outer cursor
        outer_alpha=0.3,                    # Alpha transparency for the outer cursor
        inner_size=8,                       # Size (px) of the inner cursor dot
        outer_size=35,
        inner_style={"backgroundColor": Color.TERTIARY.value},
        outer_style={"border": f"2px solid {Color.ACCENT.value}"},
        clickables=["a", "input[type='text']", "button", "select", "textarea"],
        show_system_cursor=False,
        trailing_speed=8
    )
