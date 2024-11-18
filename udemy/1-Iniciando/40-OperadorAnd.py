entrada = input('[E]ntrar ou [S]air:').upper()
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Entrou")
else:
    print("Sair")