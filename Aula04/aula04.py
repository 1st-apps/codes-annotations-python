x = 1 #int
x = "CFB Cursos" #string
x = 1.56 #float
x = True #bool

n1 = 5
n2 = 2
x = complex(n1, n2)
print(x.real) #real
print(x.imag) #imaginarios

x = ["Carro", "Aviao", "Navio", 1, 48.3, True] #array(list)
# x[0] = "Onibus" #operando o array, mudando o valor

x = ("Carro", "Aviao", "Navio", 1, 48.3, True) #Tuplas - não consigo substituir um elemento igual operar o array

x = range(0,100,1) #método para definir um array (list) de forma fácil

x = {
    "Canal" : "CFB Cursos",
    "Curso" : "Curso de Python",
    "Professor" : "Bruno"
    
} #dictionary - usando chaves, elemento chave e valor

print(f"Valor: {x["Canal"] }") #imprimindo um dictonary - usando o valor da chave
print(f"Tipo de dado: {type(x)}")

X = {5,6,7,6,2,8,8,9,5} #SET - NAO REPETE VALORES
X = frozenset({5,6,7,6,2,8,8,9,5}) #SET - BLOQUEIA O SET, nao pode alterar

print(f"Valor: {str(X)}")
print(f"Tipo: {type(X)}")