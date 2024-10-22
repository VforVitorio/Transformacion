# tare_trans/views/results.py
import reflex as rx
from tare_trans.state import State


def results() -> rx.Component:
    return rx.vstack(
        rx.heading("Resultados de Madurez Digital"),
        # Main radial chart for total score
        rx.recharts.radial_bar_chart(
            rx.recharts.radial_bar(
                data_key="score",
                background=True,
                label={"fill": "#666", "position": "insideStart"},
            ),
            data=[{"name": "Total", "score": State.total_score}],
            width=300,
            height=300,
            inner_radius="60%",
            outer_radius="80%",
            start_angle=180,
            end_angle=0,
        ),
        # Area scores
        rx.hstack(
            rx.foreach(
                State.area_scores.items(),
                lambda item: rx.vstack(
                    rx.text(item[0]),
                    rx.recharts.radial_bar_chart(
                        rx.recharts.radial_bar(
                            data_key="score",
                            background=True,
                        ),
                        data=[{"name": item[0], "score": item[1]}],
                        width=100,
                        height=100,
                        inner_radius="60%",
                        outer_radius="80%",
                        start_angle=180,
                        end_angle=0,
                    ),
                ),
            ),
            wrap="wrap",
            spacing="4",
        ),
        # Radar chart using computed var
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="score",
                stroke="#8884d8",
                fill="#8884d8",
                fill_opacity=0.6,
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="area"),
            rx.recharts.polar_radius_axis(
                angle=90,
                domain=[0, 100]
            ),
            data=State.radar_chart_data,
            width="100%",
            height=300,
        ),
        rx.text(f"Nivel de Madurez: {State.maturity_level}"),
        spacing="4",
        align_items="center",
    )
