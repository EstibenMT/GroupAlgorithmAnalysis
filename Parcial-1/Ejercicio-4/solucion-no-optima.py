class Solution:
    def stones_on_table_not_optimal(self, n: int, s: str) -> int:
        """
        Complejidad y análisis del algoritmo (Solución NO Óptima - Eliminaciones en lista)

        Idea:
        - Convertir la cadena a lista para poder eliminar elementos.
        - Recorrer con un índice i:
            - Si a[i] == a[i-1], eliminar a[i].

        - Tiempo: O(n²) en el peor caso.
          Aunque el recorrido parece lineal, cada eliminación pop(i) en una lista
          desplaza los elementos siguientes, lo cual es O(n).
          se eliminan ~n elementos y cada eliminación cuesta O(n) => O(n²).

        - Espacio: O(n).
          Se crea una lista auxiliar con los caracteres.

        Mejor caso:
        - O(n) cuando no hay adyacentes iguales (ej: "RGBRGB..."), no se elimina nada
          y solo se recorre la lista una vez.

        Peor caso:
        - O(n²) cuando todos son iguales (ej: "RRRRR..."), se eliminan muchas piedras
          y cada eliminación implica desplazamientos.

        Relación estructura de datos y complejidad:
        - Usar list permite eliminar, pero pop(i) es O(n).
        - Esa operación hace que el algoritmo pueda volverse cuadrático.
        """
        a = list(s)
        removed = 0

        i = 1
        while i < len(a):
            if a[i] == a[i - 1]:
                a.pop(i)
                removed += 1
            else:
                i += 1

        return removed