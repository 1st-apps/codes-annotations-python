a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
op = input("Digite a operação: ")
res = 0

if op == "+":
    res = a + b
    print(f"O valor de {a} + {b} é {res}")
elif op == "-":
    res = a - b
    print(f"O valor de {a} - {b} é {res}")
elif op == "*":
    res = a * b
    print(f"O valor de {a} * {b} é {res}")
elif op == "/":
    res = a / b
    print(f"O valor de {a} / {b} é {float(res):.2f}")
else:
    print("Valor invalido")
