"""
Archivo que crea iconos personalizados con enlace

"""

import reflex as rx
from tare_trans.styles.styles import Size


def link_icon(icon: str, url: str, size: str = "fs-2") -> rx.Component:
    """
    Componente con un icono con enlace al exterior

    Returns: link contenido en un icono de la biblioteca Bootstrap CSS
    """
    return rx.link(
        "",
        class_name=f"bi bi-{icon} {size}",
        href=url,
        margin_top=Size.SMALL.value,
        is_external=True
    )
