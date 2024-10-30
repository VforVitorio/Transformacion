import reflex as rx
from tare_trans.state import State
from tare_trans.styles.styles import TextColor, Color


def results() -> rx.Component:
    CHART_COLOR = "#7F56D9"
    MAX_BAR_WIDTH = "200px"  # Ajusta este valor según el ancho del texto más largo

    return rx.vstack(
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

        # Radar chart and area scores side by side
        rx.hstack(
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
                width="80%",  # Reduce el ancho del gráfico de radar
                height=650,  # Reduce la altura del gráfico de radar
            ),

            # Spacer
            rx.spacer(),

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
                                height="20px",  # Aumenta el tamaño de las barras individuales
                                background_color=CHART_COLOR,
                                border_radius="10px",
                            ),
                            rx.text(
                                f"{item[1]}%",
                                position="absolute",
                                left="50%",
                                top="50%",
                                transform="translate(-50%, -50%)",
                                color="white",
                                font_weight="bold",
                                font_size="0.9em",  # Aumenta el tamaño de fuente
                            ),
                            width=MAX_BAR_WIDTH,  # Tamaño fijo de la barra
                            height="20px",
                            background_color=Color.SECONDARY.value,
                            border_radius="10px",
                            overflow="hidden",
                            margin_y="0.5em",
                            position="relative",
                        ),
                        spacing="1",
                        align_items="center",
                    ),
                ),
                spacing="1em",
                align_items="center",  # Alinea las barras al centro verticalmente
                margin_left="2em",
                width="15%",  # Ajusta el ancho del contenedor de las barras de progreso
                margin_top="2em",  # Añade margen superior para bajar las barras
            ),
        ),

        rx.text(
            f"Nivel de Madurez: {State.maturity_level}",
            color=TextColor.PRIMARY.value,
        ),
        spacing="4",
        align_items="center",
    )
