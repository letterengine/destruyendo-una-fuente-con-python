'''Destruyendo una fuente con Python'''

# Módulos necesarios
import os
import re
import random


def destruirFuente():
    '''Esta función destruye la fuente'''
    # Primero definimos las rutas que necesitaremos para destruir la fuente
    raiz = os.path.split(__file__)[0]
    ufo = os.path.join(raiz, 'RobotoMono-Regular.ufo')
    # Vamos a revisar los archivos y carpetas que tiene
    print(os.listdir(ufo))
    # Vamos a guardar la carpeta de glifos en una variable
    glifosDir = os.path.join(ufo, 'glyphs')
    # Y ahora vamos a guardar los glifos en otra variable
    glifos = [os.path.join(glifosDir, glifo)
              for glifo in os.listdir(glifosDir) if '.glif' in glifo]
    # Vamos a hacer una iteración por cada glifo
    for glifo in glifos:
        glifoDestruido = []
        # Vamos a abrir cada glifo como un archivo de texto en modo de escritura
        with open(glifo, 'r', encoding='utf-8') as glifoFile:
            # Llamamos una función que nos permita leer el contenido
            lector = glifoFile.readlines()
            # Y comenzamos a iterar línea por línea buscando con regex el patrón de los nodos
            regex = 'x="\\d+" y="\\d+"'
            for linea in lector:
                # Hacemos una pequeña condicional para cambiar las coordenadas
                if re.search(regex, linea):
                    # Invertamos la selección
                    randomx = random.randint(0, 1000)
                    randomy = random.randint(0, 1000)
                    glifoDestruido.append(
                        re.sub(regex, f'x="{randomx}" y="{randomy}"', linea)
                    )
                # Es importante que la nueva fuente tenga todas las líneas
                # si no dejará de funcionar
                else:
                    glifoDestruido.append(linea)
        # Vamos a abrir cada glifo como un archivo de texto en modo de escritura
        with open(glifo, 'w', encoding='utf-8') as glifoFile:
            # Escribimos las lineas modificadas en el archivo
            glifoFile.writelines(glifoDestruido)


if __name__ == '__main__':
    destruirFuente()
