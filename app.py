import os
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_123456789'  # Necesario para session

@app.route("/", methods=["GET", "POST"])
def index():
    texto_original = ""
    texto_convertido = ""
    
    # Obtener idioma de la sesión o usar 'es' por defecto
    idioma = session.get('idioma', 'es')
    
    if request.method == "POST":
        texto_original = request.form.get("texto", "")
        texto_convertido = texto_original.upper()
    
    return render_template("index.html", 
                         texto_original=texto_original, 
                         texto_convertido=texto_convertido,
                         idioma=idioma)

@app.route("/cambiar-idioma", methods=["POST"])
def cambiar_idioma():
    """Cambiar el idioma de la página"""
    data = request.get_json()
    idioma = data.get("idioma", "es")
    session['idioma'] = idioma
    return jsonify({"success": True, "idioma": idioma})

@app.route("/convert-to-upper", methods=["POST"])
def convert_to_upper():
    """API endpoint para convertir a mayúsculas via JavaScript"""
    data = request.get_json()
    texto = data.get("texto", "")
    resultado = texto.upper()
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)