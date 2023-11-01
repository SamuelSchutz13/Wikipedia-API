from flask import Flask, request, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/api/v1/search", methods=["POST", "GET"])
def search_wikipedia():
    search = request.args.get("search")
    lang = request.args.get("lang")

    if not search:
        return jsonify({"error": "O parâmetro 'search' é obrigatório"}), 400

    wikipedia.set_lang(lang)

    try:
        result = wikipedia.summary(search, sentences=4)
        return jsonify({"data": result})
    except wikipedia.DisambiguationError:
        return jsonify({"error": "Pesquisa não encontrada, tente novamente utilizando outro nome."}), 404

if __name__ == "__main__":
    app.run()
