import reflex as rx


def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            color_scheme="violet"
        ),

        href=url,
        is_external=True
    )
