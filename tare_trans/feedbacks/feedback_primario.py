"""
Archivo donde se definen los feedbacks correspondientes al sector primario
    - Diccionarios por cada area
        - Clave: rango de porcentaje 
        - Valor: feedback correspondiente a ese intervalo de porcentaje
    - Diccionario de sector
        - Clave: nombre de cada area
        - Valor: llamada al dicccionario correspondiente a ese area

"""


# CREACIÓN DE DICCIONARIOS POR CADA ÁREA
estrategia_feedback = {
    "0-25": "La estrategia digital es limitada o inexistente. Es crucial establecer objetivos digitales básicos que mejoren la eficiencia y sostenibilidad, como la recolección de datos meteorológicos y la automatización de procesos de riego o alimentación animal. Capacita al liderazgo en los beneficios de la tecnología para optimizar recursos y aumentar la rentabilidad.",

    "26-50": "Existe una estrategia digital básica, pero su implementación es inconsistente. Fortalece la alineación de la estrategia digital con objetivos esenciales, como la gestión de la producción y la previsión de recursos. Te recomendamos capacitar al liderazgo en tecnologías aplicadas al monitoreo y control de factores ambientales y productivos.",

    "51-75": "La estrategia digital está bien definida y se alinea con los objetivos, pero la ejecución no es constante. Mejorar la supervisión de proyectos digitales en áreas como la eficiencia del uso de agua o fertilizantes contribuirá a reducir costos y mejorar la sostenibilidad.",

    "76-100": "La estrategia digital está integrada y alineada con los objetivos del sector. Asegúrate de revisar regularmente la estrategia para incorporar avances en tecnología, como sistemas de monitoreo en tiempo real y análisis de datos climáticos, maximizando así la producción y sostenibilidad."
}

cultura_feedback = {
    "0-25": "Actualmente, la organización muestra poca apertura hacia el cambio digital. Hay una falta de apertura hacia la digitalización. Te recomendamos comenzar con la formación básica en habilidades digitales relacionadas con el sector, como el uso de GPS para planificación agrícola o herramientas de mapeo para la minería, que pueden mejorar significativamente la eficiencia.",

    "26-50": "Existen esfuerzos iniciales en formación digital. Existen pasos iniciales hacia una cultura digital, pero persiste la resistencia al cambio. Es útil aumentar la inversión en habilidades digitales y en tecnologías de control y monitoreo, ya que facilitarán la adopción de nuevas prácticas y mejorarán la aceptación del cambio.",

    "51-75": "Buena aceptación y adopción de herramientas digitales. Buena adopción de herramientas digitales, aunque aún con margen de mejora. Considera capacitar en tecnologías emergentes específicas del sector, como sensores de calidad de suelo y sistemas de telemetría en agricultura y ganadería, que pueden ayudar a optimizar la producción y reducir el desperdicio de recursos.",

    "76-100": "Excelente avance en la cultura y habilidades digitales. La cultura digital está bien integrada y las habilidades digitales son fuertes. Mantén esta fortaleza mediante formación continua en herramientas avanzadas y automatización de procesos, como el uso de drones y sensores para monitoreo y planificación."
}


procesos_feedback = {
    "0-25": "Actualmente, la organización muestra poca apertura hacia el cambio digital. Los procesos digitalizados son escasos o inexistentes, lo que limita la eficiencia. Inicia digitalizando procesos clave como la gestión de cultivos, monitoreo de ganado o control de maquinaria. La implementación de sensores y sistemas de monitoreo puede mejorar la eficiencia y permitir una toma de decisiones basada en datos.",

    "26-50": "Existen esfuerzos iniciales en formación digital. Algunos procesos están digitalizados, pero su eficiencia es limitada. Incrementa la digitalización en áreas estratégicas como el control de calidad de producción y el mantenimiento de maquinaria agrícola o minera. La adopción de sistemas de gestión de datos sobre rendimiento del suelo o condiciones ambientales mejorará la planificación.",

    "51-75": "Buena aceptación y adopción de herramientas digitales. Hay un avance en la digitalización de procesos, aunque no está completamente optimizado. Te recomendamos emplear análisis de datos para predecir y gestionar plagas, enfermedades y rendimientos de cosechas o producción animal, mejorando así la sostenibilidad y eficiencia.",

    "76-100": "Excelente avance en la cultura y habilidades digitales. La digitalización de procesos es eficiente y completa. Para seguir optimizando, introduce herramientas de análisis en tiempo real y técnicas de mantenimiento predictivo, lo que te permitirá ajustar los procesos de producción a las condiciones del mercado o clima de manera inmediata."
}


