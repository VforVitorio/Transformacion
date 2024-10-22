import reflex as rx


class CountUp(rx.Component):
    library = "react-countup"
    tag = "CountUp"

    end: rx.Var[float]
    duration: rx.Var[int] = 2


countup = CountUp.create


def animated_score(score: float) -> rx.Component:
    return countup(end=score, duration=2)
