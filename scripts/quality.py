"""Rubrica v1: prontezza d'uso documentata, non affidabilita' runtime."""

from __future__ import annotations

RUBRIC_VERSION = 1
CRITERIA = {
    "installation": ("Installazione o accesso", 30),
    "configuration": ("Configurazione e prerequisiti", 20),
    "tools": ("Funzionalità ed esempi", 20),
    "compatibility": ("Transport e client compatibili", 15),
    "license": ("Licenza esplicita", 10),
    "limitations": ("Limiti noti", 5),
}
STATUS_LABELS = {
    "absent": "Non documentato",
    "partial": "Parziale",
    "complete": "Completo",
}
STATUS_FACTORS = {"absent": 0, "partial": 0.5, "complete": 1}


def readiness_score(server: dict) -> float | None:
    assessment = server.get("quality")
    if not assessment or assessment["status"] == "unassessed":
        return None
    if assessment["rubric_version"] != RUBRIC_VERSION:
        raise ValueError("Versione della rubrica non supportata")
    return sum(
        weight * STATUS_FACTORS[assessment["criteria"][key]["status"]]
        for key, (_, weight) in CRITERIA.items()
    )


def readiness_label(server: dict) -> str:
    score = readiness_score(server)
    return "Non valutato" if score is None else f"{score:g}/100"


def quality_rubric() -> dict:
    return {
        "version": RUBRIC_VERSION,
        "name": "Prontezza d’uso documentata",
        "criteria": [
            {"id": key, "label": label, "weight": weight}
            for key, (label, weight) in CRITERIA.items()
        ],
        "statuses": {
            key: {"label": STATUS_LABELS[key], "factor": factor}
            for key, factor in STATUS_FACTORS.items()
        },
    }
