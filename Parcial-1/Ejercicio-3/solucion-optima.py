class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Complejidad y análisis del algoritmo

        Idea:
        - Mantener el precio mínimo visto hasta el día actual (min_price).
        - Para cada día, calcular la ganancia si vendiéramos hoy: prices[i] - min_price.
        - Actualizar la mejor ganancia (max_profit).

        - Tiempo: O(n).
          Se recorre el arreglo una sola vez.

        - Espacio: O(1).
          Solo se usan dos variables: min_price y max_profit.

        Mejor caso:
        - O(1) si n <= 1 (no hay posibilidad de transacción).

        Peor caso:
        - O(n) siempre que n > 1, porque se recorre el arreglo completo una vez
          independientemente de si hay o no ganancia.

        Relación estructura de datos y complejidad:
        - Se usa un arreglo (list) y variables acumuladoras.
        - No se requiere hash map ni set porque no hay búsquedas por clave ni conteos.
        """
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit