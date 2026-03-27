class Solution:
    """
    Estado DP:
    - dp[i] representa el número de formas de decodificar el prefijo s[0:i].

    Caso base:
    - dp[0] = 1, porque la cadena vacía tiene una forma válida de decodificación.
    - dp[1] = 1 si el primer carácter no es '0'; en caso contrario, es 0.

    Complejidad y análisis del algoritmo

    Tiempo: O(n)
    - Se recorre la cadena una sola vez desde la posición 2 hasta n.
    - En cada posición se realizan verificaciones de uno y dos dígitos en tiempo constante.
    - Por lo tanto, la complejidad total es lineal.

    Espacio: O(n)
    - Se utiliza un arreglo dp de tamaño n + 1 para almacenar el número de
      formas de decodificar cada prefijo de la cadena.

    Mejor caso:
    - O(n), ya que siempre es necesario recorrer la cadena para validar
      las decodificaciones posibles.

    Peor caso:
    - O(n), cuando se analizan todas las posiciones y en cada una se evalúan
      ambas posibilidades de decodificación.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp para guardar cuántas formas existen de decodificar
      cada prefijo de la cadena.
    - Esto evita recalcular soluciones para los mismos subproblemas.
    - Así se reduce una solución recursiva exponencial a una solución lineal.
    """
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            dos_digitos = int(s[i - 2:i])
            if 10 <= dos_digitos <= 26:
                dp[i] += dp[i - 2]

        return dp[n]