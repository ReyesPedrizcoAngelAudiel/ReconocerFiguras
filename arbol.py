import json

arbol = [
    ["A","0","AA"],       #AA | Circulo, Elipse
    ["A","3","AB"],       #AB | Equilatero, Iscoceles, Escaleno, Recto 
    ["A","4","AC"],       #AC | Cuadrado, Rectangulo, Rombo, Trapecio
    ["A","5","AD"],       #AD | Pentagono
    ["A","6","AE"],       #AE | Hexagono
    ["A","8","AF"],       #AF | Octagono

    #Para los sin lados
    ["AA","S","Circulo"],        #Circulo
    ["AA","N","Elipse"],         #Elipse
    
    #Para los triangulos
    ["AB","S","Equilatero"],     #Equilatero
    ["AB","N","ABX"],
    ["ABX","S","Iscoseles"],     #Iscoseles
    ["ABX","N","ABXA"], 
    ["ABXA","S","Recto"],        #Recto
    ["ABXA","N","Escaleno"],     #Escaleno

    #Para los cuatro lados ptm
    ["AC","S","ACX"],
    ["AC","N","ACXA"],
    ["ACX","S","Cuadrado"],      #Cuadrado
    ["ACX","N","Rectangulo"],    #Rectangulo
    ["ACXA","S","Trapecio"],     #Trapecio
    ["ACXA","N","Rombo"],        #Rombo

    ["AD","","Pentagono"],       #Pentagono
    ["AE","","Hexagono"],        #Hexagono
    ["AF","","Octagono"]         #Octagono

]

arbolpreguntas = [
    #Para sin lados
    ["A","¿Cuantos lados tiene?"],
    ["AA","¿Tiene radio?"],

    #Para triangulos
    ["AB","¿Todos sus lados son iguales?"],
    ["ABX","¿Tiene 2 lados iguales?"],
    ["ABXA","¿Tiene un angulo de 90 grados?"],

    #Para los de cuatro lados
    ["AC","¿Todos sus angulos son de 90 grados?"],
    ["ACX","¿Todos sus lados son iguales?"],
    ["ACXA","¿Tiene base mayor?"]
]

# Diccionario con las estructuras del árbol
data = {
    "arbol": arbol,
    "arbolpreguntas": arbolpreguntas
}

# Guardar en un archivo JSON
with open("clasificador.json", "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=4)
print("Archivo clasificador.json generado.")