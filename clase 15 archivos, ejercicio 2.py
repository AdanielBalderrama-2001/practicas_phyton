# --- Ejercicio 1: Escribir el diario ---
nombre_archivo = "mi_diario.txt"

with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("Pero también es muy útil para guardar información nueva.\n")

print("¡Se ha escrito el diario correctamente en", nombre_archivo, "!")

# --- Ejercicio 2: Leer el diario ---

# Opción A: Leer todo de golpe (comentada)
# with open(nombre_archivo, 'r') as diario_file:
#     contenido = diario_file.read()
# print("\n--- Contenido completo del diario ---")
# print(contenido)

# Opción B: Leer línea por línea con manejo de errores
print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open(nombre_archivo, 'r') as diario_file:
        for linea in diario_file:
            print(linea.strip())  # .strip() elimina los saltos de línea extra
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
print("Adaniel Balderrama - FIN DEL PROGRAMA")  