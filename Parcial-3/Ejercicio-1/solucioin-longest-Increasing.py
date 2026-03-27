from typing import List

class Solution:
    """
    Estado DP:
    - dp[i] representa la longitud de la subsecuencia creciente más larga que termina en la posición i.

    Caso base:
    - dp[i] = 1 para toda posición i, porque cada elemento por sí solo forma
      una subsecuencia creciente de longitud 1.

    Complejidad y análisis del algoritmo

    Tiempo: O(n^2)
    - Para cada posición i se recorren todas las posiciones anteriores j < i.
    - En cada comparación se verifica si nums[j] < nums[i] y se actualiza dp[i].
    - Por lo tanto, la complejidad total es cuadrática.

    Espacio: O(n)
    - Se utiliza un arreglo dp de tamaño n para almacenar las soluciones parciales.

    Mejor caso:
    - O(n^2), ya que siempre se deben evaluar las combinaciones de índices.

    Peor caso:
    - O(n^2), cuando es necesario comparar cada elemento con todos los anteriores.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp para almacenar resultados intermedios.
    - Esto evita recalcular subsecuencias y reduce el problema de exponencial a cuadrático.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)