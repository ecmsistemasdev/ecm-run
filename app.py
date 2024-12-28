from flask import Flask, jsonify, request, render_template
import mercadopago
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

#sdk = mercadopago.SDK(app.config['MP_ACCESS_TOKEN'])

sdk = mercadopago.SDK("APP_USR-4419840842819511-121317-8c522deb54aff8ea290465f557bcdf0b-96531112")
mp_publckey = "APP_USR-0b9acce0-2c45-48b5-9837-9279769b5e31"


@app.route('/')
def index():
    return render_template('index.html', 
                         public_key=mp_publckey)

@app.route('/create_preference', methods=['POST'])
def create_preference():
    try:
        preference_data = {
            "items": [
                {
                    "title": "Produto de Exemplo",
                    "quantity": 1,
                    "currency_id": "BRL",
                    "unit_price": 1.0
                }
            ],
            "back_urls": {
                "success": "https://ecmrun.up.railway.app//sucesso",
                "failure": "https://ecmrun.up.railway.app//falha",
                "pending": "https://ecmrun.up.railway.app//pendente"
            },
            "notification_url": "https://ecmrun.up.railway.app//webhook",
        }
        
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        
        return jsonify({
            "id": preference["id"],
            "init_point": preference["init_point"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        
        if data['type'] == 'payment':
            payment_id = data['data']['id']
            payment_info = sdk.payment().get(payment_id)
            
            # Aqui você pode salvar as informações do pagamento em um banco de dados
            # E emitir um evento para o frontend via WebSocket, SSE ou fazer polling
            
            return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/payment_status/<payment_id>')
def payment_status(payment_id):
    try:
        payment_info = sdk.payment().get(payment_id)
        return jsonify(payment_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)



# port = int(os.environ.get("PORT", 5000))
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=port)
