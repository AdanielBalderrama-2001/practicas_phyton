cancion = {
    "titulo": "Canguro",
    "artista": ["Wos"],
    "album": "Caravana",
    "duracion_segundos": 180,
    "genero": "rap y trap con elementos de hip hop",
    "lanzamiento": 2019,
    "letra_destacada": "Dice: What up? Esto pega como coca. La gente baila loca, el cuello se disloca, la droga en lo' dedo' que vaya de boca en boca sentís cómo te choca, esa vaina subió la nota",    
    "disponible_en": ["Spotify", "Apple Music", "YouTube"]
}
print("\n--- Información de la canción ---\n")
for clave, valor in cancion.items():
    # Si el valor es una lista, mostramos sus elementos unidos
    if isinstance(valor, list):
        print(f"{clave.capitalize()}: {', '.join(valor)}")
    else:
        print(f"{clave.capitalize()}: {valor}")
