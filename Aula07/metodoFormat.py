cidade = "São Paulo"
dia = 15
mes = "Outubro"
ano = 2024
canal = "CFB Cursos"
data = "{}, {} de {} de {} \n\"{}\"" # caracteres de scape, \n quebra de linha e \"\" imprimir aspas

print(data.format(cidade, dia, mes, ano, canal))