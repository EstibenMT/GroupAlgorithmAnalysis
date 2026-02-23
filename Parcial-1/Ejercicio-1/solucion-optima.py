class Solution:
    """
    Complejidad y análisis del algoritmo (Solución Óptima con Hash Map)

    - Tiempo: O(n). Se recorren ambas cadenas simultáneamente en un solo ciclo
      utilizando zip, realizando operaciones de incremento y decremento sobre
      un diccionario. Las operaciones de inserción, búsqueda y actualización
      en un hash map son O(1) promedio, por lo que el costo total es lineal.

    - Espacio: O(n) en el peor caso, cuando todos los caracteres son distintos
      y deben almacenarse como claves en el diccionario.

    Mejor caso:
    - O(1) si las longitudes son diferentes, ya que el método retorna inmediatamente.

    Peor caso:
    - O(n) cuando es necesario recorrer completamente ambas cadenas y validar
      que todas las frecuencias queden en cero.

    Relación estructura de datos y complejidad:
    - Se utiliza un diccionario (hash map) para almacenar frecuencias.
    - El acceso por clave es O(1) promedio, lo que permite contar y descontar
      caracteres sin realizar búsquedas lineales.
    - Sustituir una lista por un hash map reduce la complejidad de O(n²) a O(n).
    """
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for cs, ct in zip(s, t):
            count[cs] = count.get(cs, 0) + 1
            count[ct] = count.get(ct, 0) - 1

        for v in count.values():
            if v != 0:
                return False
        return True