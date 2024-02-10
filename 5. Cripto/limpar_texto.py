from string import ascii_letters


def main():
    plaintext = limpar_texto("sistemas de informação")
    print(plaintext)


def limpar_texto(texto):
    texto_limpo = ""

    for c in texto.lower():
        if c == "ç":
            texto_limpo += "c"
        elif c in ["ã", "â", "á", "à"]:
            texto_limpo += "a"
        elif c in ["ê", "é", "è"]:
            texto_limpo += "e"
        elif c in ["î", "í", "ì"]:
            texto_limpo += "i"
        elif c in ["õ", "ô", "ó", "ò"]:
            texto_limpo += "o"
        elif c in ["û", "ú", "ù"]:
            texto_limpo += "u"
        elif c in ascii_letters:
            texto_limpo += c

    return texto_limpo


if __name__ == "__main__":
    main()
