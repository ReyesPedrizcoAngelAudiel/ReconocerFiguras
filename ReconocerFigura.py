import json
import arbol

"""
Utilizamos next():
Función que se utiliza para obtener el siguiente elemento de un iterador.

Se usa para buscar en una lista y devolver el primer elemento que cumpla con una condición.
Si no encuentra ningún elemento, devuelve none.

Ejemplo visto en git:
numeros = [1, 3, 5, 7, 9]                               # Lista de números
resultado = next((x for x in numeros if x > 4), None)   # Buscar el primer número mayor que 4
print(resultado)                                        # Output: 5

SI CONSIDERAMOS AL NEXT COMO UN IF, ENTONCES TENDRIAMOS 5 IF´S EN TOTAL, DONDE HABIAMOS DELIMITADO 6 MAXIMO
"""

with open("clasificador.json", "r", encoding="utf-8") as f:
    clasificador = json.load(f)

arbol = clasificador["arbol"]
arbolpreguntas = clasificador["arbolpreguntas"]

preguntas_dict = {pregunta[0]: pregunta[1] for pregunta in arbolpreguntas}              # Diccionario de preguntas

def clasificar_figura():
    nodo_actual = "A"                                                                   # Nodo raíz
    
    while True:                                                                         # Verificar si el nodo actual corresponde a una figura
        rama_actual = next((rama for rama in arbol if rama[0] == nodo_actual), None)
        if rama_actual and rama_actual[2] and not rama_actual[1]:                       # Es una figura
            print("-------------------------------------------")
            print(f"La figura es: {rama_actual[2]}")
            print("-------------------------------------------")
            return
        
        pregunta = preguntas_dict.get(nodo_actual)                                      # Obtener la pregunta correspondiente al nodo actual
        if not pregunta:
            print("-------------------------------------------")
            print(f"La figura es: {nodo_actual}")
            print("-------------------------------------------")
            return
        
        respuesta = input(f"{pregunta}: ").lower()                                      # Obtener respuesta del usuario

        # Buscar la siguiente rama en el árbol
        nodo_actual = next((rama[2] for rama in arbol if rama[0] == nodo_actual and rama[1].lower() == respuesta), None)
        if not nodo_actual:
            print("Error: Respuesta no válida o nodo no encontrado. Intenta de nuevo.")
            return

def menu():                                                                             # Menu bonito
    print("-------------------------------------------")
    print("                 BIENVENIDO                ")
    print("-------------------------------------------")
    print("            Posibles respuestas:\n         ")
    print("Primer pregunta:\n| 0 | 3 | 4 | 5 | 6 | 8 |")
    print("Resto:\nS / N                              ")
    print("-------------------------------------------")

menu()
clasificar_figura()