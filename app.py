
import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["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"])

st.set_page_config(page_title="É Fake ou é Fato?", page_icon="🕵️")

st.title("🕵️ É Fake ou é Fato?")
st.markdown("### ⚠️ Antes de compartilhar, verifique aqui!")

st.markdown("---")

opcao = st.radio("Escolha o tipo de verificação:", ["Texto ou Link", "Imagem/Print"])

texto = ""
imagem = None

if opcao == "Texto ou Link":
    texto = st.text_area("Cole aqui o texto ou link:")
else:
    imagem = st.file_uploader("Envie um print ou imagem", type=["jpg", "jpeg", "png", "webp"])

if st.button("🔍 Verificar agora"):
    if not texto and not imagem:
        st.warning("Por favor, insira um texto/link ou envie uma imagem.")
    else:
        conteudo = texto if texto else "Imagem enviada pelo usuário."

        prompt = f"""
Você é um verificador de fake news para pessoas leigas.

Responda exatamente neste formato:

🔴 FAKE NEWS
ou
🟢 NOTÍCIA VERDADEIRA
ou
🟡 NÃO DÁ PARA CONFIRMAR

Depois explique de forma simples:
- Por que chegou nessa conclusão
- O que a pessoa deve observar
- Cite fontes confiáveis se possível
- Seja gentil e didático

Conteúdo:
{conteudo}
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            tools=[{"type": "web_search_preview"}],
            input=prompt
        )

        st.markdown("## Resultado")
        st.write(response.output_text)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 11px; margin-top: 40px;'>"
    "Criado por: Thiérry Picasky Bueri"
    "</div>",
    unsafe_allow_html=True
)
