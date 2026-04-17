class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Complejidad y análisis del algoritmo (Solución Óptima con Hash Map)

        - Tiempo: O(n). Se recorre el arreglo una sola vez.
          Cada búsqueda en el diccionario es O(1) en promedio.

        - Espacio: O(n). Se utiliza un diccionario para almacenar valores ya vistos.

        Mejor caso:
        - O(1) si la solución se encuentra en las primeras posiciones.

        Peor caso:
        - O(n) cuando se recorre todo el arreglo.

        Relación estructura de datos y complejidad:
        - Se usa un diccionario (hash map) para almacenar los valores
          y sus índices.
        - Esto evita recorrer el arreglo múltiples veces.
        """

        mapa = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in mapa:
                return [mapa[complemento], i]

            mapa[num] = i