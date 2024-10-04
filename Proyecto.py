"""Se desea utilizar un lenguaje de programación  para
 desarrollar los algoritmos dados en clases, sobre el concepto
 de Cola Circular utilizando la estructura de datos tipo arreglo para implementarla.
 El programa debe presentar los siguientes menús, para que el usuario pueda escoger
 las operaciones deseadas"""
import numpy as np
array=np([],dtype=str)
frente=0
final=0
def recorrido():
    for i in array:
        print("\n\t ___\n\t[", i, "]")

def Pila(opc,ele, tope):#Funcion de proyedcto 1
  if opc==1:
    tope+=1
    array.append(ele)
  elif opc==2:
    array.pop()
    tope-=1
  elif opc==3:
   recorrido()

def Colas(opc,ele, frente,final):#Funcion de proyecto 2
    if opc == 1:
        frente=0
        final=0
        array.insert(len(array)-1,ele)
    if opc == 2:
        array.insert(len(array)-1,ele)
        final+=1
    elif opc == 3:
        array.remove(0)
        frente-=1
    elif opc == 4:
     recorrido()
    print("El frente: ",frente,"\nEl final: ",final)
def ColaCircular(opc,ele,frente, final):#Funcion de proyecto 3
    if opc == 1:
        frente=0
        final=0
        array.insert(len(array)-1,ele)

    elif opc == 2:
        array.remove(0)
        frente-=1
    elif opc == 3:
      recorrido()
            
while True:
    print("\n***************************************************\n\t\t\tMenu Principal\nOperaciones con estructuras de datos lineales\n\t\tIntegrantes del grupo:\n\n Alan Ricketts\n Isaac Vega\n**************************************************")
    print("Escoja una de las opciones:\n\nPilas\n\n2.Colas\n\n3.Colas Circulares\n\n")
    resp=input("\nIntroduzca la respuesta:\n")
    #--------------------------------------------------------------------------------
    while True:#Proyecto 1
        print("Escoja una de las opciones:\n\n1.Insertar elementos a la Pila\n\n2.Eliminar elementos de la Pila\n\n3.Mostrar la Pila\n\n4.Retornar al menu principal")
        resp=input("\n\nIntroduzca la respuesta:\n")
    # --------------------------------------------------------------------------------
    while True:#Proyecto 2
        print("Escoja una de las opciones:\n\n1.Insertar elementos a la cola \n\n2.Eliminar elementos de la cola \n\n3.Mostrar la Cola \n\n4.Retornar al menu principal")
        resp=input("\n\nIntroduzca la respuesta:\n")

    # --------------------------------------------------------------------------------
    while True:#Proyecto 3
        print("Escoja una de las opciones:\n\n1.Insertar elementos a la cola circular\n\n2.Eliminar elementos de la cola Circular\n\n3.Mostrar la Cola Circular\n\n4.Retornar al menu principal")
        resp=input("\n\nIntroduzca la respuesta:\n")
