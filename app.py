from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def index():
    peso = request.args.get('peso', type=float)
    altura = request.args.get('altura', type=float)
    if peso and altura:
        imc = calcular_imc(peso, altura)
    else:
        imc = ""

    return (
        	"""<h1>Calcule seu IMC</h1>
            <h3>Colocar apenas números inteiros<br />
            Ex: se seu peso for 78,4 - coloque apenas 78<br />
            Ex: se sua altura for 1,81 - coloque apenas 181</h3>
            """
            """<form method="get">
                    <label for="peso">Peso: </label>
                    <input type="number" name="peso" id="peso" placeholder="Ex: 75" required>
                    <br /> <br />
                    <label for="altura">Altura: </label>
                    <input type="number" name="altura" id="altura" placeholder="Ex: 170" required>                    
                    <br /> <br /> 
                    <button type="submit">Calcular</button>
                </form>"""
            + '<h2 id="imc">' + imc + '</h2>'
    )
 
@app.route("/<int:peso><int:altura>")
def calcular_imc(peso, altura):
    calculo = round(peso / altura**2 * (10000), 1)

    if calculo < 18.5:
        grau = "abaixo do peso"
    elif calculo >= 18.5 and calculo <= 24.9:
        grau = "peso normal"
    elif calculo >= 25 and calculo <= 29.9:
        grau = "acima do peso"
    elif calculo >= 30 and calculo <= 39.9:
        grau = "obesidade"
    elif calculo >= 40:
        grau = "obesidade grave"

    imc = ("Seu IMC é {} considerado {} segundo a OMS.".format(calculo, grau))

    return str(imc)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
