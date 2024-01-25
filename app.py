import streamlit as st
from atalhos import lista_atalhos, menu_atalhos

tipo_atalho = "r"
frase = None
frases = None
atalho = None

def rodada():
    global frase
    global atalho
    global tipo_atalho
    tipo_atalho = "r"
    col1, col2 = st.columns(2)
    with col1:
        frase = st.text_input("Insira a palavra da rodada")
    with col2:
        atalho = st.selectbox("Escolha o atalho", lista_atalhos, index=0)

def lista():
    global frases
    global atalho
    global tipo_atalho
    tipo_atalho = "l"
    col1, col2 = st.columns(2)
    atalho = st.selectbox("Escolha o atalho", lista_atalhos, index=0)
    frases = st.text_area("Insira as palavras da rodada", height=250)

def main():
    st.title("Atalhos")
    st.text("by Louis")

    if st.radio("Atalho", ["Rodada", "Lista"]) == "Rodada":
        rodada()
    else:
        lista()

    if st.button("Atalhar"):
        if tipo_atalho == "r":
            st.text_area("Saída", value = menu_atalhos[atalho](frase), height=200)
        elif tipo_atalho == "l":
            st.text_area("Saída", value = "\n".join([menu_atalhos[atalho](frase) for frase in frases.split("\n") if frase != ""]))


if __name__ == '__main__':
    main()