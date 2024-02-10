from string import ascii_letters
from random import randint
from limpar_texto import limpar_texto


def main():
    plain_text = 'strike now'
    mensagem_falsa = 'hold off until you hear from me again. we may compromise.'
    texto_cifrado = encrypt(plain_text.upper(), mensagem_falsa)
    mensagem_decifrada = decrypt(texto_cifrado)

    print(f'Mensagem a ser cifrada:\n{plain_text}\n')
    print(f'Mensagem falsa:\n{mensagem_falsa}\n')
    print(f'Texto cifrado:\n{texto_cifrado}\n')
    print(f'Mensagem decifrada:\n{mensagem_decifrada}')


def encrypt(texto, mensagem_falsa):
    # Mapa do código binário de cada letra do alfabeto
    letra_para_codigo = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
                        'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
                        'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
                        'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
                        'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
                        'Z': 'bbaab'}
    texto_em_binario = ''

    # Converter cada letra do texto a ser cifrado no código binário (A/B)
    for c in texto:
        if c != ' ':
            texto_em_binario += letra_para_codigo[c]

    # Garantir que o código binário e a mensagem falsa são do mesmo tamanho (desconsiderando espaços)
    mensagem_falsa_limpa = limpar_texto(mensagem_falsa)
    total_letras_restantes = len(texto_em_binario) - len(mensagem_falsa_limpa)
    if total_letras_restantes < 0:
        mensagem_falsa_limpa = mensagem_falsa_limpa[:len(texto_em_binario)]
    elif total_letras_restantes > 0:
        for i in range(total_letras_restantes):
            mensagem_falsa_limpa += ascii_letters[randint(0, len(ascii_letters))]

    # Converter cada letra da mensagem falsa em maiúscula/minúscula de acordo com o código binario
    mensagem_falsa_cifrada = []
    for i in range(len(texto_em_binario)):
        if texto_em_binario[i] == 'a':
            mensagem_falsa_cifrada.append(mensagem_falsa_limpa[i].lower())
        elif texto_em_binario[i] == 'b':
            mensagem_falsa_cifrada.append(mensagem_falsa_limpa[i].upper())

    # Adicionar espaços e pontuações de volta na mensagem
    for i in range(len(mensagem_falsa)):
        if not mensagem_falsa[i].isalpha():
            mensagem_falsa_cifrada.insert(i, mensagem_falsa[i])

    return ''.join(mensagem_falsa_cifrada)


def decrypt(texto_cifrado):
    # Mapa da letra correspondente de cada código binário
    codigo_para_letra = {'aaaaa': 'A', 'aaaab': 'B', 'aaaba': 'C', 'aaabb': 'D', 'aabaa': 'E',
                        'aabab': 'F', 'aabba': 'G', 'aabbb': 'H', 'abaaa': 'I', 'abaab': 'J',
                        'ababa': 'K', 'ababb': 'L', 'abbaa': 'M', 'abbab': 'N', 'abbba': 'O',
                        'abbbb': 'P', 'baaaa': 'Q', 'baaab': 'R', 'baaba': 'S', 'baabb': 'T',
                        'babaa': 'U', 'babab': 'V', 'babba': 'W', 'babbb': 'X', 'bbaaa': 'Y',
                        'bbaab': 'Z'}

    # Converter o texto cifrado em código binario (A/B)
    texto_binario = ''
    for c in texto_cifrado:
        if c.isalpha() and c.islower():
            texto_binario += 'a'
        elif c.isalpha() and c.isupper():
            texto_binario += 'b'

    # Converter cada bloco de tamanho 5 na letra correspondente do alfabeto para decifrar o texto
    texto_decifrado = ''
    for i in range(0, len(texto_binario) - 4, 5):
        codigo_binario = texto_binario[i:i+5]
        texto_decifrado += codigo_para_letra[codigo_binario]

    return texto_decifrado


main()
