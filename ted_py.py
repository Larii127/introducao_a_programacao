numeros = []
for i in range(20):
    numero = int(input(f'Digite o {i+1} número:'))
    numeros.append(numero)

numeros_invertidos = list(reversed(numeros))
print(numeros_invertidos)
