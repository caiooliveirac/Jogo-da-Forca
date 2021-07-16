encoding: 'utf-8'

arquivo = open('palavras.txt','r')
arquivo2 = open('palavras2.txt', 'r')
todas = []
nivel = []
for linha in arquivo2:
    linha = str(linha)
    todas.append(linha)
for palavra in arquivo:
    nivel.append(palavra)
print(todas)
print(nivel)

