# 🎮 Clasificación de Acciones de Usuarios en una Plataforma de Videojuegos

**Institución**: Instituto Tecnológico Beltrán - Avellaneda.
**Carrera**: Tecnicatura en Ciencia de Datos e Inteligencia Artificial.
**Materia**: Procesamiento de Aprendizaje Automático.
**Profesora:** Yanina Escudero
**Estudiante**: Lugo Facundo
**Año Académico**: 2º Año.

---

## 📌 Introducción

En esta actividad se aplica **Aprendizaje Supervisado** para categorizar el comportamiento y los resultados de los usuarios dentro de una plataforma de videojuegos, a partir de sus métricas de sesión (acción realizada y duración de la misma).

## 🎯 Objetivos de la actividad

1. Analizar la tabla de datos que contiene registros de acciones de usuarios.
2. Identificar características relevantes para la clasificación (tipo de acción, duración, resultado, etc.).
3. Formular reglas simples del tipo "si-entonces" para clasificar las acciones.
4. Implementar las reglas en Python y probarlas con los datos.
5. Reflexionar sobre la precisión y utilidad del enfoque.

## 📊 Tabla de datos de ejemplo

| Usuario | Acción              | Duración (segundos) | Resultado       |
|---------|---------------------|----------------------|-----------------|
| user01  | Combate              | 120                  | Victoria        |
| user02  | Exploración          | 300                  | Descubrimiento  |
| user03  | Interacción social   | 180                  | Mensaje enviado |
| user04  | Combate              | 90                   | Derrota         |
| user05  | Exploración          | 240                  | Sin hallazgos   |

## 🧠 Reglas de clasificación

**⚔ Combate**
- Duración > 90s → Victoria
- Duración ≤ 90s → Derrota

**🗺 Exploración**
- Duración > 240s → Descubrimiento
- Duración ≤ 240s → Sin hallazgos

**💬 Interacción Social**
- Duración ≥ 180s → Mensaje enviado
- Duración < 180s → no hay parámetro

## 🐍(Python)

```python
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
```

## ⚙️ Cómo ejecutar el código

Podés correr el script desde una notebook de Jupyter, Google Colab, VS Code, o directamente desde la terminal.

### Requisitos previos

- Tener **Python 3** instalado (versión 3.8 o superior recomendada).
- No se necesitan librerías externas: el código usa únicamente funciones estándar de Python.

### Pasos para ejecutarlo

1. **Cloná el repositorio** (o descargalo como ZIP):
   ```bash
   git clone https://github.com/facundomatiaslugo/Clasificacion-de-Acciones-de-Usuarios-en-una-Plataforma-de-Videojuegos.git
   cd Clasificacion-de-Acciones-de-Usuarios-en-una-Plataforma-de-Videojuegos
   ```

2. **Verificá que tenés Python instalado:**
   ```bash
   python3 --version
   ```

3. **Ejecutá el script:**
   ```bash
   python3 clasificacion_acciones.py
   ```

4. **Usalo desde la consola:**
   - El programa te va a pedir que ingreses una acción y una duración en segundos, separadas por un espacio. Por ejemplo:
     ```
     >> Combate 120
     --> Victoria
     ```
   - Las acciones válidas son: `Combate`, `Exploración`, `Interaccion Social`.
   - Para salir del programa, escribí `salir`.

### Ejemplo de uso completo

```
Ingresá la acción y los segundos (ej: Combate 120). Escribí 'salir' para terminar:

>> Combate 120
--> Victoria

>> Exploración 300
--> Descubrimiento

>> Interaccion Social 180
--> Mensaje enviado

>> salir
```

## 💡 Preguntas de reflexión y análisis

### 1. ¿Qué reglas funcionaron mejor para clasificar las acciones?

Las reglas combinadas (Acción + Duración) permitieron predecir correctamente los resultados de la tabla de ejemplo, sin margen de error, ya que cada acción tiene un umbral de tiempo claro que determina el resultado.

### 2. ¿Qué limitaciones tiene este enfoque basado en reglas?

- **Rigidez en los límites:** un caso justo en el umbral (por ejemplo, 240 segundos exactos en Exploración) puede quedar mal clasificado, ya que las condiciones son estrictas (`>`, `≥`, etc.).
- **Falta de escalabilidad:** mantener manualmente cientos de condicionales para nuevas acciones o combinaciones resulta inviable a largo plazo.
- **Rigidez ante cambios:** si cambian las mecánicas del juego (nuevas acciones, nuevos tiempos), las reglas fijas dejan de ser válidas y hay que reescribir el código.

### 3. ¿Cómo se podría mejorar con Machine Learning avanzado?

- **Árboles de decisión (`DecisionTreeClassifier`):** permiten que el propio modelo encuentre automáticamente los límites numéricos óptimos de corte, en lugar de definirlos a mano.
- **Incorporación de nuevas variables:** agregar métricas adicionales como el nivel del usuario, la experiencia previa, o el horario de juego, para mejorar la precisión.
- **Evaluación con `train/test split`:** dividir los datos en conjuntos de entrenamiento y prueba para medir qué tan bien generaliza el modelo frente a usuarios nuevos que no vio antes.

## 📝 Observaciones

Este enfoque basado en reglas es un buen punto de partida para entender la lógica de clasificación, pero un modelo de Machine Learning entrenado con más datos sería más flexible, escalable y preciso a medida que el sistema crece.


