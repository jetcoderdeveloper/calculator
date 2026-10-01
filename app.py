from flask import Flask, render_template, request, jsonify
from convertisseur import convertir

app = Flask(__name__)


@app.route('/')
def accueil():
    return render_template('index.html')


@app.route('/convertir', methods=['POST'])
def route_convertir():
    data = request.get_json()

    nombre = data.get('nombre', '')
    base_depart = data.get('base_depart', '')
    base_arrivee = data.get('base_arrivee', '')

    resultat = convertir(nombre, base_depart, base_arrivee)

    # convertir() renvoie déjà {"resultat": ...} ou {"erreur": ...}
    return jsonify(resultat)


if __name__ == '__main__':
    app.run(debug=True)
