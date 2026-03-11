""" cadenas de caracteres : strings """

# creacion
cadena = 'esto es un a cadena de caracteres puede tener comillas simples o comillas dobles'

# unir cadenas 
saludar = ('hola,')
nombre = (' andres')
print(saludar + nombre) # une dos o mas cadenas

# repetir cadenas 
print(saludar * 3) # repite la cadena por las veces indicadas

# formateo de cadenas o f-string
apellido = ('bravo')
print(f'{saludar} soy{nombre} {apellido}')

# acceder al caracteres segun el indice

texto = ('hola mundo')
print(texto)

primer_caracter = texto[0] # salida h
print(primer_caracter)

ultimo_caracter = texto[-1] # salida o
print(ultimo_caracter)

desde_hasta = texto[0:4] # salida hola
print(desde_hasta)

# verificaciones 
esta_dentro = 'ho' in texto # pregunta si 'ho' esta dentro de la cadena texto si esta devuelve true si no false
print(esta_dentro)

enpieza_con = texto.startswith('h') # pregunta si la cadena enpiesa por 'h' si esta devuelve true si no false
print(enpieza_con)

es_numero = texto.isdigit() # Verifica si el texto contiene solo números
print(es_numero)

invertir_cadena = texto[::-1] # invirte la cadena 
print(invertir_cadena)