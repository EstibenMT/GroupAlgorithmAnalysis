class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Complejidad y análisis del algoritmo
    
        - Tiempo: O(n). Se recorre el arreglo una sola vez y en cada iteración
          se verifica si el elemento ya existe en el set.
    
        - Espacio: O(n) en el peor caso, cuando todos los elementos son distintos
          y deben almacenarse en el set.
    
        Mejor caso:
        - O(1) si el duplicado se detecta en las primeras posiciones del arreglo.
    
        Peor caso:
        - O(n) cuando no existen duplicados y es necesario recorrer completamente
          el arreglo.
    
        Relación estructura de datos y complejidad:
        - Se utiliza un set, que internamente funciona como una tabla hash.
        - El acceso y verificación de existencia son O(1) promedio.
        - Cambiar de comparaciones directas sobre el arreglo a una estructura
          basada en hash reduce la complejidad de O(n²) a O(n).
        """      
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False