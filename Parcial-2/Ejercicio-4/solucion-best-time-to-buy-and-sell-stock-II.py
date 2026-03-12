from typing import List

class Solution:
    """
    Justificación greedy:
    - Se recorren los precios y se suma cada incremento positivo entre días consecutivos.
    - Si el precio de hoy es mayor que el de ayer, conviene aprovechar esa ganancia.
    - Esto permite acumular todas las subidas y obtener el beneficio máximo total.

    Complejidad y análisis del algoritmo

    Tiempo: O(n)
    - Se recorre la lista de precios una sola vez.
    - En cada posición solo se compara el precio actual con el anterior y,
      si hay ganancia, se suma al beneficio total.
    - Por lo tanto, la complejidad total es lineal.

    Espacio: O(1)
    - Solo se utiliza una variable auxiliar para almacenar la ganancia acumulada.
    - No se emplean estructuras adicionales proporcionales al tamaño de la entrada.

    Mejor caso:
    - O(n), incluso si no hay ganancias, porque es necesario recorrer toda la lista
      para verificar los cambios entre días consecutivos.

    Peor caso:
    - O(n), cuando todos los precios deben analizarse y múltiples incrementos
      positivos se suman al beneficio total.

    Relación estructura de datos y complejidad:
    - Se utiliza una lista de precios y una variable acumuladora.
    - Esto permite capturar directamente cada subida entre días consecutivos.
    - Sin esta estrategia voraz, podrían evaluarse múltiples combinaciones de compra
      y venta, aumentando innecesariamente el costo.
    """
    def maxProfit(self, prices: List[int]) -> int:
        ganancia = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ganancia += prices[i] - prices[i - 1]

        return ganancia