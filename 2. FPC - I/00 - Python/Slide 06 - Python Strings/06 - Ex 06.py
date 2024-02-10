palavra = "BRASIL"
palavra_palpite = ["_", "_", "_", "_", "_", "_"]
acertos = erros = 0

while erros <= 6:
    palpite = str(input("Digite uma letra: ")).strip().upper()

    if palpite not in palavra:
        erros += 1
        if erros <= 6:
            print(f"-> Você errou pela {erros}ª vez. Tente de novo!")
        else:
            print("Fim de jogo, você errou 7 vezes.")
    else:
        print(f"A palavra é: ",end='')
        i = 0
        for letra in palavra:
            if palpite == letra:
                palavra_palpite[i] = palpite
            i += 1
        print(palavra_palpite)
        
    if "_" not in palavra_palpite:
        break
