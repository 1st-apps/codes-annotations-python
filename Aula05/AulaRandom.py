import random

num_r = random.randrange(0,59) #numeros inteiros
print(f"Numero Aleatorio Gerado: ({num_r}) Tipo do numero: {type(num_r)}")

# Gerar mais valores aleatórios
arr_num_r = [ #List / Array
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
]

print(f"Numeros aleatorios gerados {arr_num_r}")
print(f"Valor 1: {arr_num_r[0]}")
print(f"Valor 2: {arr_num_r[1]}")
print(f"Valor 3: {arr_num_r[2]}")
print(f"Valor 4: {arr_num_r[3]}")
print(f"Valor 5: {arr_num_r[4]}")