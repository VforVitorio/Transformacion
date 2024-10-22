import reflex as rx
from typing import List, Dict


class State(rx.State):
    current_question: int = 0
    answers: List[str] = [""] * 35
    questions: List[Dict[str, List[str]]] = [
        {
            "question": "¿Cuál es el nivel de uso de tecnología en la gestión diaria de su empresa?",
            "options": ["Muy bajo", "Bajo", "Medio", "Alto"]
        },
        {
            "question": "¿Qué tan automatizados están los procesos de su empresa?",
            "options": ["No están automatizados", "Poco automatizados", "Medianamente automatizados", "Altamente automatizados"]
        },
        {
            "question": "¿Su empresa utiliza sistemas de inteligencia artificial o análisis de datos?",
            "options": ["No", "Poco", "Medianamente", "Sí, de forma avanzada"]
        },
        {
            "question": "¿Cómo califica el uso de plataformas digitales para la interacción con clientes?",
            "options": ["Nulo", "Bajo", "Moderado", "Alto"]
        },
        {
            "question": "¿Su empresa ofrece productos o servicios a través de medios digitales?",
            "options": ["No", "Poco", "Sí, algunos", "Sí, la mayoría o todos"]
        },
        {
            "question": "¿En qué medida su empresa invierte en ciberseguridad?",
            "options": ["No invierte", "Inversion mínima", "Moderada", "Alta inversión"]
        },
        {
            "question": "¿Cómo evalúa la competencia digital de sus empleados?",
            "options": ["Muy baja", "Baja", "Moderada", "Alta"]
        },
        {
            "question": "¿Su empresa fomenta la capacitación en tecnologías emergentes?",
            "options": ["No", "Poco", "Medianamente", "Sí, mucho"]
        },
        {
            "question": "¿Cuál es el nivel de integración de sistemas tecnológicos en su cadena de valor?",
            "options": ["Muy bajo", "Bajo", "Moderado", "Alto"]
        },
        {
            "question": "¿Qué tan relevante es la transformación digital en la estrategia de su empresa?",
            "options": ["Nada relevante", "Poco relevante", "Moderadamente relevante", "Muy relevante"]
        },
        {
            "question": "¿Cómo maneja su empresa la recolección y análisis de datos?",
            "options": ["No los maneja", "Poco", "Moderadamente", "De manera avanzada"]
        },
        {
            "question": "¿Su empresa utiliza tecnologías en la nube para almacenar y gestionar datos?",
            "options": ["No", "Poco", "Moderadamente", "Sí, en gran medida"]
        },
        {
            "question": "¿Cómo calificaría la agilidad de su empresa para adaptarse a nuevas tecnologías?",
            "options": ["Muy baja", "Baja", "Moderada", "Alta"]
        },
        {
            "question": "¿En qué medida su empresa colabora con terceros para desarrollar soluciones tecnológicas?",
            "options": ["No colabora", "Poco", "Moderadamente", "Colabora mucho"]
        },
        {
            "question": "¿Qué tan integrados están los sistemas de información dentro de su organización?",
            "options": ["Nada integrados", "Poco integrados", "Moderadamente integrados", "Altamente integrados"]
        },
        {
            "question": "¿Su empresa promueve la cultura de innovación digital?",
            "options": ["No", "Poco", "Moderadamente", "Sí, mucho"]
        },
        {
            "question": "¿Cómo es la relación entre el área de TI y otras áreas en cuanto a colaboración tecnológica?",
            "options": ["Inexistente", "Poca", "Moderada", "Muy colaborativa"]
        },
        {
            "question": "¿En qué grado utiliza su empresa el comercio electrónico?",
            "options": ["No lo usa", "Poco", "Moderadamente", "En gran medida"]
        },
        {
            "question": "¿Cómo calificaría el uso de soluciones tecnológicas para mejorar la experiencia del cliente?",
            "options": ["Muy bajo", "Bajo", "Moderado", "Alto"]
        },
        {
            "question": "¿Cómo califica la inversión en innovación tecnológica dentro de su empresa?",
            "options": ["Nula", "Baja", "Moderada", "Alta"]
        },
        {
            "question": "¿Cómo evalúa la infraestructura tecnológica disponible en su empresa?",
            "options": ["Muy deficiente", "Deficiente", "Adecuada", "Excelente"]
        },
        {
            "question": "¿Qué tan eficiente es la comunicación interna gracias a las herramientas digitales?",
            "options": ["Nada eficiente", "Poco eficiente", "Moderadamente eficiente", "Muy eficiente"]
        },
        {
            "question": "¿En qué medida utiliza su empresa herramientas de colaboración digital (e.g. Slack, Teams)?",
            "options": ["No las usa", "Poco", "Moderadamente", "En gran medida"]
        },
        {
            "question": "¿Su empresa ha implementado procesos de transformación digital para reducir costos?",
            "options": ["No", "Poco", "Moderadamente", "Sí, mucho"]
        },
        {
            "question": "¿Cómo maneja su empresa la gestión del cambio digital entre los empleados?",
            "options": ["No lo maneja", "Poco", "Moderadamente", "De manera avanzada"]
        },
        {
            "question": "¿Qué tan preparados están sus empleados para trabajar de forma remota usando herramientas digitales?",
            "options": ["Nada preparados", "Poco preparados", "Moderadamente preparados", "Muy preparados"]
        },
        {
            "question": "¿Cómo calificaría la seguridad digital de su empresa?",
            "options": ["Muy baja", "Baja", "Moderada", "Alta"]
        },
        {
            "question": "¿Qué tan flexible es su empresa en la adopción de nuevas tecnologías?",
            "options": ["Nada flexible", "Poco flexible", "Moderadamente flexible", "Muy flexible"]
        },
        {
            "question": "¿Su empresa utiliza software personalizado para sus operaciones?",
            "options": ["No", "Poco", "Sí, algunos procesos", "Sí, en la mayoría de los procesos"]
        },
        {
            "question": "¿Cómo gestiona su empresa la actualización de tecnologías obsoletas?",
            "options": ["No las actualiza", "Poco", "Moderadamente", "De manera constante"]
        },
        {
            "question": "¿Qué tan digitalizados están los procesos internos (e.g. facturación, recursos humanos)?",
            "options": ["Nada digitalizados", "Poco digitalizados", "Moderadamente digitalizados", "Muy digitalizados"]
        },
        {
            "question": "¿Cómo calificaría la estrategia digital de su empresa a largo plazo?",
            "options": ["Inexistente", "Poco clara", "Moderadamente clara", "Muy clara"]
        }
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
