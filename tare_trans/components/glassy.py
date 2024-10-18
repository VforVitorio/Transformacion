import reflex as rx
from tare_trans.styles.colors import Color, TextColor


def glassy_background() -> rx.Component:
    return rx.box(
        rx.html(
            f"""
          <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" preserveAspectRatio="none" viewBox="0 0 1000 500">
              <rect width="100%" height="100%" fill="{Color.PRIMARY.value}"/>
              <g fill="none" stroke="{TextColor.ACCENT.value}" stroke-width="1.5" stroke-opacity="0.2">
                  <path d="M0 350 C 200 100, 300 450, 500 200 C 700 -50, 800 350, 1000 150" />
                  <path d="M0 300 C 150 50, 250 400, 450 150 C 650 -100, 750 300, 1000 100" />
                  <path d="M0 250 C 100 0, 200 350, 400 100 C 600 -150, 700 250, 1000 50" />
                  <path d="M0 200 C 50 -50, 150 300, 350 50 C 550 -200, 650 200, 1000 0" />
                  <path d="M0 150 C 0 -100, 100 250, 300 0 C 500 -250, 600 150, 1000 -50" />
                  <path d="M0 100 C -50 -150, 50 200, 250 -50 C 450 -300, 550 100, 1000 -100" />
                  <path d="M0 50 C -100 -200, 0 150, 200 -100 C 400 -350, 500 50, 1000 -150" />
                  <path d="M0 0 C -150 -250, -50 100, 150 -150 C 350 -400, 450 0, 1000 -200" />
              </g>
          </svg>
          """
        ),
        position="absolute",
        top="0",
        left="0",
        width="100%",
        height="100%",
        z_index="-1",
        overflow="hidden",
    )
