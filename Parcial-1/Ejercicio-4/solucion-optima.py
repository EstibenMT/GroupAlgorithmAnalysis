class Solution:
    def stones_on_table_optimal(self, n: int, s: str) -> int:
        """
        Complejidad y análisis del algoritmo (Solución Óptima - Conteo en una pasada)

        Idea:
        - Recorrer la cadena una sola vez.
        - Cada vez que s[i] == s[i-1], significa que hay dos adyacentes iguales.
          Para corregirlo, se debe quitar al menos una de esas piedras.
        - Contamos esas ocurrencias: ese conteo es el mínimo número de piedras a eliminar.

        - Tiempo: O(n).
          Un solo recorrido del string, comparaciones O(1) por carácter.

        - Espacio: O(1).
          Solo se usa un contador.

        Mejor caso:
        - O(n) pero con 0 eliminaciones cuando no hay repetidos.

        Peor caso:
        - O(n) cuando todo es igual.

        Relación estructura de datos y complejidad:
        - Evitar eliminaciones físicas evita el costo O(n) por desplazamiento y mantiene O(n).

        Nota: el resultado obtenido en los códigos es de 46 ms y 12 KB para la solución 
        óptima (O(n)) y 62 ms y 32 KB para la solución no óptima (O(n²)). La diferencia 
        está en que al pasar de un planteamiento O(n²) a O(n) se evita el doble recorrido, 
        se hacen menos operaciones y por eso mejora el rendimiento del método.
        """
        removed = 0

        for i in range(1, n):
            if s[i] == s[i - 1]:
                removed += 1

        return removed