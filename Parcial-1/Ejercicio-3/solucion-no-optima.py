class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Complejidad y análisis del algoritmo

        Idea:
        - Probar todas las parejas (i, j) con i < j y calcular la ganancia prices[j] - prices[i].

        - Tiempo: O(n²).
          Se usan dos bucles anidados:
          - El primer bucle recorre n días.
          - El segundo bucle, para cada compra, recorre hasta n días posteriores, posibles ventas.
          En total se evalúan O(n²).

        - Espacio: O(1).
          Solo se guardan variables auxiliares.

        Mejor caso:
        - O(1) si n <= 1 (arreglo con 0 o 1 elemento) porque no hay pares compra/venta.

        Peor caso:
        - O(n²) en cualquier caso con n >= 2, porque el algoritmo siempre evalúa
          todas las combinaciones posibles.

        Relación estructura de datos y complejidad:
        - Se usa únicamente un arreglo (list).
        - Como no hay estructura que permita consultas rápidas del mínimo anterior o del máximo futuro,
          se debe comparar cada precio con todos los posteriores, causando el crecimiento cuadrático.

        NOTA: Al subir el código, LeetCode marca Time Limit Exceeded porque la 
        solución usa un enfoque O(n²) (doble ciclo), y al probarla con arreglos 
        muy grandes no alcanza a ejecutarse dentro del tiempo límite definido por 
        la plataforma. 
        """
        n = len(prices)
        if n <= 1:
            return 0

        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit
        