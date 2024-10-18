import reflex as rx


def redirect_based_on_sector():
    sector = rx.select("sector")
    if sector == "Sector primario":
        return rx.redirect("/sector_primario")
    elif sector == "Sector secundario":
        return rx.redirect("/sector_secundario")
    elif sector == "Sector terciario":
        return rx.redirect("/sector_terciario")
    else:
        return rx.window_alert("Por favor, selecciona un sector antes de continuar.")
