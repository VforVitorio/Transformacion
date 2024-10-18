import reflex as rx

# Recibe el título del botón junto a la url de la página


def link_button(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            title
        ),
        href=url
    )
