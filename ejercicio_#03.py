""" estructuras de datos """

# listas: list
print('\n######### LIST ##########')
frutas = ['manzana', 'pera', 'papaya'] # sintaxis

# metodos list
frutas.append('mango') # append() : agrega un elemento al final de la lista

frutas.insert(1, 'naranja') # inserta un elemento en el indice indicado

frutas.remove('pera') # remove() : busca y elimina el elemento indicado en la lista

frutas.sort() # short() : ordena de manera ascendente la lista 

frutas.pop() # elimina el ultimo elemento

# imprimir
print(frutas)

# tuplas : tuple
print('\n######### TUPLE ##########')

colores = ('amarillo', 'azul', 'rojo') # sintaxis

# imprimir
print(colores)

# metodos de tuplas

print(colores.count('amarillo')) # count() : cuenta cuantas veces aparece un elemento dentro de la tupla

print(colores.index('azul')) # index() : busca un elemento y devuelve el indice si no existe muestra un error

# diccionarios : dict
print('\n######### DICT ##########')

""" son colecciones clave valor son mutables y no permiten claves duplicadas"""
usuario = {
    'nombre': 'andres',
    'apellido': 'bravo',
    'edad': 25
    } # sintaxis

# metodos de dict
print(usuario.get('nombre')) # get() : busca la clave y devuelve su valor

print(usuario.keys()) # keys() : devuelve todas las claves del diccionario

print(usuario.values()) # values() : devuelve todos los valores de el diccionario

print(usuario.items()) #  items() : devuelve pares de clave valor de todo el dict

print(usuario.update({'ubicacion': 'cienaga magdalena'})) # update() : agrega un nuevo elemento a dict

print(usuario.update({'ubicacion': 'cienaga'})) # update() : puedes modificar elementos ya creados en el dict

print(usuario)

# conjuntos : set
print('\n######### SET ##########')

""" son conjunto de elementos no ordenados de elementos unicos"""
numeros = {1,2,3,4,5,5}
print(numeros)

numeros.add(6) # Añade un elemento (si ya existe, no hace nada)
print(numeros)

numeros_2 = {6,7,8,9,10}
print(numeros_2)

unir_set = numeros.union(numeros_2) # Combina dos conjuntos sin duplicados
print(unir_set)

elementos_ambos = numeros.intersection(numeros_2) # Devuelve solo los elementos que están en ambos
print(elementos_ambos)

diferencia = numeros.difference(numeros_2) # Devuelve los elementos que están en el primero pero no en el segundo
print(diferencia)

#  cadenas de texto : str
print('\n######### STR ##########')

nombre = (' andres, bravo ')
print(nombre)

# metodos str
print(nombre.upper()) # comvierte la cadena a mayusculas
print(nombre.lower()) # comvierte la cadena a minusculas
print(nombre.replace('andres', 'felipe')) # remplaza un valor antiguo por uno nuevo
print(nombre.strip()) # elimina espacios vacios al inicio y al  final
print(nombre.split(',')) # rompe un testo y lo comvierte en una lista dependiendo del separador