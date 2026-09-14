def predecir_resultado(accion, duracion):
    if accion == "Combate":
        return "Victoria" if duracion > 90 else "Derrota"
    elif accion == "Exploración":
        return "Descubrimiento" if duracion > 240 else "Sin hallazgos"
    elif accion == "Interaccion Social":
        return "Mensaje enviado" if duracion >= 180 else "no hay parametro"

acciones_validas = ["Combate", "Exploración", "Interaccion Social"]

print("Ingresá la acción y los segundos (ej: Combate 120). Escribí 'salir' para terminar:\n")

while True:
    entrada = input(">> ").strip()

    if entrada.lower() == "salir":
        break

    try:
        # Se separan los dos datos directamente en las variables de la función
        minSeg = entrada.rsplit(' ', 1)

        # 1. Validación de cantidad de elementos
        if len(minSeg) < 2:
            raise ValueError("Escribiste mal la entrada: te faltó ingresar el tiempo o la acción.")

        if minSeg[0].strip() not in acciones_validas:
            raise ValueError(f"Escribiste mal la acción: '{minSeg[0].strip()}' no es una opción válida.")

        # Se envía todo de una a la función convirtiendo los segundos a entero
        resultado = predecir_resultado(minSeg[0].strip(), int(minSeg[1]))
        print(f"--> {resultado}\n")

    except ValueError as e:
        print(f"⚠️ {e}\n")