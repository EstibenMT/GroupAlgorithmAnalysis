class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Complejidad y análisis del algoritmo (Programación Dinámica - Fibonacci)

        - Tiempo: O(n). Se recorre desde 1 hasta n calculando soluciones previas.

        - Espacio: O(1). Solo se almacenan dos valores anteriores.

        Mejor caso:
        - O(1) cuando n es pequeño (n = 1 o n = 2).

        Peor caso:
        - O(n) porque se construye la solución hasta n.

        Relación estructura de datos y complejidad:
        - No se usan arreglos ni estructuras complejas.
        - Se reutilizan resultados previos (subproblemas).
        """

        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1