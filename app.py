import streamlit as st
import hashlib, json, os, time   # ← incluye time aquí


def get_hash(text: str, algo: str = "sha256") -> str:
    """Genera un hash único para el texto dado."""
    return hashlib.new(algo, text.encode("utf-8")).hexdigest()
# Combinar los datos del acta en un solo texto
fecha = time.strftime("%Y-%m-%d %H:%M:%S")

datos = {
    "titulo": titulo,
    "autor": autor,
    "contenido": contenido,
    "fecha": fecha
}

# Convertir el acta a JSON ordenado (para que el hash sea estable)
texto_canonico = json.dumps(datos, ensure_ascii=False, sort_keys=True)

# Generar el hash único
hash_acta = get_hash(texto_canonico)

# Crear el registro completo
acta = {
    **datos,
    "hash": hash_acta
}
with open("actas.json", "a") as f:
    json.dump(acta, f)
    f.write("\n")

st.success("✅ Acta registrada correctamente")
st.code(f"Hash generado: {hash_acta}")


st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
