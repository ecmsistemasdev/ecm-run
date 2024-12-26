import mercadopago


def gerar_link_pagamento():

    sdk = mercadopago.SDK("APP_USR-4419840842819511-121317-8c522deb54aff8ea290465f557bcdf0b-96531112")

    payment_data = {
        "items": [
            {"id": "1", "title": "Teste", "quantity": 1, "currency_id": "BRL", "unit_price": 1.00}
        ],
        "back_urls": {
            "success": "http://ecmrun.com.br/sucesso",
            "failure": "http://ecmrun.com.br/falha",
            "pending": "http://ecmrun.com.br/penndente",
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    
    return link_iniciar_pagamento
