class Solution:
    """
    Estado DP:
    - dp[i][j] representa la longitud de la subsecuencia común más larga entre
      los primeros i caracteres de text1 y los primeros j caracteres de text2.

    Caso base:
    - dp[i][0] = 0 y dp[0][j] = 0, porque si una de las cadenas está vacía,
      la longitud de la subsecuencia común más larga es 0.

    Complejidad y análisis del algoritmo

    Tiempo: O(m * n)
    - Se recorren todos los pares de posiciones posibles entre text1 y text2.
    - En cada celda de la tabla dp se realiza una comparación y una asignación
      en tiempo constante.
    - Por lo tanto, la complejidad total es O(m * n), donde m y n son las
      longitudes de las dos cadenas.

    Espacio: O(m * n)
    - Se utiliza una matriz dp de tamaño (m + 1) x (n + 1) para almacenar
      las soluciones de los subproblemas.

    Mejor caso:
    - O(m * n), ya que siempre es necesario llenar la tabla completa.

    Peor caso:
    - O(m * n), porque se deben evaluar todas las combinaciones de prefijos
      de ambas cadenas.

    Relación estructura de datos y complejidad:
    - Se utiliza una matriz dp para guardar la mejor subsecuencia común para
      cada par de prefijos de las dos cadenas.
    - Esto evita recalcular subproblemas repetidos.
    - Así se transforma una solución recursiva exponencial en una solución
      polinómica.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]