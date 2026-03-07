# ejemplos de tipos de operadores

# operadores aritmeticos
print('suma +')
numero1 = 3
numero2 = 2
resultado_suma = numero1 + numero2
print(resultado_suma)

print('\nresta -')
resultado_resta = numero1 - numero2
print(resultado_resta)

print('\nmultiplicacion *')
resultado_multiplicacion= numero1 * numero2
print(resultado_multiplicacion)

print('\ndivision /')
resultado_division = numero1 / numero2
print(resultado_division)

print('\ndivision de enteros //')
resultado_division_enteros = numero1 // numero2
print(resultado_division_enteros)

print('\nresto de la division %')
resultado_resto_division = numero1 % numero2
print(resultado_resto_division)

print('\npotenciacion **')
resultado_potenciacion = numero1 ** numero2
print(resultado_potenciacion)

# operadores de comparacion
print('\nigual (==)')
es_igual = numero1 == numero2
print(es_igual)

print('\nes diferente (!=)')
es_diferente = numero1 != numero2
print(es_diferente)

print('\nes mayor que (>)')
es_mayor_que = numero1 > numero2
print(es_mayor_que)

print('\nes mayor o ugual que (>=)')
es_mayor_igual = numero1 >= numero2
print(es_mayor_igual)

print('\nes menor que (<)')
es_menor_que = numero1 < numero2
print(es_menor_que)

print('\nes menor o ugual que (<=)')
es_menor_igual = numero1 <= numero2
print(es_menor_igual)

# operadores logicos
print('\noperador and')
if numero1 > numero2 and numero2 > 1: # (and) retorna verdadero si ambas condiciones son verdaderas
    print('verdadero')

print('\noperador or')
if numero1 > numero2 or numero2 > 1: # (or) retorna verdadero si al menos 1 condicion es verdadera
    print('verdadero')

print('\noperador not')
result = True
print(not result) # (not) retorna lo contrario si el resultado es true de vuelve false y si es false de vuelve true

# operadores de asignacion
valor = 10
print(f'\nvalor = {valor}')
print('(+=) suma 1 al la variable asignada')
valor += 1
print(f'valor = {valor}')

print('\n(-=) resta 1 al la variable asignada')
valor -= 1
print(f'valor = {valor}')

print('\n(*=) multiplica 2 al la variable asignada')
valor *=2
print(f'valor = {valor}')

print('\n(/=) divide 2 al la variable asignada')
valor /= 2
print(f'valor = {valor}')

print('\n(**=) potenciacion 4 al la variable asignada')
valor **= 4
print(f'valor = {valor}')

print('\n(//=) division de enteros 3 al la variable asignada')
valor //= 3
print(f'valor = {valor}')

print('\n(%=) resto de la division 3 al la variable asignada')
valor %= 3
print(f'valor = {valor}')

# operadores de identidad y pertenencia
numeros = {1,2,3,4,5,6,7}
num1 = 4
num2 = 5

print('\noperador de identidad (is)')
print(f'{num1} es igual que {num2} = {num1 is num2}')

print('\noperador de identidad (is not)')
print(f'{num1} es igual que {num2} = {num1 is not num2}')

print('\noperador de pertenencia (in)')
print(f'{num1} esta dentro de numeros = {num1 in numeros}')

print('\noperador de pertenencia (not in)')
print(f'{num1} esta dentro de numeros = {num1 not in numeros}')

# operadores de bit
print('\noperado (&) AND da 1 si ambos bit son 1')
a = 15
b = 4
print(f'a:{a} b:{b} = {a & b}')

print('\noperado (|) OR da 1 si almenos un bit es 1')
print(f'a:{a} b:{b} = {a | b}')

print('\noperado (^) XOR da 1 si EXACTAMENTE uno de los bit es 1')
print(f'a:{a} b:{b} = {a ^ b}')

print('\noperado (~) NOT invierte todos los bit completamente a dos')
print(f'a:{a} b:{b} = {~a}')

print('\noperado (<<) Left Shift desplaza bit a la izquierda añade ceros')
print(f'a:{a} b:{b} = {a << 2}')

print('\noperado (>>) Right Shift  desplaza bit a la izquierda añade ceros')
print(f'a:{a} b:{b} = {a >> 2}')
