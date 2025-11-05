import streamlit as st
import hashlib, json, os
from datetime import datetime

def get_hash(text: str, algo: str = "sha256") -> str:
    return hashlib.new(algo, text.encode("utf-8")).hexdigest()

st.title("🧾 Acta Digital")
titulo = st.text_input("Título")
autor = st.text_input("Autor")
contenido = st.text_area("Contenido")

if st.button("📄 Guardar acta"):
    if titulo and autor and contenido:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos = {"titulo": titulo, "autor": autor, "contenido": contenido, "fecha": fecha}
        texto_canonico = json.dumps(datos, ensure_ascii=False, sort_keys=True)
        hash_acta = get_hash(texto_canonico)

        acta = {**datos, "hash": hash_acta}
        with open("actas.json", "a") as f:
            json.dump(acta, f)
            f.write("\n")

        st.success("✅ Acta registrada")
        st.code(f"Hash: {hash_acta}")
    else:
        st.warning("Completa todos los campos.")



st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
