"""Implementar aquí la función pequeña acordada con el ayudante."""
"""confirmación de commmit"""

"""Capacidad total y cupos ocupados. Devuelve cupos disponibles."""

def calcular_cupos_disponibles(capacidad_total, cupos_ocupados):
    if not isinstance(cupos_ocupados, int) or isinstance(cupos_ocupados, bool):
        raise ValueError("Los cupos ocupados deben ser un entero.")

    if cupos_ocupados < 0:
        raise ValueError("Los cupos ocupados no pueden ser negativos.")

    if cupos_ocupados > capacidad_total:
        raise ValueError(
            "Los cupos ocupados no pueden superar la "
            "capacidad total."
        )

    cupos_disponibles = capacidad_total - cupos_ocupados
    return cupos_disponibles
