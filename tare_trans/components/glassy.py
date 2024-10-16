import reflex as rx
from tare_trans.styles.colors import Color


def glassy_background() -> rx.Component:
    return rx.box(
        rx.html(
            f"""
            <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" preserveAspectRatio="none" viewBox="0 0 1000 500">
                <defs>
                    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:{Color.PRIMARY.value};stop-opacity:1" />
                        <stop offset="100%" style="stop-color:{Color.PRIMARY.value};stop-opacity:1" />
                    </linearGradient>
                </defs>
                <rect width="100%" height="100%" fill="url(#grad1)"/>
                <g fill="none" stroke="#4B5563" stroke-width="1" stroke-opacity="0.2">
                    <path d="M0 350 C 250 300, 350 450, 500 300 C 650 150, 750 350, 1000 250" />
                    <path d="M0 300 C 200 250, 300 400, 450 250 C 600 100, 700 300, 1000 200" />
                    <path d="M0 250 C 150 200, 250 350, 400 200 C 550 50, 650 250, 1000 150" />
                    <path d="M0 200 C 100 150, 200 300, 350 150 C 500 0, 600 200, 1000 100" />
                    <path d="M0 150 C 50 100, 150 250, 300 100 C 450 -50, 550 150, 1000 50" />
                    <path d="M0 100 C 0 50, 100 200, 250 50 C 400 -100, 500 100, 1000 0" />
                    <path d="M0 50 C -50 0, 50 150, 200 0 C 350 -150, 450 50, 1000 -50" />
                    <path d="M0 0 C -100 -50, 0 100, 150 -50 C 300 -200, 400 0, 1000 -100" />
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
