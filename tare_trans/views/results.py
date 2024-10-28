# tare_trans/views/results.py
import reflex as rx
from tare_trans.state import State
from tare_trans.styles.styles import TextColor, Color


def results() -> rx.Component:
    CHART_COLOR = "#7F56D9"

    return rx.vstack(
        rx.heading("Resultados de Madurez Digital",
                   padding_top="1em"),

        # Progress bar with text
        rx.box(
            rx.box(
                width=f"{State.total_score}%",
                height="30px",
                background_color=CHART_COLOR,
                border_radius="15px",
            ),
            rx.text(
                f"{State.total_score}%",
                position="absolute",
                left="50%",
                top="50%",
                transform="translate(-50%, -50%)",
                color="white",
                font_weight="bold",
            ),
            width="80%",
            height="30px",
            background_color=Color.SECONDARY.value,
            border_radius="15px",
            overflow="hidden",
            margin_y="2em",
            position="relative",  # Required for absolute positioning of text
        ),

        # Radar chart
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="score",
                stroke=CHART_COLOR,
                fill=CHART_COLOR,
                fill_opacity=0.6,
                dot=True,
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="area"),
            rx.recharts.polar_radius_axis(
                angle=90,
                domain=[0, 100]
            ),
            data=State.radar_chart_data,
            width="100%",
            height=400,
        ),
        rx.text(
            f"Nivel de Madurez: {State.maturity_level}",
            color=TextColor.PRIMARY.value,
        ),
        spacing="4",
        align_items="center",
    )
