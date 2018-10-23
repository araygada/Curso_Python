# Diccionarios
import pprint

diccionario = {}

# Le agrego una llave al diccionario

diccionario["primera_llave"] = 123
diccionario["palabra"] = "Hola"
diccionario["lista"] = ["Hola", "Adios"]
diccionario["sub_diccionario"] = {"sub_llave_uno":["elemento",123], "otra_sub_llave":15}

"""
pprint.pprint(diccionario)
print(diccionario["sub_diccionario"]["sub_llave_uno"][0])
"""

def suma(x,y):
    resultado = x + y
    return resultado

perfil = {
    "nombre": "John",
    "apellido": "Doe",
    "emails": ["john.doe@example.com",
    "doe@hotmail.com"
    ],
    "id": 112233445,
    "personal_function": suma
}

print(perfil.keys())

for key in perfil.keys():
    print(perfil[key])

    
