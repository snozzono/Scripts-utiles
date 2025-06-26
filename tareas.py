import math

def distribuir_tareas_prioritarias(tareas, minutos_disponibles=60):
    # Calcular ponderaciones
    ponderaciones = [
        (nombre, (horas * (preocupacion / 100)) / dias)
        for nombre, preocupacion, dias, horas in tareas
    ]
    
    total_ponderacion = sum(p for _, p in ponderaciones)
    
    # Cantidad total de intervalos (cada uno de hasta 60 minutos)
    total_intervalos = math.ceil(minutos_disponibles / 60)

    # Convertir la lógica a intervalos
    intervalos = {
        nombre: (p / total_ponderacion) * total_intervalos
        for nombre, p in ponderaciones
    }

    # Redondear los intervalos a enteros, asegurando que sumen el total
    intervalos_redondeados = {}
    suma_parcial = 0
    for nombre, cantidad in intervalos.items():
        redondeado = round(cantidad)
        intervalos_redondeados[nombre] = redondeado
        suma_parcial += redondeado

    # Ajustar si hay desfase por redondeo
    diferencia = suma_parcial - total_intervalos
    if diferencia != 0:
        # Ordenamos por el residuo decimal para ajustar de forma más justa
        ajustes = sorted(intervalos.items(), key=lambda x: x[1] % 1, reverse=(diferencia > 0))
        for i in range(abs(diferencia)):
            nombre, _ = ajustes[i % len(ajustes)]
            intervalos_redondeados[nombre] -= 1 if diferencia > 0 else -1

    # Asignar minutos a cada tarea
    tiempos = {}
    for nombre, bloques in intervalos_redondeados.items():
        tiempos[nombre] = bloques * 60

    # Ajustar el último bloque para que no se pase de los minutos disponibles
    total_distribuido = sum(tiempos.values())
    if total_distribuido > minutos_disponibles:
        diferencia = total_distribuido - minutos_disponibles
        # Restamos del último
        for nombre in reversed(tiempos):
            if tiempos[nombre] >= diferencia:
                tiempos[nombre] -= diferencia
                break

    return tiempos


def pedir_tarea():
    nombre = input("Nombre de la tarea: ")
    preocupacion = float(input("Preocupación (0 a 100): "))
    dias = float(input("¿En cuántos días se entrega?: "))
    horas = float(input("¿Cuántas horas estimas que necesitas?: "))
    return (nombre, preocupacion, dias, horas)


def main():
    print("=== Planificador de estudio diario ===")
    
    tareas = []
    
    while True:
        tarea = pedir_tarea()
        tareas.append(tarea)
        
        seguir = input("¿Quieres agregar otra tarea? (s/n): ").strip().lower()
        if seguir != "s":
            break

    minutos_totales = int(input("¿Cuántos minutos tienes hoy para estudiar?: "))
    resultados = distribuir_tareas_prioritarias(tareas, minutos_totales)

    print("\n=== Tiempo recomendado por tarea ===")
    for nombre, minutos in resultados.items():
        print(f"- {nombre}: {minutos} min")

    print(f"\nTotal distribuido: {sum(resultados.values())} min")

if __name__ == "__main__":
    main()
