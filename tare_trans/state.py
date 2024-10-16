import reflex as rx


class State(rx.State):
    show_questionnaire: bool = False

    def start_questionnaire(self):
        self.show_questionnaire = True
