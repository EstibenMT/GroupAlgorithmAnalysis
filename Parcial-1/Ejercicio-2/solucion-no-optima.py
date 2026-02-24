class Solution:
    """
    Complejidad y análisis del algoritmo

    - Tiempo: O(n²)  Se utilizan dos ciclos anidados que comparan
      cada elemento con los demás.

    - Espacio: O(1), no se utilizan estructuras de datos adicionales,
      únicamente variables auxiliares.

    Mejor caso:
    - O(1) si el duplicado se encuentra en las primeras posiciones y el método
      retorna inmediatamente.

    Peor caso:
    - O(n²) cuando no existen duplicados y es necesario recorrer completamente
      el arreglo comparando todos los elementos entre sí.

    Relación estructura de datos y complejidad:
    - Se trabaja directamente sobre un arreglo (lista).
    - La comparación elemento a elemento obliga a recorrer múltiples veces
      la estructura, lo que provoca la complejidad cuadrática.
    
    NOTA: Al subir el código, LeetCode marca Time Limit Exceeded porque la 
    solución usa un enfoque O(n²) (doble ciclo), y al probarla con arreglos 
    muy grandes no alcanza a ejecutarse dentro del tiempo límite definido por 
    la plataforma.
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False