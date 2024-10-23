# tare_trans/views/results.py
import reflex as rx
from tare_trans.state import State
from tare_trans.styles.styles import TextColor


def results() -> rx.Component:
    # Definimos los colores según tu paleta
    CHART_COLOR = "#7F56D9"  # Color.ACCENT
    BACKGROUND_COLOR = "#111827"  # Color.SECONDARY

    return rx.vstack(
        rx.heading("Resultados de Madurez Digital",
                   padding_top="1em"),

        # Main radial chart - más grande y con el color actualizado
        rx.recharts.radial_bar_chart(

            rx.recharts.radial_bar(
                data_key="score",

                label={
                    "fill": "#FFFFFF",  # TextColor.PRIMARY
                    "position": "center",  # Centered text
                    "fontSize": 20  # Larger font
                },

            ),
            data=[{"name": "Total", "score": State.total_score}],
            width=400,  # Increased size
            height=400,  # Increased size
            inner_radius="60%",
            outer_radius="80%",
            start_angle=360,
            end_angle=0,
            fill=CHART_COLOR,
        ),

        # Area scores organizados en dos vstack
        rx.vstack(
            # Primer vstack para los gráficos semicirculares
            rx.hstack(
                rx.foreach(
                    State.area_scores.items(),
                    lambda item: rx.vstack(
                        rx.text(item[0]),
                        rx.recharts.radial_bar_chart(
                            rx.recharts.radial_bar(
                                data_key="score",
                                background=True,
                                fill="#FFFFFF",
                                label={
                                    "fill": "#FFFFFF",  # TextColor.PRIMARY
                                    "position": "center",
                                    "fontSize": 16
                                },
                            ),
                            data=[{"name": item[0], "score": item[1]}],
                            width=200,  # Increased size
                            height=200,  # Increased size
                            inner_radius="60%",
                            outer_radius="80%",
                            fill=CHART_COLOR

                        ),
                    ),
                ),
                spacing="4",
            ),

            # Segundo vstack para el radar chart
            rx.vstack(
                rx.recharts.radar_chart(
                    rx.recharts.radar(
                        data_key="score",
                        stroke=CHART_COLOR,
                        fill=CHART_COLOR,
                        fill_opacity=0.6,
                    ),
                    rx.recharts.polar_grid(),
                    rx.recharts.polar_angle_axis(data_key="area"),
                    rx.recharts.polar_radius_axis(
                        angle=90,
                        domain=[0, 100]
                    ),
                    data=State.radar_chart_data,
                    width=400,  # Specific width
                    height=400,  # Increased height

                ),
            ),
            spacing="8",  # Más espacio entre los grupos de gráficos
            align_items="center",
        ),

        rx.text(
            f"Nivel de Madurez: {State.maturity_level}",
            color=TextColor.PRIMARY.value,
        ),
        spacing="4",
        align_items="center",
    )