tecnologia_feedback = {
    "0-25": "Actualmente, la organización muestra poca apertura hacia el cambio digital. La adopción de tecnología avanzada y gestión de datos es muy limitada. Comienza integrando sensores básicos y recolectando datos de producción y rendimiento. La información sobre el uso de agua, fertilizantes y alimento permitirá reducir desperdicios y mejorar la sostenibilidad.",

    "26-50": "Existen esfuerzos iniciales en formación digital. La tecnología avanzada se usa de forma limitada y los datos no se aprovechan en su totalidad. Mejora la integración de tecnologías como IoT y drones en el monitoreo de cultivos y ganado. Centralizar estos datos te permitirá obtener una visión general de la producción y hacer ajustes en tiempo real.",

    "51-75": "Buena aceptación y adopción de herramientas digitales. Hay una buena integración de tecnología avanzada y se utiliza en algunos procesos. Para optimizar, implementa análisis de datos para predecir condiciones climáticas o de suelo que afecten la producción, permitiéndote hacer ajustes de manera anticipada y aumentar la eficiencia.",

    "76-100": "Excelente avance en la cultura y habilidades digitales. La integración de tecnología avanzada es excelente y la gestión de datos es sólida. Mantén esta ventaja buscando constantemente nuevas herramientas para monitoreo, recolección y análisis de datos que te permitan predecir y adaptarte a condiciones de mercado y ambientales en tiempo real."
}


experiencia_feedback = {
    "0-25": "Actualmente, la organización muestra poca apertura hacia el cambio digital. La estrategia digital centrada en el cliente es casi inexistente. Considera mejorar la comunicación con tus clientes y proveedores a través de sistemas básicos de gestión de pedidos, ofreciendo mayor transparencia sobre la disponibilidad de productos y condiciones de entrega.",

    "26-50": "Existen algunos canales de comunicación con el cliente, pero son básicos y no están integrados. Te sugerimos optimizar estos canales e implementar un sistema de gestión de pedidos y consultas para mejorar la relación con el cliente y la eficiencia en la respuesta.",

    "51-75": "La experiencia del cliente está bien desarrollada, pero se puede optimizar. Introduce herramientas para mejorar la personalización de pedidos, como plataformas de información sobre el origen y calidad del producto. Esto permite que los clientes accedan a datos específicos de los productos que consumen, aumentando la confianza y fidelidad.",

    "76-100": "Excelente experiencia del cliente en todos los puntos de contacto. Para mantener este nivel, sigue fortaleciendo la personalización de la experiencia del cliente y asegúrate de que tengan acceso a información actualizada sobre la trazabilidad, sostenibilidad y origen de los productos. La transparencia y la personalización son claves para una experiencia de cliente de alto valor en el sector primario."
}


# CREACIÓN DEL DICCIONARIO PRINCIPAL
primario_feedback = {
    "Estrategia y Liderazgo Digital": estrategia_feedback,
    "Cultura y Habilidades Digitales": cultura_feedback,
    "Procesos y operaciones": procesos_feedback,
    "Tecnología y datos": tecnologia_feedback,
    "Experiencia del Cliente": experiencia_feedback
}
