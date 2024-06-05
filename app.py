import streamlit as st

# Estilo personalizado
st.markdown("""
    <style>
    body {
        background-color: #282828;
        color: white;
        font-family: 'Press Start 2P', cursive;
    }
    .stApp {
        background-color: #282828;
    }
    .title {
        text-align: center;
        font-size: 72px;
        color: white;
    }
    .subtitle {
        text-align: center;
        font-size: 48px;
        color: white;
    }
    .update-button {
        display: block;
        margin: auto;
        font-size: 24px;
        font-family: 'Press Start 2P', cursive;
        border: 2px solid white;
        background-color: transparent;
        color: white;
        padding: 10px 20px;
        cursor: pointer;
    }
    .update-button:hover {
        background-color: white;
        color: #282828;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.markdown("<h1 class='title'>KIRAMETER</h1>", unsafe_allow_html=True)

# Subtítulo en el centro de la pantalla
st.markdown("<h2 class='subtitle'>LASS MAL REDEN</h2>", unsafe_allow_html=True)

# Botón de actualización
if st.button('UPDATE'):
    st.write('Has hecho clic en actualizar.')

st.markdown("""
    <style>
    div.stButton > button {
        display: block;
        margin: auto;
        font-size: 24px;
        font-family: 'Press Start 2P', cursive;
        border: 2px solid white;
        background-color: #444;
        color: white;
    }
    div.stButton > button:hover {
        background-color: white;
        color: #282828;
    }
    </style>
    """, unsafe_allow_html=True)