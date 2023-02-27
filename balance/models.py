"""
Un movimiento debe tener:

1. Fecha
2. Concepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""


import csv
from datetime import date

from . import RUTA_FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.errores = []

        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        if self.fecha is None:
            fecha = "---"
        else:
            fecha = self.fecha
<<<<<<< HEAD
        return f'{self.fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}'
=======
        return f'{fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}'
>>>>>>> e5b57d513e7031589c69c0f8c5fab5e4619a4231

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    """
    Almacenar y gestionar la lista con todos los movimientos
    """

    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                mov = Movimiento(
                    fila["fecha"],
                    fila["concepto"],
                    fila["ingreso_gasto"],
                    fila["cantidad"])
<<<<<<< HEAD
                self.lista_movimientos.append(mov)


def __str__(self):
    """Pinta la lista de movimientos por pantalla (consola)
    """
    if len(self.movimientos) > 0:
        resultado = ""
        for mov in self.movimientos:
            resultado += f"{mov}\n"
    else:
        resultado = "La lista de movimientos esta vacia"




def __repr__(self):
    conteo = len(self.movimientos)
    return f"Lista de movimientos con {conteo} movimientos"
=======
                self.movimientos.append(mov)

    def __str__(self):
        """
        Pinta la lista de movimientos por pantalla (consola)
        """
        if len(self.movimientos) > 0:
            resultado = ""
            for mov in self.movimientos:
                resultado += f'{mov}\n'
        else:
            resultado = 'La lista de movimientos está vacía'
        return resultado

    def __repr__(self):
        conteo = len(self.movimientos)
        return f'Lista de movimientos con {conteo} movimientos'
>>>>>>> e5b57d513e7031589c69c0f8c5fab5e4619a4231
