from random import randint

def forca():
    print("="*53)
    print("="*19,"JOGO DA FORCA","="*19)
    print("="*53)
    dificuldade = int(input("Deseja jogar no [1] Fácil [2] Médio [3] Difícil: "))
    print("=" * 53)
    while True:
        if dificuldade == 1:
            arquivo = open("palavras.txt", "r")
            break
        elif dificuldade == 2:
            arquivo = open("palavras.txt", "r")
            break
        elif dificuldade == 3:
            arquivo = open("palavras.txt", "r")
            break
        else:
            print("Não entendi. Digite 1, 2 ou 3.")
    palavras = []
    for linha in arquivo:
        palavras.append(linha)
    palavra_secreta = palavras[randint(0,len(palavras))]

    acertou = False
    errou = False
    erros = 0
    erradas = ""
    palavra = [x for x in palavra_secreta]
    escondida = ["_" for x in palavra_secreta]
    for x in escondida:
        print(x,end=" ")
    while (not acertou and not errou):
        chute = input("\nQual letra quer verificar? ").lower()
        index = 0
        if len(chute) != 1:
            print("Você deve digitar uma e apenas uma letra.")
            continue
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {chute} na posição {index}.")
                escondida[index] = chute
            index += 1
        if palavra_secreta.find(chute) == -1:
            print("Não. Essa letra eu não encontrei.")
            erros += 1
            erradas += chute + " "
            print("\nSeus erros até agora: ",erradas.upper(),end=" ")
            print()
            if erros >= 12:
                print("GAME OVER. VOCÊ NÃO CONSEGUIU!")
                print(f'A fruta era {palavra_secreta}')
                break
        novo_result = ""
        for i in escondida:
            novo_result += i
            novo_result += " "
        print(f"Até agora temos: {novo_result}")
        if escondida == palavra:
            print("\nMUITO BEM! VOCÊ CONSEGUIU!!!")
            break

if __name__ == "__main__":
    forca()