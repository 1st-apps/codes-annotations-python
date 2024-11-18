nome = input('Digite o seu nome: ')
encontrar_palavra = input('Digite a palavra que deseja encontrar: ')

if encontrar_palavra in nome:
    print(f'VOCÊ ENCONTROU! {encontrar_palavra=} ESTÁ EM {nome=}')
else:
    print(f'{encontrar_palavra=} não está em {nome=}')

# print('pp' in nome) # true - pp está entre nome - pp está em nome
# print('pp' not in nome) # false - pp esta em nome - pp nao esta em nome
# print(10 * '-')
# print('aa' not in nome) # 'aa' nao esta em nome