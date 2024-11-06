"""
Archivo con las preguntas del sector terciario
Diccionario de diccionarios
    - Clave pregunta, valor su enunciado
    - Clave opciones, valor una lista de las 4 opciones por pregunta

"""

from typing import List, Dict, Union


# Lista de preguntas actualizada con la estructura correcta
questions_terciario: List[Dict[str, Union[str, List[str]]]] = [
    {
        "question": "¿Existe una estrategia digital clara que integre la digitalización de servicios, plataformas en línea y tecnologías emergentes (como IA y Big Data) para mejorar la experiencia del cliente?",
        "options": [
            "No hay estrategia digital.",
            "Hay una estrategia digital, pero no está bien definida ni alineada.",
            "Existe una estrategia digital definida, pero no se implementa de manera consistente.",
            "La estrategia digital está bien definida y alineada con la estrategia empresarial, pero su implementación es irregular.",
            "La estrategia digital está completamente alineada y es ejecutada de manera consistente."
        ]
    },
    {
        "question": "¿El liderazgo de la empresa está comprometido con la adopción de tecnologías digitales para mejorar la eficiencia de los servicios ofrecidos?",
        "options": [
            "No hay compromiso por parte del liderazgo.",
            "Algunos líderes muestran interés, pero no están plenamente comprometidos.",
            "El liderazgo reconoce la importancia de la transformación digital, pero no actúa activamente.",
            "El liderazgo está comprometido, pero hay falta de coherencia en la ejecución.",
            "El liderazgo está altamente comprometido y lidera activamente la transformación."
        ]
    },
    {
        "question": "¿Se asignan recursos adecuados para la digitalización de servicios, incluyendo plataformas en línea, infraestructura tecnológica y capacitación del personal?",
        "options": [
            "No se asignan recursos.",
            "Los recursos asignados son insuficientes.",
            "Los recursos asignados son adecuados, pero no siempre se utilizan eficientemente.",
            "Los recursos son suficientes y están bien utilizados.",
            "Los recursos son adecuados y están perfectamente alineados con los objetivos digitales."
        ]
    },
    {
        "question": "¿La empresa mide el impacto de sus iniciativas digitales en la mejora de la experiencia del cliente y la eficiencia operativa?",
        "options": [
            "No se mide.",
            "Se miden resultados aislados.",
            "Se miden algunos resultados, pero no de manera consistente.",
            "Se miden resultados clave, pero no siempre se actúa sobre ellos.",
            "Se miden, analizan y actúan regularmente sobre los resultados."
        ]
    },
    {
        "question": "¿Existen métricas claras para evaluar el éxito de las plataformas digitales, aplicaciones móviles y servicios en línea?",
        "options": [
            "No hay métricas definidas.",
            "Hay métricas, pero no están bien definidas.",
            "Hay métricas claras, pero no se utilizan de manera efectiva.",
            "Las métricas están claras y se usan parcialmente.",
            "Las métricas están claras y se utilizan para guiar la toma de decisiones."
        ]
    },



    {
        "question": "¿La empresa fomenta una cultura abierta al cambio y la adopción de tecnologías digitales para mejorar la oferta de servicios?",
        "options": [
            "No existe apertura al cambio.",
            "Hay resistencia significativa al cambio.",
            "Hay cierta apertura, pero aún persiste resistencia.",
            "La empresa fomenta el cambio, pero algunos sectores aún se resisten.",
            "Existe una cultura de cambio y se promueve activamente la innovación."
        ]
    },
    {
        "question": "¿Se invierte en el desarrollo de habilidades digitales para el personal en áreas como la gestión de plataformas en línea, atención al cliente digital y análisis de datos?",
        "options": [
            "No se invierte en formación digital.",
            "Se invierte de manera limitada.",
            "Se ofrece formación, pero no es accesible a todos los empleados.",
            "Se invierte en programas regulares de formación digital para algunos empleados.",
            "Hay un plan integral de desarrollo de habilidades digitales para todos los empleados."
        ]
    },
    {
        "question": "¿Se incentiva la adopción de herramientas digitales para mejorar la prestación de servicios en todos los niveles de la empresa?",
        "options": [
            "No se incentiva el uso de herramientas digitales.",
            "Se incentiva el uso solo en ciertos departamentos.",
            "Se incentiva el uso, pero no de manera proactiva.",
            "Se promueve el uso de herramientas digitales en la mayoría de los departamentos.",
            "Se fomenta activamente la adopción digital en toda la organización."
        ]
    },
    {
        "question": "¿La empresa tiene un enfoque en la colaboración digital para ofrecer servicios integrados y mejorar la atención al cliente?",
        "options": [
            "No hay herramientas o políticas de colaboración digital.",
            "Hay herramientas, pero no se usan de manera efectiva.",
            "Se promueve la colaboración digital en algunos equipos.",
            "La mayoría de los equipos utiliza herramientas digitales para colaborar.",
            "La colaboración digital está totalmente integrada en la cultura organizacional."
        ]
    },
    {
        "question": "¿Los empleados tienen acceso a herramientas digitales que faciliten la colaboración, gestión de servicios y comunicación en línea?",
        "options": [
            "No tienen las herramientas necesarias.",
            "Tienen algunas herramientas, pero no son suficientes.",
            "Las herramientas están disponibles, pero no siempre son las adecuadas.",
            "Las herramientas son adecuadas, pero no todos los empleados las usan.",
            "Todos los empleados tienen acceso a las herramientas digitales necesarias."
        ]
    },

    {
        "question": "¿Los procesos clave para la prestación de servicios están digitalizados para mejorar la eficiencia y calidad?",
        "options": [
                    "No han sido digitalizados.",
                    "Algunos procesos están parcialmente digitalizados.",
                    "Los procesos clave están digitalizados, pero su eficiencia es baja.",
                    "La mayoría de los procesos clave están digitalizados de forma efectiva.",
                    "Todos los procesos clave están completamente digitalizados y optimizados."
        ]
    },
    {
        "question": "¿Se utilizan tecnologías avanzadas (IA, Big Data, RPA) para mejorar la eficiencia operativa y la calidad de los servicios ofrecidos?",
        "options": [
                    "No se utilizan.",
                    "Se utilizan en algunos procesos, pero de manera limitada.",
                    "Se están implementando, pero de forma parcial.",
                    "Las tecnologías avanzadas están integradas en la mayoría de los procesos.",
                    "Las tecnologías avanzadas están completamente implementadas y generan mejoras significativas."
        ]
    },
    {
        "question": "¿Se realizan análisis de datos para optimizar la gestión y prestación de servicios?",
        "options": [
                    "No se realizan análisis de datos.",
                    "Se analizan datos, pero no se usan para mejorar procesos.",
                    "Los análisis se utilizan en algunos procesos.",
                    "Se utiliza análisis de datos para optimizar la mayoría de los procesos.",
                    "El análisis de datos está completamente integrado en la toma de decisiones operativas."
        ]
    },
    {
        "question": "¿Los equipos de servicio están alineados y coordinados para ofrecer una experiencia digital consistente y de alta calidad al cliente?",
        "options": [
                    "No hay coordinación.",
                    "Hay coordinación en algunos equipos, pero es limitada.",
                    "Los equipos trabajan coordinadamente en algunos procesos.",
                    "La mayoría de los equipos está alineada y colabora en los procesos digitales.",
                    "Los equipos están totalmente alineados y optimizan sus esfuerzos mediante procesos digitales."
        ]
    },
    {
        "question": "¿Los sistemas de la empresa son escalables y flexibles para adaptarse a la demanda de servicios digitales?",
        "options": [
                    "No permiten escalabilidad ni flexibilidad.",
                    "Los sistemas son escalables en algunas áreas, pero limitados en otras.",
                    "Los sistemas son parcialmente escalables y flexibles.",
                    "Los sistemas son escalables, pero necesitan ajustes continuos.",
                    "Los sistemas son altamente escalables y flexibles, alineados con las necesidades del crecimiento."
        ]
    },


    {
        "question": "¿La empresa utiliza tecnologías de vanguardia (nube, IA, big data, automatización) para ofrecer sus servicios?",
                    "options": [
                        "No utiliza tecnologías avanzadas.",
                        "Se utilizan algunas tecnologías, pero no están integradas.",
                        "Las tecnologías avanzadas están implementadas parcialmente.",
                        "Las tecnologías avanzadas están integradas en la mayoría de los procesos.",
                        "Las tecnologías avanzadas están completamente integradas y son el núcleo de las operaciones."
                    ]
    },
    {
        "question": "¿Se gestionan los datos de manera centralizada para ofrecer servicios personalizados a los clientes?",
                    "options": [
                        "Los datos no se gestionan centralizadamente.",
                        "La gestión de datos es limitada y no se utiliza para decisiones clave.",
                        "Los datos se gestionan parcialmente y se utilizan para algunas decisiones.",
                        "Los datos se gestionan centralizadamente y se utilizan en decisiones clave.",
                        "La gestión de datos es integral y guía las decisiones estratégicas."
                    ]
    },
    {
        "question": "¿Existen políticas y herramientas adecuadas para la seguridad y privacidad de los datos de clientes?",
                    "options": [
                        "No hay políticas ni herramientas.",
                        "Hay políticas, pero no están bien implementadas.",
                        "Las políticas y herramientas son adecuadas, pero tienen deficiencias.",
                        "Las políticas y herramientas son sólidas, pero no se aplican consistentemente.",
                        "La seguridad y privacidad de los datos es una prioridad y se garantiza mediante políticas sólidas y herramientas avanzadas."
                    ]
    },
    {
        "question": "¿Se utiliza inteligencia artificial para personalizar la experiencia del cliente y mejorar la prestación de servicios?",
                    "options": [
                        "No se usa IA ni aprendizaje automático.",
                        "Se utilizan en algunos procesos, pero no de manera significativa.",
                        "La IA y el aprendizaje automático están parcialmente implementados.",
                        "La IA y el aprendizaje automático están integrados en procesos clave.",
                        "La IA y el aprendizaje automático están completamente integrados y son críticos para las operaciones."
                    ]
    },
    {
        "question": "¿La empresa utiliza herramientas de gestión del conocimiento para compartir información y mejorar la eficiencia en la prestación de servicios?",
                    "options": [
                        "No se utilizan herramientas de gestión del conocimiento.",
                        "Las herramientas existen, pero no se utilizan efectivamente.",
                        "Las herramientas son utilizadas por algunos equipos.",
                        "La mayoría de los equipos utiliza herramientas de gestión del conocimiento.",
                        "Las herramientas de gestión del conocimiento están totalmente integradas en la cultura empresarial."
                    ]
    },


    {
        "question": "¿La empresa tiene una estrategia digital centrada en mejorar la experiencia del cliente en servicios ofrecidos a través de canales digitales?",
        "options": [
            "No hay estrategia centrada en el cliente.",
            "Existe, pero no está bien definida ni aplicada.",
            "La estrategia es clara, pero la implementación es inconsistente.",
            "La estrategia se aplica de manera regular, pero aún tiene áreas de mejora.",
            "La estrategia está claramente definida, aplicada y mejora continuamente."
        ]
    },
    {
        "question": "¿Se utilizan datos para personalizar la experiencia del cliente y ofrecer servicios relevantes?",
        "options": [
            "No se utilizan datos para personalización.",
            "Se utilizan, pero de manera limitada y no personalizada.",
            "Se utilizan parcialmente para personalización.",
            "Se utilizan para personalizar productos y servicios, pero no en todas las áreas.",
            "Los datos del cliente se utilizan para una personalización completa y coherente en todos los puntos de contacto."
        ]
    },
    {
        "question": "¿La empresa ofrece múltiples canales digitales para interactuar con clientes (ecommerce, redes sociales, apps, etc.)?",
        "options": [
            "No hay canales digitales activos.",
            "Existen algunos canales, pero no están integrados.",
            "Los canales digitales están parcialmente integrados y funcionales.",
            "La mayoría de los canales están bien integrados y optimizados.",
            "Todos los canales digitales están perfectamente integrados, ofreciendo una experiencia omnicanal."
        ]
    },
    {
        "question": "¿Se gestionan las interacciones con los clientes de manera efectiva mediante CRM u otras herramientas?",
        "options": [
            "No se utilizan herramientas para gestionar interacciones.",
            "Las herramientas existen, pero no se usan de manera efectiva.",
            "Se utilizan herramientas, pero la integración es limitada.",
            "Se gestionan las interacciones de manera efectiva en la mayoría de los casos.",
            "Las herramientas de CRM están totalmente integradas y mejoran continuamente la experiencia del cliente."
        ]
    },
    {
        "question": "¿La empresa recoge y actúa sobre el feedback del cliente para mejorar servicios ofrecidos digitalmente?",
        "options": [
            "No se recoge feedback del cliente.",
            "Se recoge, pero rara vez se actúa sobre él.",
            "Se actúa sobre el feedback en algunas áreas.",
            "Se utiliza el feedback para mejorar regularmente productos.",
            "La recogida y actuación sobre el feedback es un proceso continuo que guía las decisiones estratégicas."
        ]
    },
    {
        "question": "¿Los empleados están capacitados para ofrecer un servicio al cliente digitalizado y de alta calidad?",
        "options": [
            "No hay capacitación para el servicio digital.",
            "Existe capacitación limitada.",
            "Los empleados están parcialmente capacitados.",
            "La mayoría de los empleados recibe capacitación regular.",
            "Todos los empleados reciben formación continua para ofrecer un excelente servicio digital."
        ]
    },
    {
        "question": "¿Se utilizan chatbots o IA para mejorar la atención al cliente en servicios digitales?",
        "options": [
            "No se utilizan chatbots ni IA para la atención al cliente.",
            "Los chatbots o IA están implementados, pero con funciones limitadas.",
            "Se utilizan en algunos aspectos del servicio al cliente.",
            "Los chatbots o IA ayudan a mejorar la atención al cliente en la mayoría de las interacciones.",
            "Los chatbots y la IA están completamente integrados y son parte de la estrategia de atención al cliente."
        ]
    },
    {
        "question": "¿La empresa ofrece una experiencia de usuario coherente y atractiva en todos los puntos de contacto digitales?",
        "options": [
            "La experiencia de usuario es inconsistente y no se centra en el cliente.",
            "Hay esfuerzos para mejorar, pero la experiencia es limitada.",
            "La experiencia es coherente en algunos puntos de contacto.",
            "La mayoría de los puntos de contacto ofrecen una experiencia coherente y atractiva.",
            "Todos los puntos de contacto digitales proporcionan una experiencia excelente, centrada en el usuario."
        ]
    },
    {
        "question": "¿La empresa ofrece una experiencia de usuario coherente y atractiva en todos los puntos de contacto digitales?",
        "options": [
            "La experiencia de usuario es inconsistente y no se centra en el cliente.",
            "Hay esfuerzos para mejorar, pero la experiencia es limitada.",
            "La experiencia es coherente en algunos puntos de contacto.",
            "La mayoría de los puntos de contacto ofrecen una experiencia coherente y atractiva.",
            "Todos los puntos de contacto digitales proporcionan una experiencia excelente, centrada en el usuario."
        ]
    },
    {
        "question": "¿La empresa ha implementado procesos de automatización para responder rápidamente a las consultas de los clientes sobre servicios digitales?",
        "options": [
            "No hay procesos de automatización implementados.",
            "Hay algunos procesos de automatización, pero no son efectivos.",
            "Los procesos de automatización son efectivos en algunas áreas.",
            "La mayoría de las consultas se responden rápidamente gracias a la automatización.",
            "Todas las consultas se responden de manera rápida y eficiente gracias a la automatización."
        ]
    }
]
