class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Complejidad y análisis del algoritmo (Kadane)

        - Tiempo: O(n). Se recorre el arreglo una sola vez.
          En cada posición se decide si conviene continuar el subarreglo actual
          o comenzar uno nuevo desde el elemento actual.

        - Espacio: O(1). Solo se utilizan variables auxiliares.

        Mejor caso:
        - O(1) conceptual si el arreglo tiene un solo elemento.

        Peor caso:
        - O(n) porque siempre se recorre todo el arreglo una vez.

        Relación estructura de datos y complejidad:
        - Se trabaja directamente sobre el arreglo.
        - No se generan todos los subarreglos.
        - Se aprovecha la suma acumulada local para construir la mejor solución global.
        """

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum