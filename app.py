import os
from flask import Flask, render_template, request, jsonify
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

@app.route("/webhook", methods=["POST"])
def webhook():
    # Recebe a notificação do Mercado Pago
    data = request.json

    # Verifica se a notificação é válida
    if data and "data" in data:
        payment_id = data["data"]["id"]
        payment_status = data["data"]["status"]

        # Aqui você pode processar o status do pagamento
        # Por exemplo, atualizar o banco de dados ou enviar um e-mail
        print(f"Pagamento ID: {payment_id}, Status: {payment_status}")

        # Retorna uma resposta 200 OK para o Mercado Pago
        return jsonify({"status": "received"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400




port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
