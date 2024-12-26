import mercadopago



def gerar_link_pagamento(title, quantity, unit_price):
    
    sdk = mercadopago.SDK("APP_USR-4419840842819511-121317-8c522deb54aff8ea290465f557bcdf0b-96531112")

    payment_data = {
        "items": [
            {"id": "1", 
             "title": title, 
             "quantity": quantity, 
             "currency_id": "BRL", 
             "unit_price": unit_price}],
        "back_urls": {
            "success": "http://ecmrun.com.br/sucesso",
            "failure": "http://ecmrun.com.br/falha",
            "pending": "http://ecmrun.com.br/penndente",
        },
        "payment_method_id": "pix"
    }

    # Cria o pagamento
    result = sdk.payment().create(payment_data)

    # Obtém a resposta do pagamento
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]

    return link_iniciar_pagamento
