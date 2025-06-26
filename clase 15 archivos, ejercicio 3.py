# --- Ejercicio 1: Escribir el diario desde cero (modo 'w') ---
nombre_archivo = "mi_diario.txt"

with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("Pero también es muy útil para guardar información nueva.\n")

print("¡Se ha escrito el diario correctamente en", nombre_archivo, "!")

# --- Ejercicio 2: Leer el diario (línea por línea con manejo de errores) ---

# Opción A: Leer todo de golpe (comentada)
# with open(nombre_archivo, 'r') as diario_file:
#     contenido = diario_file.read()
# print("\n--- Contenido completo del diario ---")
# print(contenido)

print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())  # Elimina espacios y saltos de línea extra
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")

# --- Ejercicio 3: Añadir nuevas entradas (modo 'a') ---
print("\nAñadiendo nuevas entradas al diario...")
with open(nombre_archivo, 'a') as diario_file:
    diario_file.write("\n--- Entrada del 20 de Junio de 2025 ---\n")
    diario_file.write("El modo 'a' es genial para no perder datos.\n")
    diario_file.write("Ahora mi diario puede crecer cada día.\n")
print("¡Nuevas entradas guardadas!")

# Verificación final: Releer el diario con Opción B (línea por línea)
print("\n--- Contenido del diario actualizado ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")

print("Adaniel Balderrama - FIN DEL PROGRAMA")  