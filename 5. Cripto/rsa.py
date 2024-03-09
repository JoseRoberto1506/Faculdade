from random import randint


def main():
    mensagem = "criptografia"
    mensagem_codificada = codificar_mensagem(mensagem)  # Mensagem condificada em ASCII
    p, q = 17, 23   # Números primos (chaves privadas)
    n = p * q   # 1ª Chave pública
    totiente = (p - 1) * (q - 1)    # Função totiente de n
    e = definir_segunda_chave_publica(totiente) # 2ª Chave pública
    d = inverso_modular(e, totiente)    # Chave privada
    mensagem_cifrada = cifrar_mensagem(mensagem_codificada, e, n)
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, d, n)
    mensagem_descodificada = descodificar_mensagem(mensagem_decifrada)
    imprimir_dados(
        mensagem, mensagem_codificada, p, q, n, totiente, e, d,
        mensagem_cifrada, mensagem_decifrada, mensagem_descodificada,
    )


def codificar_mensagem(mensagem):
    mensagem_codificada = []
    for letra in mensagem:
        mensagem_codificada.append(ord(letra))

    return mensagem_codificada


def definir_segunda_chave_publica(totiente):
    while True:
        chave = randint(2, totiente - 1)
        if mdc(chave, totiente) == 1:
            return chave


def mdc(a, b):
    if a < b:
        a, b = b, a
    # Caso base
    if b == 0:
        return a
    # Cálculo recursivo
    else:
        return mdc(b, a % b)


def mdc_estendido(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = mdc_estendido(b, a % b)
        return [y, x - (a // b) * y, d]


def inverso_modular(e, totiente):
    if mdc(e, totiente) != 1:
        return 'Inverso modular não existe'
    else:
        x, y, d = mdc_estendido(e, totiente)
        return x % totiente


def cifrar_mensagem(m, e, n):
    mensagem_cifrada = []
    for valor_ascii in m:
        mensagem_cifrada.append(valor_ascii**e % n)

    return mensagem_cifrada


def decifrar_mensagem(m, d, n):
    mensagem_decifrada = []
    for valor_ascii in m:
        mensagem_decifrada.append(valor_ascii**d % n)

    return mensagem_decifrada


def descodificar_mensagem(mensagem_decifrada):
    mensagem = ""
    for valor_ascii in mensagem_decifrada:
        mensagem += chr(valor_ascii)

    return mensagem


def imprimir_dados(
        mensagem, mensagem_codificada, p, q, n, totiente, e, d,
        mensagem_cifrada, mensagem_decifrada, mensagem_descodificada
):
    print(f"Mensagem: {mensagem}")
    print(f"Mensagem codificada em ASCII: {mensagem_codificada}")
    print(f"Chaves Privadas: (p) = {p}; (q) = {q}; (d) = {d}")
    print(f"Chaves Públicas: (n) = {n}; (e) = {e}")
    print(f"Função totiente de n: {totiente}")
    print(f"Mensagem cifrada: {mensagem_cifrada}")
    print(f"Mensagem decifrada: {mensagem_decifrada}")
    print(f"Mensagem descodificada: {mensagem_descodificada}")


main()
