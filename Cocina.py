import streamlit as st
import time

# Título y autor
st.title("Temporizador")
st.write("Esta app fue elaborada por Linder Rodriguez.")

# Selector de alimento
alimento = st.selectbox("Selecciona un alimento:", ["Carne", "Pollo", "Otro"])

# Duración del temporizador según el alimento seleccionado
if alimento == "Carne":
    duracion = 15
elif alimento == "Pollo":
    duracion = 20
else:
    duracion = 10

# Mostrar temporizador
temporizador = st.empty()
for i in range(duracion, 0, -1):
    temporizador.write(f"Tiempo restante: {i} segundos")
    time.sleep(1)
temporizador.write("¡Listo!")

