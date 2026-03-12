from typing import List
class Solution:
    """
    Justificación greedy:
    - Se ordenan los niños por su nivel de avaricia y las galletas por tamaño.
    - Siempre se asigna la galleta más pequeña que pueda satisfacer al niño menos exigente.
    - Esto evita desperdiciar galletas grandes y permite maximizar el número de niños satisfechos.
    
    Complejidad y análisis del algoritmo

    Tiempo: O(n log n + m log m)
    - Se ordena la lista de avaricia de los niños g, lo cual cuesta O(n log n).
    - Se ordena la lista de tamaños de galletas s, lo cual cuesta O(m log m).
    - Luego se recorren ambas listas una sola vez con dos punteros, lo cual cuesta O(n + m).
    - Por lo tanto, la complejidad total es O(n log n + m log m).

    Espacio: O(1)
    - Solo se utilizan variables auxiliares para los punteros y el contador.
    - Si no se cuenta el espacio interno que puede usar el método de ordenamiento,
      el espacio adicional del algoritmo es constante.

    Mejor caso:
    - O(n log n + m log m), porque siempre es necesario ordenar ambas listas.

    Peor caso:
    - O(n log n + m log m), ya que en el peor escenario también se deben ordenar
      ambas listas y recorrerlas completamente.

    Relación estructura de datos y complejidad:
    - Se utilizan listas ordenadas y la técnica de dos punteros.
    - El ordenamiento permite emparejar eficientemente a cada niño con la galleta
      más pequeña que pueda satisfacerlo.
    - Sin ordenar, sería más costoso decidir qué galleta asignar a cada niño,
      pudiendo llegar a comparaciones innecesarias o soluciones menos eficientes.
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # puntero para niños
        j = 0  # puntero para galletas
        contentos = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                contentos += 1
                i += 1
                j += 1
            else:
                j += 1

        return contentos
        