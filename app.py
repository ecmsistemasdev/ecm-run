from flask import Flask, render_template, jsonify
from gerencianet import Gerencianet
import qrcode
import base64
from io import BytesIO
import json
import os

app = Flask(__name__)

# Configurações da Gerencianet
CREDENTIALS = {
    'client_id': 'Client_Id_a1a8fcd9338ce308b9fe06b73ef6f40fc2627e97',
    'client_secret': 'Client_Secret_63e0df2e45c3957af75520ad68a0ce2cf45b93ac',
    'sandbox': False  # Mude para False em produção
}

# Inicializa o objeto Gerencianet
gn = Gerencianet(CREDENTIALS)

def generate_qr_code(pix_code):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(pix_code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_charge', methods=['POST'])
def generate_charge():
    try:
        # Dados da cobrança
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'devedor': {
                'cpf': '66553075204',
                'nome': 'Elienai Monteiro'
            },
            'valor': {
                'original': '1.00'
            },
            'chave': '14e02a0f-3468-434c-895d-a7d9c60d874b',  # Sua chave PIX cadastrada na Gerencianet
            'solicitacaoPagador': 'Pagamento do Produto X'
        }

        # Gera a cobrança
        response = gn.pix_create_immediate_charge(body=body)
        
        # Gera QR Code
        qr_response = gn.pix_generate_qrcode(response['loc']['id'])
        
        # Converte QR Code para imagem base64
        qr_code_image = generate_qr_code(qr_response['qrcode'])
        
        return jsonify({
            'qr_code': qr_code_image,
            'txid': response['txid']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check_payment/<txid>')
def check_payment(txid):
    try:
        # Consulta o status do pagamento
        response = gn.pix_detail_charge(txid=txid)
        status = response['status']
        
        return jsonify({
            'status': status,
            'paid': status == 'CONCLUIDA'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
