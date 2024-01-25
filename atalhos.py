def espelho(frase):
    return frase[::-1]

def pontilhado(frase):
    return "".join([f"{x}." if not x.isspace() else x for x in frase])

def compor(frase):
    return "\n".join([frase[:x+1] for x in range(len(frase)) if not frase[x].isspace()])

def decompor(frase):
    return "\n".join(compor(frase).split("\n")[::-1])

def piramide(frase):
    return compor(frase) + decompor(frase)[len(frase):]

def piramide_inversa(frase):
    return piramide(espelho(frase))

def ponto_virgula(frase):
    return " ".join([f".{x}," for x in frase if not x.isspace()])

def recompor(frase):
    return decompor(frase) + compor(frase)[1:]

def rebobinando(frase):
    frase = recompor(frase).split("\n")
    frase = [x[::-1] if frase.index(x) % 2 else x for x in frase]
    return "```\n" + "\n".join(frase) + "\n```"

menu_atalhos = {
        "Espelho": espelho,
        "Pontilhado": pontilhado,
        "Compor": compor,
        "Decompor": decompor,
        "Piramide": piramide,
        "Piramide Inversa": piramide_inversa,
        "Ponto e Virgula": ponto_virgula,
        "Recompor": recompor,
        "Rebobinando": rebobinando,
        }

lista_atalhos = [atalho for atalho in menu_atalhos]

if __name__ == "__main__":
    for atalho in lista_atalhos:
        print(lista_atalhos[atalho]("Luis Fernando Santos Cardeal"), end="\n\n")
