import os
from flask import Flask, render_template
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("home.html", link_pagamento=link_iniciar_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
