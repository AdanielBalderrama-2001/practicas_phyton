edad_str = input("Bienvenido a la elecciones de nuestro proximo tirano, saqueador: Ingrese su edad... ")
edad = int(edad_str)
if edad >=18:
    print ("Eres mayor de edad, puedes votar por el Capitan Lara :)")
elif edad >= 13:
    print ("Lo lamento, no puedes votar eres menor de edad")
elif edad >=5:
    print ("Eres un niño o niña.")  
else :
    print ("No puedes votar...")
