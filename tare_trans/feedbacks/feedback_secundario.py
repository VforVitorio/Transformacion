"""
Archivo donde se definen los feedbacks correspondientes al sector secundario
    - Diccionarios por cada area
        - Clave: rango de porcentaje 
        - Valor: feedback correspondiente a ese intervalo de porcentaje
    - Diccionario de sector
        - Clave: nombre de cada area
        - Valor: llamada al dicccionario correspondiente a ese area

"""


# CREACIÓN DE DICCIONARIOS POR CADA ÁREA
estrategia_feedback = {
    "0-25": "La estrategia digital no está clara o falta alineación con los objetivos productivos. Recomendamos iniciar con una estrategia básica que se enfoque en mejorar la eficiencia y reducir los costos de producción mediante tecnologías digitales. Formar al liderazgo sobre las oportunidades de la digitalización en manufactura podría ser un primer paso.",

    "26-50": "Existen objetivos digitales, pero la implementación es irregular. Recomendamos fortalecer la alineación de la estrategia digital con objetivos clave, como el control de calidad y la optimización de la cadena de suministro. La capacitación del liderazgo en metodologías digitales aplicadas al sector productivo puede mejorar los resultados.",

    "51-75": "La estrategia digital está bien definida y alineada, pero la ejecución es inconsistente. Te sugerimos mejorar la supervisión de los proyectos digitales y adoptar un enfoque de mejora continua en áreas como eficiencia de producción y control de calidad.",

    "76-100": "Excelente integración de la estrategia digital con los objetivos del negocio. Para mantener este nivel, asegúrate de actualizar la estrategia según los cambios en la demanda del mercado y las innovaciones tecnológicas, especialmente en automatización y mantenimiento predictivo."
}

cultura_feedback = {
    "0-25": "La cultura digital es limitada y hay resistencia al cambio. Inicia una formación básica en habilidades digitales, centrándote en tecnología para mejorar la productividad, como el manejo de maquinaria avanzada y técnicas de control de calidad digitalizadas.",

    "26-50": "Se han tomado pasos iniciales hacia una cultura digital, pero persiste resistencia. Aumenta la inversión en desarrollo de habilidades y capacitación en tecnología de producción. Un enfoque en adopción de maquinaria digital y automatización puede mejorar la aceptación del cambio.",

    "51-75": "Buena adopción de herramientas digitales, aunque con margen para optimizar. Introducir programas específicos de capacitación en nuevas tecnologías, como IA aplicada a la producción y control de calidad, ayudará a mejorar la colaboración digital en el equipo de manufactura.",

    "76-100": "La cultura y las habilidades digitales están bien integradas. Para mantener esta fortaleza, introduce programas avanzados de formación continua en mantenimiento predictivo y tecnologías de control, asegurando una mejora continua en el entorno de trabajo."
}

procesos_feedback = {
    "0-25": "La digitalización de procesos es baja, afectando la eficiencia. Comienza digitalizando procesos básicos, como la monitorización de la maquinaria y la gestión de inventarios. Implementar tecnologías como sensores y sistemas de control puede reducir el tiempo de inactividad y mejorar la seguridad.",

    "26-50": "Algunos procesos están parcialmente digitalizados. Aumenta la digitalización en áreas clave, como la gestión de la producción y la cadena de suministro. El uso de sistemas ERP (planificación de recursos empresariales) para integrar datos de producción y optimizar los recursos reducirá errores y mejorará la eficiencia.",

    "51-75": "Buen avance en la digitalización, aunque no del todo optimizado. Implementar técnicas de análisis de datos para anticipar la demanda y planificar el mantenimiento preventivo mejorará la eficiencia y reducirá costos operativos.",

    "76-100": "La digitalización de procesos es avanzada y eficiente. Para seguir mejorando, adopta herramientas de análisis predictivo en tiempo real para ajustar la producción a la demanda y reducir costos de mantenimiento, maximizando la productividad en cada etapa."
}

tecnologia_feedback = {
    "0-25": "Actualmente, la tecnología avanzada y la gestión de datos son mínimas. Comienza introduciendo tecnología básica de recopilación de datos en puntos críticos de producción, y usa estos datos para ajustar los procesos y reducir errores.",

    "26-50": "La tecnología avanzada se usa de manera limitada. Mejora la integración de tecnologías como IoT y la centralización de datos en áreas clave para obtener una vista completa del flujo de producción y optimizar la toma de decisiones.",

    "51-75": "Buena integración de tecnología avanzada y gestión de datos en algunos procesos. Implementar herramientas de análisis de datos para la optimización de la cadena de suministro y el mantenimiento predictivo ayudará a optimizar los recursos.",

    "76-100": "Excelente integración tecnológica y manejo de datos. Mantén esta fortaleza evaluando e implementando nuevas tecnologías que mejoren aún más la eficiencia en producción y aumenten la visibilidad de la cadena de suministro."
}

experiencia_feedback = {
    "0-25": "La estrategia digital centrada en el cliente es limitada. Te recomendamos implementar un sistema básico de CRM (Gestión de las Relaciones con los Clientes) que gestione mejor la comunicación con el cliente y optimice la respuesta a pedidos y consultas.",

    "26-50": "Existen algunos canales para la comunicación con el cliente, pero son básicos y no están integrados. Te sugerimos mejorar estos canales e integrar sistemas de gestión de pedidos para una respuesta más rápida y eficiente en la atención al cliente.",

    "51-75": "Buen progreso en la experiencia del cliente, aunque se puede optimizar. Introduce herramientas de personalización de pedidos y sistemas de seguimiento en tiempo real, mejorando la visibilidad y satisfaciendo la demanda de los clientes.",

    "76-100": "Excelente experiencia del cliente en todos los puntos de contacto. Para mantener este nivel, continúa personalizando la experiencia del cliente con datos en tiempo real, asegurando que cada interacción mejore la satisfacción y refuerce la relación comercial."
}


# CREACIÓN DEL DICCIONARIO PRINCIPAL
secundario_feedback = {
    "Estrategia y Liderazgo Digital": estrategia_feedback,
    "Cultura y Habilidades Digitales": cultura_feedback,
    "Procesos y operaciones": procesos_feedback,
    "Tecnología y datos": tecnologia_feedback,
    "Experiencia del Cliente": experiencia_feedback
}
