curso = " Curso de Python "

print(f"Original: {curso} Tamanho da palavra: {len(curso)} caracteres")

# print(curso.lower().strip())
# print(curso.upper().strip())
# print(curso.replace("Python", "C#").strip())
# print(curso.replace("P", "A"))

z = curso.strip()
x = z.split(" ")
print(x[0], x[1], x[2])