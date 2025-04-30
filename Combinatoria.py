def generar_combinaciones(n, k):

    resultado = []
    
    # Función auxiliar de backtracking
    def backtrack(combinacion_actual, inicio):
        # Si la longitud de la combinación actual es igual a k, se agrega al resultado
        if len(combinacion_actual) == k:
            resultado.append(combinacion_actual.copy())
            return
        
        # Recorre todos los elementos restantes desde 'inicio' hasta 'n'
        for i in range(inicio, n):
            # Añade el elemento actual a la combinación
            combinacion_actual.append(i)
            # Llama recursivamente con el siguiente elemento como punto de inicio
            backtrack(combinacion_actual, i + 1)
            # Elimina el último elemento para explorar otras combinaciones
            combinacion_actual.pop()

    # Llama a la función auxiliar con una combinación vacía y punto de inicio en 0
    backtrack([], 0)
    return resultado

# Ejemplo de uso
n = 7  # Número total de elementos
k = 3  # Número de elementos a elegir

combinaciones = generar_combinaciones(n, k)
for comb in combinaciones:
    print(comb)
