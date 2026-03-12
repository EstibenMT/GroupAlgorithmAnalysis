from typing import List
class Solution:
    """
    Justificación greedy:
    - Se ordenan los intervalos por su punto de inicio.
    - Luego se recorre la lista fusionando cada intervalo con el último si se superponen.
    - Esto permite combinar los intervalos en el momento correcto y obtener la fusión completa.

    Complejidad y análisis del algoritmo

    Tiempo: O(n log n)
    - Se ordenan los intervalos por su valor inicial, lo cual cuesta O(n log n).
    - Luego se recorre la lista una sola vez para fusionar los intervalos superpuestos,
      lo cual cuesta O(n).
    - Por lo tanto, la complejidad total es O(n log n).

    Espacio: O(n)
    - Se utiliza una lista adicional para almacenar los intervalos fusionados.
    - En el peor caso, si no hay superposiciones, se almacenan todos los intervalos.

    Mejor caso:
    - O(n log n), porque siempre es necesario ordenar los intervalos antes de fusionarlos.

    Peor caso:
    - O(n log n), ya que incluso si todos los intervalos se fusionan o ninguno se fusiona,
      el ordenamiento sigue dominando el costo total.

    Relación estructura de datos y complejidad:
    - Se utiliza una lista de intervalos ordenada por su inicio y una lista resultado.
    - El ordenamiento permite comparar cada intervalo solo con el último fusionado.
    - Sin ordenar, sería más difícil detectar correctamente las superposiciones y el
      proceso podría requerir más comparaciones.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        fusionados = [intervals[0]]

        for inicio, fin in intervals[1:]:
            ultimo_fin = fusionados[-1][1]

            if inicio <= ultimo_fin:
                fusionados[-1][1] = max(ultimo_fin, fin)
            else:
                fusionados.append([inicio, fin])

        return fusionados
        