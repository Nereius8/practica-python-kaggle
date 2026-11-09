import string

# ==========================================
# PROBLEMA 1: Procesamiento de una lista
# ==========================================
def procesar_lista(lista: list[int]) -> list[int]:
    # 1. Filtramos dejando solo los números mayores o iguales a 0
    filtrados = [n for n in lista if n >= 0]
    
    # 2. Usamos set() para eliminar duplicados
    sin_duplicados = set(filtrados)
    
    # 3. Ordenamos de menor a mayor y devolvemos como lista
    return sorted(list(sin_duplicados))


# ==========================================
# PROBLEMA 2: Frecuencia de palabras
# ==========================================
def frecuencia_palabras(palabras: list[str], ruta_fichero: str) -> dict:
    # 1. Abrimos el fichero de texto y leemos su contenido en minúsculas
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        texto = f.read().lower()
    
    # 2. Eliminamos los signos de puntuación reemplazándolos por espacios
    for signo in string.punctuation:
        texto = texto.replace(signo, ' ')
    
    palabras_texto = texto.split()
    
    # 3. Contamos cuántas veces aparece cada palabra de la lista
    resultado = {}
    for palabra in palabras:
        palabra_limpia = palabra.lower()
        resultado[palabra_limpia] = palabras_texto.count(palabra_limpia)
        
    # 4. Devolvemos el diccionario ordenado alfabéticamente por clave
    return dict(sorted(resultado.items()))


# ==========================================
# PROBLEMA 3: Trabajo con conjuntos
# ==========================================
def operar_conjuntos(lista1: list[int], lista2: list[int]) -> dict:
    # Convertimos las listas a conjuntos (sets)
    set1 = set(lista1)
    set2 = set(lista2)
    
    return {
        "interseccion": list(set1.intersection(set2)),
        "union": list(set1.union(set2)),
        "diferencia_simetrica": list(set1.symmetric_difference(set2))
    }


# ==========================================
# PRUEBAS LOCALES (Para verificar que funciona)
# ==========================================
if __name__ == "__main__":
    # Prueba Problema 1
    entrada_p1 = [4, -1, 2, 4, 3, -5, 2]
    print("Prueba P1:", procesar_lista(entrada_p1))  # Debe salir [2, 3, 4]
    
    # Prueba Problema 3
    l1 = [1, 2, 3, 4]
    l2 = [3, 4, 5, 6]
    print("Prueba P3:", operar_conjuntos(l1, l2))

    # Prueba Problema 2
    palabras_a_buscar = ["python", "datos", "código", "java"]
    resultado_p2 = frecuencia_palabras(palabras_a_buscar, "texto.txt")
    print("Prueba P2:", resultado_p2)