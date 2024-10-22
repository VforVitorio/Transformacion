import reflex as rx
from tare_trans.state import State
from tare_trans.components.react_components.count_up import animated_score


def results() -> rx.Component:
    return rx.vstack(
        rx.heading("Resultados de Madurez Digital"),
        rx.hstack(
            rx.recharts.radial_bar_chart(
                rx.recharts.radial_bar(
                    data_key="score",
                    background=True,
                    label={"fill": "#666", "position": "insideStart"},
                ),
                data=[
                    {"name": "Total", "score": rx.Var.create(State.total_score)}],
                width=300,
                height=300,
                inner_radius="60%",
                outer_radius="80%",
                start_angle=180,
                end_angle=0,
            ),
            rx.vstack(
                rx.foreach(
                    State.area_scores,
                    lambda key, value: rx.hstack(
                        rx.text(key),
                        animated_score(value)
                    )
                )
            )
        ),
        rx.text("Nivel de Madurez: "),
        animated_score(State.total_score),
        rx.text(State.maturity_level)
    )
