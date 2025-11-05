memes_modernos = {
    "GOAT": "Melhor de todos os tempos",
    "FLEX": "Se exibir ou ostentar",
    "SHIPPAR": "Torcer para que duas pessoas fiquem juntas",
    "LACRAR": "Arrasar, se destacar muito em algo",
    "TROLLAR": "Brincar ou zombar de alguém",
    "HYPE": "Grande expectativa ou animação"
}

print("Dicionário Moderno")
print("Escreva uma palavra MAIÚSCULA.")

for i in range(5):
    print("Palavra:")
    palavra = input()
    if palavra in memes_modernos:
        print(memes_modernos[palavra])
    else:
        print("Palavra não encontrada.")
        print("Deseja adicionar? (s/n)")
        resposta = input()
        if resposta == "s" or resposta == "S":
            print("Digite o significado:")
            significado = input()
            memes_modernos[palavra] = significado
            print("Adicionado.")
print("Fim.")
