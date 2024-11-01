import reflex as rx
from typing import List, Dict, Tuple, Union
from tare_trans.questions.questions_primario import questions_primario
from tare_trans.questions.questions_secundario import questions_secundario
from tare_trans.questions.questions_terciario import questions_terciario


class State(rx.State):

    total_score: float = 0.0
    area_scores: Dict[str, float] = {}
    maturity_level: str = ""
    current_question: int = 0
    answers: List[str] = [""] * 30
    scores: List[int] = [0] * 30
    sector: str = ""
    questions: List[Dict[str, Union[str, List[str]]]] = []

    is_loading: bool = True
    current_question_data: Dict[str, List[str]] = {
        "question": "Por favor, selecciona un sector primero", "options": []}

    # Definición de las áreas y sus pesos
    areas = {
        "Estrategia y Liderazgo Digital": {"name": "Estrategia y Liderazgo Digital", "weight": 0.20, "questions": range(0, 5)},
        "Cultura y Habilidades Digitales": {"name": "Cultura y Habilidades Digitales", "weight": 0.20, "questions": range(5, 10)},
        "Procesos y operaciones": {"name": "Procesos y Operaciones", "weight": 0.20, "questions": range(10, 15)},
        "Tecnología y datos": {"name": "Tecnología y Datos", "weight": 0.20, "questions": range(15, 20)},
        "Experiencia del Cliente": {"name": "Experiencia del Cliente", "weight": 0.20, "questions": range(20, 30)}
    }

    def set_sector(self, sector: str):
        print("State set_sector called with:", sector)
        self.sector = sector
        print("Setting loading to True")
        self.is_loading = True
        if sector == "Sector primario":
            print("Loading primario questions")
            self.questions = questions_primario
        elif sector == "Sector secundario":
            print("Loading secundario questions")
            self.questions = questions_secundario
        elif sector == "Sector terciario":
            print("Loading terciario questions")
            self.questions = questions_terciario
        else:
            self.questions = []
        self.update_current_question()
        print("Setting loading to False")
        self.is_loading = False
        print("Sector setup completed")

    def update_current_question(self):
        if not self.sector:
            self.current_question_data = {
                "question": "Por favor, selecciona un sector primero", "options": []}
        elif self.questions and 0 <= self.current_question < len(self.questions):
            self.current_question_data = self.questions[self.current_question]
        else:
            self.current_question_data = {
                "question": "No hay pregunta disponible", "options": []}

    @rx.var
    def current_question_number(self) -> str:
        return f"Pregunta {self.current_question + 1} de 30"

    @rx.var
    def progress_percentage(self) -> float:
        return (self.current_question + 1) / 30 * 100

    @rx.var
    def current_answer(self) -> str:
        return self.answers[self.current_question] or ""

    @rx.var
    def radar_chart_data(self) -> list:
        return [{"area": area["name"], "score": self.area_scores.get(area_key, 0)}
                for area_key, area in self.areas.items()]

    @rx.var
    def is_first_question(self) -> bool:
        return self.current_question == 0

    @rx.var
    def is_last_question(self) -> bool:
        return self.current_question == 29

    def get_score_for_answer(self, answer_index: int) -> int:
        """Obtiene la puntuación basada en el índice de la respuesta seleccionada."""
        return answer_index  # En este caso, el índice corresponde directamente a la puntuación (0-4)

    def answer_question(self, answer: str):
        self.answers[self.current_question] = answer
        # Calculate and store the score
        score = self.questions[self.current_question]["options"].index(answer)
        self.scores[self.current_question] = score

    def calculate_area_score(self, area_questions: range) -> Tuple[float, float]:
        total_possible = len(area_questions) * 4
        area_score = sum(self.scores[q] for q in area_questions)
        return area_score, round((area_score / total_possible) * 100)

    def calculate_total_score(self) -> Tuple[float, Dict[str, float]]:
        """Calcula la puntuación total y por área."""
        area_scores = {}
        total_score = 0

        for area, details in self.areas.items():
            score, percentage = self.calculate_area_score(details["questions"])
            # Guardar el porcentaje directamente
            area_scores[area] = percentage
            # Aplicar el peso al porcentaje
            total_score += percentage * details["weight"]

        return total_score, area_scores

    def get_maturity_level(self, score: float) -> str:
        """Determina el nivel de madurez basado en la puntuación total."""
        if score >= 80:
            return "Optimizado"
        elif score >= 60:
            return "Gestionado"
        elif score >= 40:
            return "Definido"
        elif score >= 20:
            return "Emergente"
        else:
            return "Inicial"

    def next_question(self):
        if self.current_question < 29:
            self.current_question += 1
        else:
            return self.show_results()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1

    def change_page(self):
        return rx.redirect("/results", external=False)

    def show_results(self):
        total_score, area_scores = self.calculate_total_score()
        self.maturity_level = self.get_maturity_level(total_score)
        self.area_scores = area_scores
        self.total_score = total_score
        return rx.redirect("/results")
