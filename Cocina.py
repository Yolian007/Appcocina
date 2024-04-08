import streamlit as st
import time

# Título y autor
st.title("Temporizador")
st.write("Esta app fue elaborada por Linder Rodriguez.")

# Selector de alimento
alimento = st.selectbox("Selecciona un alimento:", ["Carne", "Pollo", "Otro"])

# Selector de tiempo
tiempo_deseado = st.number_input("Ingresa el tiempo deseado en segundos:", min_value=1, step=1)

# Duración del temporizador según el alimento seleccionado (si lo hubiera)
if alimento == "Carne":
    tiempo_deseado = 15
elif alimento == "Pollo":
    tiempo_deseado = 20
elif alimento == "Otro":
    tiempo_deseado = 10

# Mostrar temporizador
temporizador = st.empty()
for i in range(tiempo_deseado, 0, -1):
    temporizador.write(f"Tiempo restante: {i} segundos")
    time.sleep(1)
temporizador.write("¡Listo!")
