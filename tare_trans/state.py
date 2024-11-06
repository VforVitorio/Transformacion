"""

GRUPO 05: PROYECTO DE TRANSFORMACIÓN DIGITAL

Este archivo define la lógica y peticiones asociadas a las diferentes acciones de la web
mediante el uso de una clase State, que hereda del componente de reflex rx.State.

    - variables de Reflex: sirven para actualizar el valor de diferentes componentes del backend segun las peticiones 
    - metodos de clase: metodos para establecer la logica de la aplicacion

Se trata del backend de la aplicacion. El backend puede ser encontrado en el archivo 
tare_trans.py.


"""

import reflex as rx
from typing import List, Dict, Tuple, Union
from tare_trans.questions.questions_primario import questions_primario
from tare_trans.questions.questions_secundario import questions_secundario
from tare_trans.questions.questions_terciario import questions_terciario
from tare_trans.feedbacks.feedback_primario import primario_feedback
from tare_trans.feedbacks.feedback_secundario import secundario_feedback
from tare_trans.feedbacks.feedback_terciario import terciario_feedback


class State(rx.State):
    """
    Definicion de las variables usadas en el backend
    En reflex, es importante tipar correctamente las variables para que el backend funcione correctamente
        - total_score: puntuacion total de la empresa
        - area_scores: puntuacion de la empresa en cada una de las areas definidas 
        - maturity_level: nivel de madurez digital de la empresa
        - current_question: pregunta actual del cuestionario
        - answers: respuestas del cuestionario
        - scores: puntuaciones recogidas de las respuestas
        - sector: los 3 sectores disponibles para elegir en el cuestionario
        - questions: preguntas del cuestionario
        - is_loading: booleano para saber si las preguntas se estan cargando en el cuestionario
        - current_question_data: proporciona toda la informacion referente a la pregunta actual del cuestionario
        - areas: diferentes areas de transformacion digital, con respectivos pesos y numero de preguntas donde se encuentran
    """
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
    areas: Dict[str, Dict[str, Union[str, float, range]]] = {
        "Estrategia y Liderazgo Digital": {"name": "Estrategia y Liderazgo Digital", "weight": 0.20, "questions": range(0, 5)},
        "Cultura y Habilidades Digitales": {"name": "Cultura y Habilidades Digitales", "weight": 0.20, "questions": range(5, 10)},
        "Procesos y operaciones": {"name": "Procesos y Operaciones", "weight": 0.20, "questions": range(10, 15)},
        "Tecnología y datos": {"name": "Tecnología y Datos", "weight": 0.20, "questions": range(15, 20)},
        "Experiencia del Cliente": {"name": "Experiencia del Cliente", "weight": 0.20, "questions": range(20, 30)}
    }

    @rx.var
    def current_question_number(self) -> str:
        """
        Renderiza el numero actual de la pregunta del cuestionario
        """
        return f"Pregunta {self.current_question + 1} de 30"

    @rx.var
    def progress_percentage(self) -> float:
        """
        Renderiza el porcentaje que se lleva realizado del cuestionario
        """
        return (self.current_question + 1) / 30 * 100

    @rx.var
    def current_answer(self) -> str:
        """
        Obtiene la respuesta actual que se ha dado a una de las preguntas
        """
        return self.answers[self.current_question] or ""

    @rx.var
    def radar_chart_data(self) -> list:
        """
        Prepara los datos necesarios para renderizarlos en un grafico de radar 
        """
        return [{"area": area["name"], "score": self.area_scores.get(area_key, 0)}
                for area_key, area in self.areas.items()]

    @rx.var
    def is_first_question(self) -> bool:
        """
        booleano para saber si se encuentra en la primera pregunta
        """
        return self.current_question == 0

    @rx.var
    def is_last_question(self) -> bool:
        """
        booleano para saber si se encuentra en la ultima pregunta
        """
        return self.current_question == 29

    @rx.var
    def area_feedbacks(self) -> Dict[str, str]:
        """
        Recoge los feedbacks correspondienites al sector y el intervalo de porcentaje obtenido por area

        Returns: diccionario de diccionarios con los feedbacks correspondientes al sector e intervalo
        """
        feedbacks = {}
        # Select the appropriate feedback dictionary based on sector
        if self.sector == "Sector primario":
            feedback_dict = primario_feedback
        elif self.sector == "Sector secundario":
            feedback_dict = secundario_feedback
        else:
            feedback_dict = terciario_feedback

        for area in self.areas:
            score = self.area_scores.get(area, 0)
            if score <= 25:
                range_key = "0-25"
            elif score <= 50:
                range_key = "26-50"
            elif score <= 75:
                range_key = "51-75"
            else:
                range_key = "76-100"
            feedbacks[area] = feedback_dict[area][range_key]
        return feedbacks

    def get_score_for_answer(self, answer_index: int) -> int:
        """Obtiene la puntuación basada en el índice de la respuesta seleccionada."""
        return answer_index  # En este caso, el índice corresponde directamente a la puntuación (0-4)

    def answer_question(self, answer: str):
        """
        Permite elegir una de las 4 opciones para responder la pregunta
        """
        self.answers[self.current_question] = answer
        # Calculate and store the score
        score = self.current_question_data["options"].index(answer)
        self.scores[self.current_question] = score

    def calculate_area_score(self, area_questions: range) -> Tuple[float, float]:
        """
        Calcula la puntuacion obtenida por area

        Returns: puntuacion por area junto con su porcentaje redondeado al entero mas cercano
        """
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
        """
        Permite pasar a la siguiente pregunta.
        Suma 1 a la pregunta actual hasta que sean menor a 30 preguntas.
        Si son mas, renderiza el componente para mostrar los resultados 
        """
        if self.current_question < 29:
            self.current_question += 1
            self.update_current_question()
        else:
            return self.show_results()

    def previous_question(self):
        """
        Permite volver a la pregunta anterior.
        Resta uno a la pregunta actual hasta estar en la primera
        """
        if self.current_question > 0:
            self.current_question -= 1
            self.update_current_question()

    def change_page(self):
        """
        Cambia de pagina redirigiendo a la seccion de resultados
        """
        return rx.redirect("/results", external=False)

    def show_results(self):
        """
        Llama a las funciones de calculo de puntuaciones y nivel de madurez digital

        Returns: redirige a la pagina donde se renderizan los resultados
        """
        total_score, area_scores = self.calculate_total_score()
        self.maturity_level = self.get_maturity_level(total_score)
        self.area_scores = area_scores
        self.total_score = total_score
        return rx.redirect("/results")

    def set_sector(self, sector: str):
        """
        Establece el sector elegido en el formulario.
        Contiene mensajes de depuracion en los prints
        """
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
        """
        Actualiza la pregunta actual, asegurandose de que hay datos de las preguntas
        """
        if not self.sector:
            self.current_question_data = {
                "question": "Por favor, selecciona un sector primero", "options": []}
        elif self.questions and 0 <= self.current_question < len(self.questions):
            self.current_question_data = self.questions[self.current_question]
        else:
            self.current_question_data = {
                "question": "No hay pregunta disponible", "options": []}
