import reflex as rx
from typing import List, Dict


class State(rx.State):
    current_question: int = 0
    answers: List[str] = [""] * 35
    questions: List[Dict[str, List[str]]] = [
        {
            "question": "pregunta 1",
            "options": ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
        },
        # ... Add the remaining 34 questions here
    ]

    @rx.var
    def current_question_number(self) -> str:
        return f"Pregunta {self.current_question + 1} de 35"

    @rx.var
    def progress_percentage(self) -> float:
        return (self.current_question + 1) / 35 * 100

    @rx.var
    def current_question_data(self) -> Dict[str, List[str]]:
        return self.questions[self.current_question]

    @rx.var
    def current_answer(self) -> str:
        return self.answers[self.current_question]

    @rx.var
    def is_first_question(self) -> bool:
        return self.current_question == 0

    @rx.var
    def is_last_question(self) -> bool:
        return self.current_question == 34

    def answer_question(self, answer: str):
        self.answers[self.current_question] = answer

    def next_question(self):
        if self.current_question < 34:
            self.current_question += 1

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
