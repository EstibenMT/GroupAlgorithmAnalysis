class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Complejidad y análisis del algoritmo (Fuerza Bruta)

        - Tiempo: O(n²). Se generan todos los subarreglos posibles
          comenzando en cada posición, y se acumula la suma de forma progresiva.

        - Espacio: O(1). No se usan estructuras auxiliares relevantes.

        Mejor caso:
        - O(1) conceptual si el arreglo tiene un solo elemento.

        Peor caso:
        - O(n²) porque se revisan todos los posibles subarreglos contiguos.

        Relación estructura de datos y complejidad:
        - Se usa únicamente el arreglo original.
        - Al evaluar todas las combinaciones contiguas, el costo crece cuadráticamente.

        NOTA: Al subir el código, LeetCode marca Time Limit Exceeded porque la 
        solución usa un enfoque O(n²) (doble ciclo), y al probarla con arreglos 
        muy grandes no alcanza a ejecutarse dentro del tiempo límite definido por 
        la plataforma.
        """

        max_sum = nums[0]

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum