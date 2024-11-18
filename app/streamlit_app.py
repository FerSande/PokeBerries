import streamlit as st
import requests
import streamlit.components.v1 as components

st.title("Poke Berries Statistics")
st.write("Interface to interact with Poke Berries API endpoints")

BASE_URL = "http://localhost:8000"

response = requests.get(f"{BASE_URL}/")
if response.status_code == 200:
    st.success(response.json()["message"])
else:
    st.error(f"Error: {response.status_code} - {response.text}")

st.header("Poke Berries Statistics")
if st.button("Cargar Estadísticas"):
    response = requests.get(f"{BASE_URL}/allBerryStats")
    if response.status_code == 200:
        stats = response.json()
        st.write("### Statistics obtained:")
        st.write(stats)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")

st.header("Berries Distribution Chart")
if st.button("Load Berries Histogram"):
    response = requests.get(f"{BASE_URL}/berryHistogram")
    if response.status_code == 200:
        html_content = response.text
        components.html(html_content, height=700)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
