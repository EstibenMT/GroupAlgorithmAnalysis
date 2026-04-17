class Solution:
    """
    Estado DP:
    - dp[i] representa la máxima cantidad de dinero que se puede robar
      considerando las casas desde la 0 hasta la i, sin robar casas adyacentes.

    Caso base:
    - dp[0] = nums[0], ya que solo hay una casa disponible.
    - dp[1] = max(nums[0], nums[1]), porque no se pueden robar ambas.

    Recurrencia:
    - Para cada casa i, existen dos opciones:
        1. No robar la casa i --> dp[i-1]
        2. Robar la casa i --> dp[i-2] + nums[i]
    - Por lo tanto:
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Complejidad y análisis del algoritmo

    Tiempo: O(n)
    - Se recorre el arreglo una sola vez desde la posición 2 hasta n.
    - En cada iteración se realiza una operación constante (max).
    - Por lo tanto, la complejidad total es lineal.

    Espacio: O(n)
    - Se utiliza un arreglo dp de tamaño n para almacenar los resultados.

    Mejor caso:
    - O(n), ya que siempre se debe recorrer el arreglo completo.

    Peor caso:
    - O(n), cuando se evalúan todas las casas del arreglo.

    Relación estructura de datos y complejidad:
    - Se utiliza un arreglo dp para almacenar soluciones parciales.
    - Esto evita recalcular subproblemas.
    - Se reduce una solución exponencial a una solución lineal.
    """
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]