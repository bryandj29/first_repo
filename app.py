from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡hola mundo, soy Bryan Delgado Justiz!"

@app.route('/version')
def version():
    return jsonify({"version": os.getenv("APP_VERSION", "No definida")})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  
    app.run(host="0.0.0.0", port=port)
