from typing import List

class Solution:
    """
    Estado DP:
    - dp[i] indica si el prefijo s[0:i] se puede segmentar usando palabras del diccionario.

    Caso base:
    - dp[0] = True, porque la cadena vacía siempre puede formarse sin usar palabras.

    Complejidad y análisis del algoritmo

    Tiempo: O(n^3)
    - Se recorren todas las posiciones i de la cadena, lo cual cuesta O(n).
    - Para cada i se prueban todas las posiciones anteriores j, lo cual cuesta O(n).
    - En cada caso se evalúa el fragmento s[j:i], cuya obtención y comparación puede costar O(n).
    - Por lo tanto, la complejidad total es O(n^3).

    Espacio: O(n)
    - Se utiliza un arreglo dp de tamaño n + 1 para almacenar si cada prefijo
      puede segmentarse correctamente.

    Mejor caso:
    - O(n^3), ya que en esta implementación se siguen evaluando combinaciones
      de prefijos y fragmentos de la cadena.

    Peor caso:
    - O(n^3), cuando es necesario revisar múltiples particiones posibles para
      determinar si la cadena puede segmentarse.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp para guardar el estado de cada prefijo de la cadena.
    - Esto evita recalcular repetidamente si un prefijo ya puede segmentarse.
    - Así se reduce el problema de intentar todas las particiones de forma
      exponencial a una solución polinómica.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        palabras = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in palabras:
                    dp[i] = True
                    break

        return dp[n]