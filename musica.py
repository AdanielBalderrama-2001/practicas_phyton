producto = {
    "marca": "Tesla",
    "modelo": "Model 3",
    "año": 2021,
    "color": "Rojo metálico",
    "placa": "XYZ-1234",
    "caracteristicas": {
        "autonomia_km": 480,
        "tipo_motor": "eléctrico",
        "puertas": 4
    }
}

print("\n--- Claves del producto ---")
for clave in producto:  # Por defecto, itera sobre las CLAVES
    print(clave)

print("\n--- Clave y Valor ---")
for clave in producto:
    valor = producto[clave]
    print(f"{clave.capitalize()}: {valor}")
