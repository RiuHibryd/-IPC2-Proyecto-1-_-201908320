import xml.etree.cElementTree as ET
from xml.dom import minidom
import os
print("Ingrese la Ruta del XML")
filename = input()
if not os.path.isfile(filename):
    print("No se encontro, verifique que este bien escrito")
    exit()
tree = ET.parse(filename)
root = tree.getroot()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DatosMartes:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

datos_martes = DatosMartes()

print("----Generando Lista Bacterias----")
for organismos in root.find("listaOrganismos").findall("organismo"):
    codex = organismos.find("codigo").text
    nombre = organismos.find("nombre").text

    datos_martes.insert({"Codigo:": codex, "Nombre Organismo": nombre}) 

print("--Lista Organismos--")
datos_martes.print_list()

print("---Generando Lista Celdas Vivas---")
Bacterias_vivas_cargadas = DatosMartes()
for muestras in root.find("listadoMuestras").findall("muestra"):
    codigo = muestras.find("codigo").text
    descripcion = muestras.find("descripcion").text
    filas = muestras.find("filas").text
    columnas = muestras.find("columnas").text

    celdas_vivas = DatosMartes()
    #Lista Entre Lista, mi vida se consume en listas :D
    for celda in muestras.find("listadoCeldasVivas").findall("celdaViva"):
        fila = celda.find("fila").text
        columna = celda.find("columna").text
        codigo = celda.find("codigoOrganismo").text
        
        celdas_vivas.insert({"Fila": fila, "Columna": columna, "Codigo": codigo, "Estado": "viva"})
    Bacterias_vivas_cargadas.insert({"Codigo": codigo, "Descripcion": descripcion, "Filas": filas, "Columnas": columnas, "Celdas_vivas": celdas_vivas})

print("Prueba A")
Bacterias_vivas_cargadas.print_list()
for celda_viva in Bacterias_vivas_cargadas:
    print(celda_viva["Codigo"], celda_viva["Descripcion"])
    celdas_vivas = celda_viva["Celdas_vivas"]
    for celda in celdas_vivas:
        print("\t", celda["Fila"], celda["Columna"], celda["Codigo"])
