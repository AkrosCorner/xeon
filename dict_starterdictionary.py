import os
import commands

frases = {
    "hola": {
        "text": "Hola, ¿en qué te puedo ayudar?",
        "type": "ans"
    },
    "que hora es": {
        "text": commands.hora,
        "type": "command"
    },
    "pl.install": {"text": commands.pl_installator, "type": "command"}
}

exitc = {
    "adiós": "¡Adiós!",
    "hasta pronto": "¡Hasta pronto!",
    "buenas noches": "Buenas noches, que sueñes bonito.",
    "hasta mañana": "¡Hasta mañana!",
    "hasta luego": "¡Hasta luego!",
    "adiós para siempre": "Adiós, cuídate mucho.",
    "hasta la próxima": "¡Hasta la próxima vez!",
    "buen día": "¡Buen día para ti!",
    "buen fin de semana": "¡Buen fin de semana!",
    "cuídate": "Cuídate, nos vemos pronto.",

    "adios": "¡Adiós!",
    "hasta pronto": "¡Hasta pronto!",
    "buenas noches": "Buenas noches, que sueñes bonito.",
    "hasta mañana": "¡Hasta mañana!",
    "hasta luego": "¡Hasta luego!",
    "adios para siempre": "Adiós, cuídate mucho.",
    "hasta la proxima": "¡Hasta la próxima vez!",
    "buen dia": "¡Buen día para ti!",
    "buen fin de semana": "¡Buen fin de semana!",
    "cuidate": "Cuídate, nos vemos pronto."
}