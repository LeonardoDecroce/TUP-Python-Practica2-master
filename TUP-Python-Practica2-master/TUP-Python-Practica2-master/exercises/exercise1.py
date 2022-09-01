"""Bloque IF, operadores lógicos, función max y operador ternario."""


def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor.

    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
    """


# NO MODIFICAR - INICIO
def maximo_basico(a: float, b: float) -> float:
    if a > b:
        return a
    if b > a:
        return b


assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """


# NO MODIFICAR - INICIO
def maximo_libreria(a: float, b: float) -> float:
    return max(a, b)


assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """


# NO MODIFICAR - INICIO
def maximo_ternario(a: float, b: float) -> float:
    numero = a if a > b else b
    return numero


assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN