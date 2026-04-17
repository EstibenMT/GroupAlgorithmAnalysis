from typing import List
class Solution:
    """
    Justificación greedy:
    - Se ordenan los intervalos por su tiempo de finalización y se selecciona
      siempre el que termina primero y no se superpone con el anterior.
    - Elegir el intervalo que finaliza antes deja más espacio disponible para
      los siguientes intervalos.
    - Esto permite maximizar la cantidad de intervalos no superpuestos y
      minimizar los intervalos que deben eliminarse.
  
    Complejidad y análisis del algoritmo

    Tiempo: O(n log n)
    - Se ordenan los intervalos por su tiempo de finalización, lo cual cuesta O(n log n).
    - Luego se recorre la lista una sola vez para verificar si cada intervalo
      se solapa o no con el último intervalo conservado, lo cual cuesta O(n).
    - Por lo tanto, la complejidad total es O(n log n).

    Espacio: O(1)
    - Solo se utilizan variables auxiliares para contar eliminaciones y almacenar
      el final del último intervalo aceptado.
    - Si no se cuenta el espacio interno usado por el ordenamiento, el espacio
      adicional del algoritmo es constante.

    Mejor caso:
    - O(n log n), porque siempre es necesario ordenar los intervalos antes de recorrerlos.

    Peor caso:
    - O(n log n), ya que incluso si todos los intervalos se superponen o ninguno se
      superpone, el ordenamiento sigue dominando el costo total.

    Relación estructura de datos y complejidad:
    - Se utiliza una lista de intervalos ordenada por el valor de finalización.
    - Este criterio permite tomar en cada paso el intervalo que deja más espacio
      disponible para los siguientes.
    - Sin ordenar por finalización, sería más dificil decidir cual intervalo conservar
      cuando ocurre un solapamiento, y se podrían requerir comparaciones más costosas.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        eliminados = 0
        fin_actual = intervals[0][1]

        for i in range(1, len(intervals)):
            inicio, fin = intervals[i]

            if inicio < fin_actual:
                eliminados += 1
            else:
                fin_actual = fin

        return eliminados
        