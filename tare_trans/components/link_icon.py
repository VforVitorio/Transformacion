import reflex as rx
from tare_trans.styles.styles import Size
# con size dentro de los parametros podemos cambiar el tamaño
# al icono de bootsrap


def link_icon(icon: str, url: str, size: str = "fs-2") -> rx.Component:
    return rx.link(
        "",
        class_name=f"bi bi-{icon} {size}",
        href=url,
        margin_top=Size.SMALL.value,
        is_external=True
    )
