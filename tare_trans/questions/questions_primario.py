"""
Archivo con las preguntas del sector primario
Diccionario de diccionarios
    - Clave pregunta, valor su enunciado
    - Clave opciones, valor una lista de las 4 opciones por pregunta

"""
from typing import List, Dict, Union


# Lista de preguntas actualizada con la estructura correcta
questions_primario: List[Dict[str, Union[str, List[str]]]] = [
    {
        "question": "¿Existe una estrategia digital clara que integre tecnologías agrícolas como la automatización de riego, drones o sistemas de monitoreo de cultivos?",
        "options": [
            "No hay estrategia digital",
            "Hay una estrategia digital, pero no está bien definida ni alineada",
            "Existe una estrategia digital definida, pero no se implementa de manera consistente",
            "La estrategia digital está bien definida y alineada con la estrategia empresarial, pero su implementación es irregular",
            "La estrategia digital está completamente alineada y es ejecutada de manera consistente"
        ]
    },
    {
        "question": "¿El liderazgo está comprometido con la adopción de tecnologías para mejorar la eficiencia y sostenibilidad en la producción agrícola o ganadera?",
        "options": [
            "No hay compromiso por parte del liderazgo",
            "Algunos líderes muestran interés, pero no están plenamente comprometidos",
            "El liderazgo reconoce la importancia de la transformación digital, pero no actúa activamente",
            "El liderazgo está comprometido, pero hay falta de coherencia en la ejecución",
            "El liderazgo está altamente comprometido y lidera activamente la transformación"
        ]
    },
    {
        "question": "¿Se asignan recursos adecuados para la implementación de tecnologías como sensores de suelo, software de gestión de cultivos o maquinaria automatizada?",
        "options": [
            "No se asignan recursos",
            "Los recursos asignados son insuficientes",
            "Los recursos asignados son adecuados, pero no siempre se utilizan eficientemente",
            "Los recursos son suficientes y están bien utilizados",
            "Los recursos son adecuados y están perfectamente alineados con los objetivos digitales"
        ]
    },
    {
        "question": "¿La empresa mide el impacto de las nuevas tecnologías en la productividad y reducción de costos operativos?",
        "options": [
            "No se mide",
            "Se miden resultados aislados",
            "Se miden algunos resultados, pero no de manera consistente",
            "Se miden resultados clave, pero no siempre se actúa sobre ellos",
            "Se miden, analizan y actúan regularmente sobre los resultados"
        ]
    },
    {
        "question": "¿Existen métricas claras para evaluar el impacto de tecnologías como IoT, drones, o sistemas de riego inteligentes en la producción?",
        "options": [
            "No hay métricas definidas",
            "Hay métricas, pero no están bien definidas",
            "Hay métricas claras, pero no se utilizan de manera efectiva",
            "Las métricas están claras y se usan parcialmente",
            "Las métricas están claras y se utilizan para guiar la toma de decisiones"
        ]
    },
    {
        "question": "¿La empresa fomenta una cultura abierta al cambio y la adopción de nuevas tecnologías en la agricultura o producción primaria?",
        "options": [
            "No existe apertura al cambio",
            "Hay resistencia significativa al cambio",
            "Hay cierta apertura, pero aún persiste resistencia",
            "La empresa fomenta el cambio, pero algunos sectores aún se resisten",
            "Existe una cultura de cambio y se promueve activamente la innovación"
        ]
    },
    {
        "question": "¿Se invierte en el desarrollo de habilidades digitales para el manejo de nuevas tecnologías (sensores, maquinaria automatizada) entre los empleados?",
        "options": [
            "No se invierte en formación digital",
            "Se invierte de manera limitada",
            "Se ofrece formación, pero no es accesible a todos los empleados",
            "Se invierte en programas regulares de formación digital para algunos empleados",
            "Hay un plan integral de desarrollo de habilidades digitales para todos los empleados"
        ]
    },
    {
        "question": "¿Se incentiva la adopción de tecnologías digitales para la mejora de procesos agrícolas o ganaderos en todos los niveles de la empresa?",
        "options": [
            "No se incentiva el uso de tecnologías digitales",
            "Se incentiva el uso solo en ciertos departamentos",
            "Se incentiva el uso, pero no de manera proactiva",
            "Se promueve el uso de tecnologías en la mayoría de los departamentos",
            "Se fomenta activamente la adopción digital en toda la organización"
        ]
    },
    {
        "question": "¿La empresa tiene un enfoque en la colaboración y el uso de tecnología digital para la gestión y planificación agrícola?",
        "options": [
            "No hay herramientas o políticas de colaboración digital",
            "Hay herramientas, pero no se usan de manera efectiva",
            "Se promueve la colaboración digital en algunos equipos",
            "La mayoría de los equipos utiliza herramientas digitales para colaborar",
            "La colaboración digital está totalmente integrada en la cultura organizacional"
        ]
    },
    {
        "question": "¿Los empleados tienen las herramientas necesarias para colaborar y comunicarse digitalmente en operaciones agrícolas y ganaderas?",
        "options": [
            "No tienen las herramientas necesarias",
            "Tienen algunas herramientas, pero no son suficientes",
            "Las herramientas están disponibles, pero no siempre son las adecuadas",
            "Las herramientas son adecuadas, pero no todos los empleados las usan",
            "Todos los empleados tienen acceso a las herramientas digitales necesarias"
        ]
    },

    {
        "question": "¿Los procesos clave de producción agrícola y ganadera han sido digitalizados para mejorar la eficiencia?",
        "options": [
            "No han sido digitalizados",
            "Algunos procesos están parcialmente digitalizados",
            "Los procesos clave están digitalizados, pero su eficiencia es baja",
            "La mayoría de los procesos clave están digitalizados de forma efectiva",
            "Todos los procesos clave están completamente digitalizados y optimizados"
        ]
    },
    {
        "question": "¿Se utilizan tecnologías avanzadas (sensores, drones, automatización) para optimizar los procesos de producción agrícola?",
        "options": [
            "No se utilizan",
            "Se utilizan en algunos procesos, pero de manera limitada",
            "Se están implementando, pero de forma parcial",
            "Las tecnologías avanzadas están integradas en la mayoría de los procesos",
            "Las tecnologías avanzadas están completamente implementadas y generan mejoras significativas"
        ]
    },
    {
        "question": "¿Se realizan análisis de datos para mejorar los procesos agrícolas o de producción ganadera?",
        "options": [
            "No se realizan análisis de datos",
            "Se analizan datos, pero no se usan para mejorar procesos",
            "Los análisis se utilizan en algunos procesos",
            "Se utiliza análisis de datos para optimizar la mayoría de los procesos",
            "El análisis de datos está completamente integrado en la toma de decisiones operativas"
        ]
    },
    {
        "question": "¿Los equipos están alineados y trabajan de manera coordinada en torno a procesos agrícolas digitales?",
        "options": [
            "No hay coordinación",
            "Hay coordinación en algunos equipos, pero es limitada",
            "Los equipos trabajan coordinadamente en algunos procesos",
            "La mayoría de los equipos está alineada y colabora en los procesos digitales",
            "Los equipos están totalmente alineados y optimizan sus esfuerzos mediante procesos digitales"
        ]
    },
    {
        "question": "¿Los sistemas de la empresa permiten la escalabilidad y flexibilidad para la expansión de operaciones agrícolas o ganaderas?",
        "options": [
            "No permiten escalabilidad ni flexibilidad",
            "Los sistemas son escalables en algunas áreas, pero limitados en otras",
            "Los sistemas son parcialmente escalables y flexibles",
            "Los sistemas son escalables, pero necesitan ajustes continuos",
            "Los sistemas son altamente escalables y flexibles, alineados con las necesidades del crecimiento"
        ]
    },
    {
        "question": "¿La empresa utiliza tecnologías de vanguardia (sensores IoT, análisis de datos, automatización) en sus operaciones agrícolas?",
        "options": [
            "No utiliza tecnologías avanzadas",
            "Se utilizan algunas tecnologías, pero no están integradas",
            "Las tecnologías avanzadas están implementadas parcialmente",
            "Las tecnologías avanzadas están integradas en la mayoría de los procesos",
            "Las tecnologías avanzadas están completamente integradas y son el núcleo de las operaciones"
        ]
    },
    {
        "question": "¿Se gestionan los datos de manera centralizada y se utilizan para la toma de decisiones estratégicas en producción agrícola?",
        "options": [
            "Los datos no se gestionan centralizadamente",
            "La gestión de datos es limitada y no se utiliza para decisiones clave",
            "Los datos se gestionan parcialmente y se utilizan para algunas decisiones",
            "Los datos se gestionan centralizadamente y se utilizan en decisiones clave",
            "La gestión de datos es integral y guía las decisiones estratégicas"
        ]
    },
    {
        "question": "¿Existen políticas y herramientas adecuadas para la seguridad y privacidad de los datos agrícolas?",
        "options": [
            "No hay políticas ni herramientas",
            "Hay políticas, pero no están bien implementadas",
            "Las políticas y herramientas son adecuadas, pero tienen deficiencias",
            "Las políticas y herramientas son sólidas, pero no se aplican consistentemente",
            "La seguridad y privacidad de los datos es una prioridad y se garantiza mediante políticas sólidas y herramientas avanzadas"
        ]
    },
    {
        "question": "¿Se usan sistemas de análisis predictivo para la mejora de la producción y optimización de recursos en agricultura?",
        "options": [
            "No se usan sistemas de análisis predictivo",
            "Se utilizan en algunos procesos, pero no de manera significativa",
            "El análisis predictivo está parcialmente implementado",
            "Está integrado en procesos clave para optimización",
            "El análisis predictivo está completamente integrado y es crítico para las operaciones"
        ]
    },
    {
        "question": "¿La empresa utiliza herramientas de gestión del conocimiento para compartir información y datos agrícolas?",
        "options": [
            "No se utilizan herramientas de gestión del conocimiento",
            "Las herramientas existen, pero no se utilizan efectivamente",
            "Las herramientas son utilizadas por algunos equipos",
            "La mayoría de los equipos utiliza herramientas de gestión del conocimiento",
            "Las herramientas de gestión del conocimiento están totalmente integradas en la cultura empresarial"
        ]
    },
    {
        "question": "¿La empresa tiene una estrategia digital centrada en mejorar la trazabilidad y transparencia de productos agrícolas para los clientes?",
        "options": [
            "No hay estrategia centrada en el cliente",
            "Existe, pero no está bien definida ni aplicada",
            "La estrategia es clara, pero la implementación es inconsistente",
            "La estrategia se aplica de manera regular, pero aún tiene áreas de mejora",
            "La estrategia está claramente definida, aplicada y mejora continuamente"
        ]
    },
    {
        "question": "¿Se utilizan datos para asegurar la calidad y origen de los productos agrícolas ofrecidos a los clientes?",
        "options": [
            "No se utilizan datos para la calidad y trazabilidad",
            "Se utilizan, pero de manera limitada y no transparente",
            "Se utilizan parcialmente para asegurar la calidad y origen",
            "Se utilizan para asegurar la calidad, pero no en todas las operaciones",
            "Los datos aseguran la calidad y origen de forma consistente y transparente"
        ]
    },
    {
        "question": "¿La empresa ofrece canales digitales para interactuar con los clientes (e-commerce, apps de pedidos, etc.)?",
        "options": [
            "No hay canales digitales activos",
            "Existen algunos canales, pero no están integrados",
            "Los canales digitales están parcialmente integrados y funcionales",
            "La mayoría de los canales están bien integrados y optimizados",
            "Todos los canales digitales están perfectamente integrados, ofreciendo una experiencia omnicanal"
        ]
    },
    {
        "question": "¿Se gestionan las interacciones con los clientes de manera efectiva mediante CRM u otras herramientas?",
        "options": [
            "No se utilizan herramientas para gestionar interacciones",
            "Las herramientas existen, pero no se usan de manera efectiva",
            "Se utilizan herramientas, pero la integración es limitada",
            "Se gestionan las interacciones de manera efectiva en la mayoría de los casos",
            "Las herramientas de CRM están totalmente integradas y mejoran continuamente la experiencia del cliente"
        ]
    },
    {
        "question": "¿La empresa recoge y actúa sobre el feedback del cliente para mejorar productos agrícolas?",
        "options": [
            "No se recoge feedback del cliente",
            "Se recoge, pero rara vez se actúa sobre él",
            "Se actúa sobre el feedback en algunas áreas",
            "Se utiliza el feedback para mejorar regularmente productos",
            "La recogida y actuación sobre el feedback es un proceso continuo que guía las decisiones estratégicas"
        ]
    },
    {
        "question": "¿Los empleados están capacitados para ofrecer información sobre productos agrícolas y trazabilidad a los clientes?",
        "options": [
            "No hay capacitación para el servicio digital",
            "Existe capacitación limitada",
            "Los empleados están parcialmente capacitados",
            "La mayoría de los empleados recibe capacitación regular",
            "Todos los empleados reciben formación continua para ofrecer un excelente servicio digital"
        ]
    },
    {
        "question": "¿Se utilizan chatbots o IA para mejorar la atención al cliente?",
        "options": [
            "No se utilizan chatbots ni IA para la atención al cliente",
            "Los chatbots o IA están implementados, pero con funciones limitadas",
            "Se utilizan en algunos aspectos del servicio al cliente",
            "Los chatbots o IA ayudan a mejorar la atención al cliente en la mayoría de las interacciones",
            "Los chatbots y la IA están completamente integrados y son parte de la estrategia de atención al cliente"
        ]
    },
    {
        "question": "¿La empresa ofrece una experiencia de usuario coherente y atractiva en todos los puntos de contacto digitales?",
        "options": [
            "La experiencia de usuario es inconsistente y no se centra en el cliente",
            "Hay esfuerzos para mejorar, pero la experiencia es limitada",
            "La experiencia es coherente en algunos puntos de contacto",
            "La mayoría de los puntos de contacto ofrecen una experiencia coherente y atractiva",
            "Todos los puntos de contacto digitales proporcionan una experiencia excelente, centrada en el usuario"
        ]
    },
    {
        "question": "¿La empresa ha implementado procesos de automatización para responder rápidamente a las consultas de los clientes?",
        "options": [
            "No se ha implementado automatización",
            "Hay procesos limitados de automatización",
            "Los procesos de automatización son funcionales, pero no están totalmente implementados",
            "La mayoría de las consultas se gestionan automáticamente y de manera eficiente",
            "La automatización es efectiva y ofrece respuestas rápidas a las necesidades de los clientes"
        ]
    },
    {
        "question": "¿Se realiza monitoreo continuo del comportamiento del cliente en los canales digitales para ajustar estrategias?",
        "options": [
            "No se realiza monitoreo",
            "Hay monitoreo limitado, pero no se usa para ajustar estrategias",
            "El monitoreo es parcial y se utiliza en algunas áreas",
            "Se realiza monitoreo regular y se ajustan estrategias, aunque no de manera integral",
            "El monitoreo es continuo y se realizan ajustes estratégicos basados en los datos de comportamiento del cliente"
        ]
    }
]
