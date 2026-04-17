class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Complejidad y análisis del algoritmo (Fuerza Bruta)

        - Tiempo: O(n²). Se utilizan dos ciclos anidados para comparar
          cada par posible de elementos en el arreglo.

        - Espacio: O(1). No se utiliza memoria adicional significativa.

        Mejor caso:
        - O(1) si la solución se encuentra en las primeras posiciones.

        Peor caso:
        - O(n²) cuando es necesario recorrer todos los pares posibles.

        Relación estructura de datos y complejidad:
        - Se usa un arreglo simple.
        - No hay estructuras auxiliares, obliga a comparar todos los pares.
        """

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]