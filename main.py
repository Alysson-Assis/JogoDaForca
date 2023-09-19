from random import *


with open(file="words.txt", mode="r") as dados:
    list_palavras = [palavra.rstrip('\n') for palavra in dados]

palavra_random = choice(list_palavras)
print(palavra_random)

len_palavra = len(palavra_random)
vida = 6
display = ["_" for _ in range(len_palavra)]

num_taços = len(display)
jogoLigado = "_" in display

while jogoLigado:
    print(f"{' '.join(display)}")
    letra_escolhida = input("Adivinhe uma letra: ").lower()

    for posicao in range(len_palavra):
        letra = palavra_random[posicao]
        if letra == letra_escolhida:
            display[posicao] = letra
    if letra_escolhida not in palavra_random:
        vida -=1

    if vida == 0:
        jogoLigado = False
    print(f"\nVocê tem {vida} chances!")
