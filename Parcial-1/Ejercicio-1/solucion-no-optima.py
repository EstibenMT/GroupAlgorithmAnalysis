class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Complejidad y análisis del algoritmo

        - Tiempo: O(n²). Se recorren n caracteres de la cadena s y, en cada iteración,
          se realiza una búsqueda lineal sobre t_list, cuya complejidad es O(n). 
          Además, la operación remove también implica un
          desplazamiento lineal de elementos. Por lo tanto, el costo total es n * n.

        - Espacio: O(n). Se crea una lista auxiliar (t_list) a partir de la cadena t,
          cuyo tamaño es proporcional al número de caracteres de entrada.

        Mejor caso:
        - O(1) si las longitudes son diferentes, ya que el algoritmo retorna inmediatamente false.

        Peor caso:
        - O(n²) cuando ambas cadenas son anagramas o cuando la diferencia se detecta
          en la última comparación, obligando a recorrer completamente las estructuras.

        Relación estructura de datos y complejidad:
        - Las operaciones de búsqueda y eliminación en una lista son O(n),
          lo que convierte el algoritmo en cuadrático.
        """
        if len(s) != len(t):
            return False
        t_list: list[str] = list(t)
        
        for ch in s:
            if ch not in t_list:
                return False    
            t_list.remove(ch)
        return True