import heapq  # Importamos heapq para manejar la cola de prioridad

# Mapa con distancias
mapa_de_lugares = {  # muestra qué lugares están conectados y cuánto cuesta ir de uno a otro
    "Casa": {"Parque": 4, "Tienda": 2},
    "Parque": {"Casa": 4, "Colegio": 3},
    "Tienda": {"Casa": 2, "Colegio": 6},
    "Colegio": {"Parque": 3, "Tienda": 6}
}

def encontrar_ruta_mas_corta(inicio, destino):  #Esta función que busca la mejor ruta
    distancias = {lugar: float('inf') for lugar in mapa_de_lugares}  # Al inicio, suponemos que todos los lugares están infinitamente lejos
    distancias[inicio] = 0

    rutas_previas = {}  # aqui es donde se guarda por dónde pasamos
    lugares_por_revisar = [(0, inicio)]  # Esta es la fila de lugares que debemos revisar, empezando por el inicio

    while lugares_por_revisar:  # Mientras tengamos lugares pendientes por revisar, seguimos buscando
        distancia_actual, lugar_actual = heapq.heappop(lugares_por_revisar)  # Sacamos el lugar más cercano de la fila para revisarlo

        if lugar_actual == destino:  # Si llegamos al destino, reconstruimos la ruta
            ruta = []  # Creamos una lista vacía para guardar la ruta
            while lugar_actual:  # Mientras haya un lugar en la cadena
                ruta.append(lugar_actual)  # Agregamos el lugar actual a la ruta
                lugar_actual = rutas_previas.get(lugar_actual)  # Nos movemos al lugar anterior (de dónde vinimos)
            return ruta[::-1], distancia_actual  # Devolvemos la ruta en orden correcto (invertida) y la distancia total

        for vecino, distancia in mapa_de_lugares[lugar_actual].items():  # Revisamos todos los lugares conectados al lugar actual
            nueva_distancia = distancia_actual + distancia  # Calculamos cuánto costaría llegar al vecino pasando por aquí
            if nueva_distancia < distancias[vecino]:  # Si este camino es mejor (más corto) que el que teníamos anotado
                distancias[vecino] = nueva_distancia  # Actualizamos la mejor distancia a ese vecino
                rutas_previas[vecino] = lugar_actual  # Anotamos que para llegar aquí, vinimos desde el lugar actual
                heapq.heappush(lugares_por_revisar, (nueva_distancia, vecino))  # Agregamos este vecino a la fila para revisarlo después

    return None, None  # Si no encontramos ruta, devolvemos None (no hay camino posible)

print("=== Sistema de Ruta Más Corta ===")  # Mostramos el título del programa
print("Lugares disponibles:")  # Informamos que vamos a mostrar los lugares del mapa
for lugar in mapa_de_lugares:  # Recorremos todos los lugares del mapa
    print("-", lugar)  # Mostramos cada lugar con un guion delante

lugar_inicio = input("\nEscribe desde dónde partes: ")  # Preguntamos al usuario dónde está actualmente
lugar_destino = input("Escribe hacia dónde vas: ")  # Preguntamos al usuario a dónde quiere ir

ruta, distancia_total = encontrar_ruta_mas_corta(lugar_inicio, lugar_destino)  #para calcular la mejor ruta

if ruta:  # Si se encontró una ruta
    print("\nLa ruta más corta es:")  # Informamos que vamos a mostrar la ruta
    print(" → ".join(ruta))  # Mostramos la ruta con flechas entre cada lugar (ej: Casa → Parque → Colegio)
    print(f"Distancia total: {distancia_total}")  # Mostramos cuánto cuesta en total el viaje
else:  # Si no se encontró ruta
    print("\nNo existe un camino entre esos lugares.")  # Informamos que no hay forma de llegar de un lugar al otro
