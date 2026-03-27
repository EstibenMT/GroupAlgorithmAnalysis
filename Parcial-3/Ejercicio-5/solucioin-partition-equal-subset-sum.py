from typing import List

class Solution:
    """
    Estado DP:
    - dp[s] indica si es posible formar la suma s usando algunos elementos del arreglo.

    Caso base:
    - dp[0] = True, porque siempre es posible formar suma 0 sin tomar elementos.

    Complejidad y análisis del algoritmo

    Tiempo: O(n * target)
    - Primero se calcula la suma total del arreglo.
    - Luego, para cada número del arreglo, se recorren las sumas desde target
      hasta el valor del número.
    - Por lo tanto, la complejidad total es O(n * target), donde target es
      la mitad de la suma total.

    Espacio: O(target)
    - Se utiliza un arreglo dp de tamaño target + 1 para almacenar si cada suma
      es alcanzable.

    Mejor caso:
    - O(n * target), ya que en esta implementación se procesan los elementos
      y las sumas posibles necesarias para determinar la respuesta.

    Peor caso:
    - O(n * target), cuando se deben evaluar todas las combinaciones de números
      y sumas hasta target.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp de una dimensión para guardar qué sumas pueden
      formarse con los elementos procesados.
    - Esto evita recalcular subconjuntos repetidos.
    - Así se transforma un problema exponencial de subconjuntos en una solución
      pseudo-polinómica.
    """
    def canPartition(self, nums: List[int]) -> bool:
        suma_total = sum(nums)

        if suma_total % 2 != 0:
            return False

        target = suma_total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]