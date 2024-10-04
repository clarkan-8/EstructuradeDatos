import numpy as np

# Tamaño de la estructura de datos
TAM = 5

# Arreglo para almacenar elementos
array = np.empty(TAM, dtype=str)
# Inicializar los índices para la cola y la cola circular
frente = -1
final = -1
tope = -1

# Función para mostrar el contenido del arreglo
def recorrido():
    for i in array:
        print(f"\n\t____\n\t| {i} |")


# Implementación de la pila
def pilas(opc, ele):
    global tope

    # Opción 1: Insertar en la pila
    if opc == 1:
        if tope == TAM - 1:
            print("La pila está llena, no se puede insertar más elementos.")
        else:
            tope += 1
            array[tope] = ele
            print(f"¡Elemento '{ele}' agregado correctamente a la pila!")

    # Opción 2: Eliminar de la pila
    elif opc == 2:
        if tope == -1:
            print("No se puede realizar la eliminación, la pila está vacía.")
        else:
            print(f"¡Elemento '{array[tope]}' eliminado correctamente de la pila!")
            array[tope] = ""  # Eliminar el elemento
            tope -= 1

    # Opción 3: Mostrar la pila
    elif opc == 3:
        print("Elementos de la pila:")
        recorrido()
        print("Tope: ",tope)


# Implementación de la cola
def colas(opc):
    global frente, final

    # Opción 1: Insertar en la cola
    if opc == 1:
        ele = input("Ingrese el elemento para insertar en la cola:\n")
        if (final + 1) % TAM == frente:
            print("La cola está llena, no se puede insertar más elementos.")
        else:
            if frente == -1:  # Si la cola está vacía
                frente = 0
            final = (final + 1) % TAM
            array[final] = ele
            print(f"¡Elemento '{ele}' agregado correctamente a la cola!")

    # Opción 2: Eliminar de la cola
    elif opc == 2:
        if frente == -1:
            print("No se puede eliminar, la cola está vacía.")
        else:
            print(f"¡Elemento '{array[frente]}' eliminado correctamente de la cola!")
            array[frente] = ""
            if frente == final:
                frente = final = -1
            else:
                frente = (frente + 1) % TAM

    # Opción 3: Mostrar la cola
    elif opc == 3:
        print("Elementos de la cola:")
        recorrido()
    print("Frente: ", frente,"\nFinal: ", final)

# Implementación de la cola circular
def cola_circular(opc):
    global frente, final

    # Opción 1: Insertar en la cola circular
    if opc == 1:
        ele = input("Ingrese el elemento para insertar en la cola circular:\n")
        if (final + 1) % TAM == frente:
            print("La cola circular está llena, no se puede insertar más elementos.")
        else:
            if frente == -1:  # Si la cola circular está vacía
                frente = 0
            final = (final + 1) % TAM
            array[final] = ele
            print(f"¡Elemento '{ele}' agregado correctamente a la cola circular!")

    # Opción 2: Eliminar de la cola circular
    elif opc == 2:
        if frente == -1:
            print("No se puede eliminar, la cola circular está vacía.")
        else:
            print(f"¡Elemento '{array[frente]}' eliminado correctamente de la cola circular!")
            array[frente] = ""
            if frente == final:
                frente = final = -1
            else:
                frente = (frente + 1) % TAM

    # Opción 3: Mostrar la cola circular
    elif opc == 3:
        print("Elementos de la cola circular:")
        recorrido()
        print("Frente: ", frente, "\nFinal: ", final)


# Programa principal con menús de operación
while True:
    print("\n***************************************************\n\t\t\tMenú Principal\nOperaciones con estructuras de datos lineales\n\t\tIntegrantes del grupo:\n\n Alan Ricketts\n Isaac Vega\n**************************************************")
    print("Escoja una de las opciones:\n\n1. Pilas\n\n2. Colas\n\n3. Colas Circulares\n\n4. Salir")
    resp = input("\nIntroduzca la respuesta:\n")

    # Menú de Pilas
    if resp == "1":
        while True:
            print("Escoja una de las opciones:\n\n1. Insertar elementos a la Pila\n2. Eliminar elementos de la Pila\n3. Mostrar la Pila\n4. Retornar al menú principal")
            resp_pila = input("\nIntroduzca la respuesta:\n")
            if resp_pila == "1":
                ele = input("Ingrese el elemento para agregar a la pila:\n")
                pilas(1, ele)
            elif resp_pila == "2":
                pilas(2, None)
            elif resp_pila == "3":
                pilas(3, None)
            elif resp_pila == "4":
                break

    # Menú de Colas
    elif resp == "2":
        while True:
            print("Escoja una de las opciones:\n\n1. Insertar elementos a la Cola\n2. Eliminar elementos de la Cola\n3. Mostrar la Cola\n4. Retornar al menú principal")
            resp_cola = input("\nIntroduzca la respuesta:\n")
            if resp_cola in ["1", "2", "3"]:
                colas(int(resp_cola))
            elif resp_cola == "4":
                break

    # Menú de Colas Circulares
    elif resp == "3":
        while True:
            print("Escoja una de las opciones:\n\n1. Insertar elementos a la Cola Circular\n2. Eliminar elementos de la Cola Circular\n3. Mostrar la Cola Circular\n4. Retornar al menú principal")
            resp_cola_circular = input("\nIntroduzca la respuesta:\n")
            if resp_cola_circular in ["1", "2", "3"]:
                cola_circular(int(resp_cola_circular))
            elif resp_cola_circular == "4":
                break

    # Salir del programa
    elif resp == "4":
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción inválida. Por favor, elija una opción correcta.")
