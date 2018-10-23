"""
def suma(x,y):
    return x + y

lista_ejemplo = ["hilera", 2344, 2344.29, None, False, suma]

for elemento in lista_ejemplo: print(elemento)

print(len(lista_ejemplo))
print(lista_ejemplo[-1])
print(lista_ejemplo[None])
resultado = lista_ejemplo[5](50,80)
print(resultado)
"""

def print_matrix_impura(matrix):
    for fila in matrix:
        print(fila)

def generar_matrix(filas, columnas):
    lista_lista = []
    for numero in range(0, filas):
        lista_lista.append([])
        for num in range(0, columnas):
            lista_lista[num].append(0)
    return lista_lista


lista_lista = []


        lista_lista[numero].append(num)


print_matrix_impura(lista_lista)

