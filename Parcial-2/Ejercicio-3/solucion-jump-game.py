from typing import List

class Solution:
    """
    Justificación greedy:
    - Se recorre el arreglo manteniendo la posición más lejana que se puede alcanzar.
    - Si en algún punto el índice actual supera esa posición, ya no es posible continuar.
    - Si se logra alcanzar o superar el último índice, entonces sí se puede llegar al final.

    Complejidad y análisis del algoritmo

    Tiempo: O(n)
    - Se recorre el arreglo una sola vez.
    - En cada posición solo se realiza una comparación y una actualización de la
      posición más lejana alcanzable.
    - Por lo tanto, la complejidad total es lineal.

    Espacio: O(1)
    - Solo se utiliza una variable auxiliar para almacenar la posición más lejana
      que se puede alcanzar.
    - No se emplean estructuras adicionales proporcionales al tamaño de la entrada.

    Mejor caso:
    - O(1) si desde las primeras posiciones ya se puede determinar que no es posible
      avanzar o si el arreglo tiene un solo elemento.

    Peor caso:
    - O(n) cuando es necesario recorrer todo el arreglo para verificar si se puede
      llegar al último índice.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo y una variable que guarda el máximo alcance.
    - Esto permite decidir en cada paso si la posición actual es accesible y hasta
      dónde se puede seguir avanzando.
    - Sin esta estrategia voraz, podrían evaluarse múltiples saltos posibles,
      aumentando innecesariamente el costo.
    """
    def canJump(self, nums: List[int]) -> bool:
        max_alcance = 0

        for i in range(len(nums)):
            if i > max_alcance:
                return False

            max_alcance = max(max_alcance, i + nums[i])

            if max_alcance >= len(nums) - 1:
                return True

        return True