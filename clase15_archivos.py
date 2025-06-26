# Paso 1: Definimos el nombre del archivo
nombre_archivo = "mi_diario.txt"

# Paso 2 y 3: Abrimos el archivo en modo escritura y escribimos entradas de diario
with open(nombre_archivo, 'w') as diario_file:
    diario_file.write("Querido diario,\n")
    diario_file.write("Hoy aprendí sobre archivos en Python.\n")
    diario_file.write("El modo 'w' borra todo antes de escribir. ¡Qué miedo!\n")
    diario_file.write("Pero también es muy útil para guardar información nueva.\n")

# Paso 4: Confirmamos que la escritura se completó
print("¡Se ha escrito el diario correctamente en", nombre_archivo, "!")
print("Adaniel Balderrama - FIN DEL PROGRAMA")  