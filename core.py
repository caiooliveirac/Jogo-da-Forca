#Modelo de criação de diferentes arquivos txt com dificuldades diferentes baseados numa lista

arquivo = open('palavras2.txt',mode='r',encoding='utf8')
arquivo2 = open('palavras3.txt',mode='r',encoding='utf8')
todas = []
nivel = []

for linha in arquivo:
    linha.strip()
    todas.append(linha)
for palavra in arquivo2:
    palavra.strip()
    nivel.append(palavra)

with open('palavras2.txt','w',encoding='utf8') as arq:
    for i, k in enumerate(todas):
        if i > 0 and k not in nivel:
            arq.write(f"{k}")
print(todas)
print(nivel)

