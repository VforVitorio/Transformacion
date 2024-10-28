# tare_trans/views/results.py
import reflex as rx
from tare_trans.state import State
from tare_trans.styles.styles import TextColor, Color


def results() -> rx.Component:
    CHART_COLOR = "#7F56D9"

    return rx.hstack(
        rx.vstack(
            rx.heading("Resultados de Madurez Digital", padding_top="1em"),

            # Total progress bar with text
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
                position="relative",
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
                rx.recharts.polar_radius_axis(angle=90, domain=[0, 100]),
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
        ),

        # Area scores with individual progress bars
        rx.vstack(
            rx.foreach(
                State.area_scores.items(),
                lambda item: rx.box(
                    rx.text(
                        item[0],  # Nombre del área
                        font_weight="bold",
                        color=TextColor.PRIMARY.value,
                        margin_bottom="0.5em",
                    ),
                    rx.box(
                        rx.box(
                            # Porcentaje de puntaje del área
                            width=f"{item[1]}%",
                            height="10px",  # Tamaño reducido para las barras individuales
                            background_color=CHART_COLOR,
                            border_radius="5px",
                        ),
                        rx.text(
                            f"{item[1]}%",
                            position="absolute",
                            left="50%",
                            top="50%",
                            transform="translate(-50%, -50%)",
                            color="white",
                            font_weight="bold",
                            font_size="0.7em",  # Tamaño reducido de fuente
                        ),
                        width="80%",  # Tamaño de la barra
                        height="10px",
                        background_color=Color.SECONDARY.value,
                        border_radius="5px",
                        overflow="hidden",
                        margin_y="0.5em",
                        position="relative",
                    ),
                    spacing="1",
                    align_items="center",
                ),
            ),
            spacing="1em",
            align_items="flex-start",
            margin_left="2em",
        ),
    )
