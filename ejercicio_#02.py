# funciones en python

####### estructura basica #########

# esta funcion resive un parametro (nombre)
def saludar(nombre):
    return f'hola {nombre}'

# guardar el resultado de la funcion   
mensaje = saludar('andres')

# ejecutar la funcion
print(mensaje)

######################################
# argumentos predefinidos

def suma(a, b=3):
    return f'{a} + {b} = {a + b}'

resultado = suma(3)
print(resultado)

#################################
# funciones lambdas o funciones anonimas

restar = lambda a, b: a - b
print(restar(6, 5)) 

###################################
# manejo de argumentos variables
# *args: Recibe múltiples argumentos como una tupla.
# **kwargs: Recibe múltiples argumentos con nombre como un diccionario.

def pedido(tamaño, *ingredientes, **detalles):
    print(f'pizza tamaño {tamaño} con ingredientes {ingredientes}')
    print(f'detalles {detalles}')

pedido("Grande", "Peperoni", "Queso", direccion="Calle 123", nota="Sin cebolla")

def sumar(b, *numero):
    """esta funcion rescive primero un parametro (b) y lo suma con los siguientes argumentos multiples(*numero) estos los resive la funcion en forma de tupla y los recore uno a uno utilizando un ciclo for"""
    for numer in numero:
        print(f'{b} + {numer} = {b + numer}')
sumar(1,1,2,3,4,5,6,7,8,9,10)

###################################

# alcance local y clobal
variable_global = 'El alcance global: funciona desde cualquier parte del codigo.'
def alcance():
    """Function documentation"""
    variable_local = 'El alcance local: solo funciona dentro de la funcion.'
    print(variable_local)
    print(variable_global)
alcance()
# print(variable_local) # la variable local fuera de la funcion no se encuentra definida

#################################