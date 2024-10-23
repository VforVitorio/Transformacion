import reflex as rx
from tare_trans.state import State
from tare_trans.styles.styles import TextColor
import matplotlib.pyplot as plt
from math import pi
import io
import base64


def create_donut_chart(value: float, title: str):
    try:
        value_float = float(value)
    except (TypeError, ValueError):
        value_float = 0.0

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    fig.patch.set_alpha(0.0)

    startangle = 90
    x = (value_float * pi * 2) / 100
    left = (startangle * pi * 2) / 360

    plt.xticks([])
    plt.yticks([])
    ax.spines.clear()

    ax.barh(1, pi * 2, left=left, height=1, color='#2D3748', alpha=0.3)
    ax.barh(1, x, left=left, height=1, color='#7F56D9')

    plt.ylim(-3, 3)

    plt.text(0, -3, f"{value_float:.1f}%",
             ha='center',
             va='center',
             fontsize=42,
             color='white',
             fontweight='bold')

    plt.title(title,
              color='white',
              fontsize=16,
              pad=20,
              fontweight='bold')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True,
                bbox_inches='tight', dpi=100)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"


def donut_chart(value, title):
    return rx.image(
        src=create_donut_chart(value, title),
        width="300px",
        height="300px",
    )


def results() -> rx.Component:
    CHART_COLOR = "#7F56D9"
    BACKGROUND_COLOR = "#111827"

    return rx.vstack(
        rx.heading("Resultados de Madurez Digital",
                   padding_top="1em"),

        # Main donut chart
        rx.cond(
            State.total_score != None,
            donut_chart(State.total_score, "Total"),
            rx.text("Cargando...")
        ),

        # Area scores organizados en dos vstack
        rx.vstack(
            # Usar rx.hstack con flex_wrap="wrap" en lugar de rx.wrap
            rx.hstack(
                rx.foreach(
                    State.area_scores.items(),
                    lambda item: donut_chart(item[1], item[0])
                ),
                spacing="4",
                flex_wrap="wrap",
                justify="center",
            ),

            # Radar chart
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
                    width=400,
                    height=400,
                ),
            ),
            spacing="8",
            align_items="center",
        ),

        rx.text(
            f"Nivel de Madurez: {State.maturity_level}",
            color=TextColor.PRIMARY.value,
        ),
        spacing="4",
        align_items="center",
    )
