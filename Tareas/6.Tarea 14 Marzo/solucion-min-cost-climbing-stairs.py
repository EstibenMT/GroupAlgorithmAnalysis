class Solution:
    """
    Estado DP:
    - dp[i] representa el costo mínimo para llegar al escalón i.
    - El objetivo final es llegar a dp[n], donde n es la posición
      más allá del último escalón.

    Caso base:
    - dp[0] = 0, porque iniciar en el escalón 0 no tiene costo.
    - dp[1] = 0, porque también se puede iniciar en el escalón 1 sin costo.

    Recurrencia:
    - Para llegar al escalón i, se puede venir de:
        1. i-1 pagando cost[i-1]
        2. i-2 pagando cost[i-2]
    - Por lo tanto:
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    Complejidad y análisis del algoritmo

    Tiempo: O(n)
    - Se recorre el arreglo desde la posición 2 hasta n.
    - Cada iteración realiza operaciones constantes.
    - Por lo tanto, la complejidad total es lineal.

    Espacio: O(n)
    - Se utiliza un arreglo dp de tamaño n + 1.

    Mejor caso:
    - O(n), ya que siempre es necesario recorrer el arreglo.

    Peor caso:
    - O(n), cuando se evalúan todos los escalones.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp para almacenar los costos mínimos.
    - Esto evita recalcular subproblemas.
    - Se reduce una solución recursiva exponencial a una solución lineal.
    """
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]