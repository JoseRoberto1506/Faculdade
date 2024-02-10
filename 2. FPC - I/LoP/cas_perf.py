def main():
    string = [i for i in input() if i in ['(', ')', '[', ']', '{', '}']]
    casamento_perfeito(string)


def casamento_perfeito(s):
    pilha = []
    casamentos = {')': '(', ']': '[', '}': '{'}

    if len(s) % 2 != 0:
        return print("casamento imperfeito")
    
    for ch in s:
        if ch in casamentos:
            if pilha and pilha[-1] == casamentos[ch]:
                pilha.pop()
            else:
                return print("casamento imperfeito")
        else:
            pilha.append(ch)
    
    return print("casamento perfeito")


main()
