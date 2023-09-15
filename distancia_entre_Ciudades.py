import math

# Función para calcular la distancia entre dos puntos geográficos usando la fórmula de Haversine
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convertir las latitudes y longitudes de grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Diferencia de latitudes y longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calcular la distancia
    distancia = R * c

    return distancia

# Función para leer las ciudades y sus coordenadas desde la entrada estándar
def leer_ciudades():
    entrada = input().split()
    ciudades = []

    for i in range(0, len(entrada), 3):
        ciudad = entrada[i]
        latitud = float(entrada[i + 1])
        longitud = float(entrada[i + 2])
        ciudades.append((ciudad, latitud, longitud))

    return ciudades

# Función principal
def main():
    ciudades = leer_ciudades()

    for i in range(len(ciudades)):
        for j in range(i + 1, len(ciudades)):
            ciudad1, lat1, lon1 = ciudades[i]
            ciudad2, lat2, lon2 = ciudades[j]
            distancia = calcular_distancia(lat1, lon1, lat2, lon2)
            print(f"{ciudad1} {ciudad2} {distancia:.7f}")

if __name__ == "__main__":
    main()
