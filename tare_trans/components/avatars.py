"""
Archivo donde se recopila informacion de los avatares y se renderiza a traves 
de un componente de reflex

"""
import reflex as rx

from tare_trans.styles.styles import Size
# Lista con el avatar, nombre y empleo de cada uno de los creadores
info = [
    {
        "avatar": "https://avatars.githubusercontent.com/u/117594428",
        "name": "Víctor Vega",
        "job": "Ingeniería en Sistemas Inteligentes",
    },
    {
        "avatar": "https://avatars.githubusercontent.com/u/161401345",
        "name": "Hugo Iglesias",
        "job": "Ingeniería en Sistemas Inteligentes",
    }
]


def item(image: str, name: str, job: str):
    """
    Componente que crea dos tarjetas con la foto de perfil, nombre y empleo 
    de los 2 creadores de la aplicacion

    Returns: componente de reflex que renderiza las dos tarjetas de los creadores
    """
    return rx.vstack(
        rx.image(
            src=image,
            width="100%",
            height="100%",
            object_fit="fit",
            transition="all 550ms ease",
            _hover={"transform": "scale(1.1)"},
            mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
        ),
        rx.vstack(
            rx.text(name, size="2", weight="bold",
                    color=rx.color("slate", 12)),
            rx.text(
                job,
                size="2",
                weight="bold",
                color=rx.color("slate", 10),
            ),
            position="absolute",
            bottom="0",
            left="0",
            bg=rx.color("gray", 3),
            width="100%",
            padding="12px 18px",
            spacing="0",
            justify="between",
        ),
        align="center",
        justify="center",
        position="relative",
        flex="1 1 auto 1",
        height="220px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 2),
        border_radius="12px",
        overflow="hidden",
        spacing="0",
        transition="all 250ms linear",
    )


def card_v2():
    """
    Componente que usa al anterior para generar cuantas tarjetas sean necesarias

    Returns: tarjetas con los avatares de cada uno de los creadores

    """
    return rx.vstack(
        rx.text("Integrantes", size=Size.BIG.value, color=rx.color(
            "slate", 11)),
        rx.hstack(
            *[item(data["avatar"], data["name"], data["job"])
              for data in info],
            width="100%",
            flex_wrap="wrap",
            justify="center",
        ),
        align="center",
        spacing="4",
        width="100%",
    )
