def test_grupo_04_page(client):
    assert client.get("/modulos/grupo_04/").status_code == 200

# Agregar pruebas del cálculo y de entradas inválidas cuando implementen la función.

import random
import pytest
from ..logic import calcular_cupos_disponibles

def test_caso_valido_aleatorio():
    ocupados = random.randint(0, 100)

    resultado = calcular_cupos_disponibles(ocupados)

    assert resultado == 100 - ocupados
    assert resultado >= 0


def test_caso_limite_aleatorio():
    ocupados = 100

    resultado = calcular_cupos_disponibles(ocupados)

    assert resultado == 0


def test_caso_invalido_cupos_excedidos_aleatorio():
    ocupados = random.randint(101, 200)

    with pytest.raises(
        ValueError,
        match="Los cupos ocupados no pueden superar la capacidad total."
    ):
        calcular_cupos_disponibles(ocupados)


def test_valores_negativos_aleatorios():
    ocupados = random.randint(-100, -1)

    with pytest.raises(
        ValueError,
        match="Los cupos ocupados no pueden ser negativos."
    ):
        calcular_cupos_disponibles(ocupados)


def test_tipos_invalidos():
    with pytest.raises(
        ValueError,
        match="Los cupos ocupados deben ser un entero."
    ):
        calcular_cupos_disponibles("30")

    with pytest.raises(
        ValueError,
        match="Los cupos ocupados deben ser un entero."
    ):
        calcular_cupos_disponibles(30.5)


def test_booleano_invalido():
    with pytest.raises(
        ValueError,
        match="Los cupos ocupados deben ser un entero."
    ):
        calcular_cupos_disponibles(True)