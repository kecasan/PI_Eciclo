from gerencianet import Gerencianet
from django.conf import settings

def gerar_qr_code_pix(valor):
    credentials = {
        'client_id': settings.GERENCIANET_CLIENT_ID,
        'client_secret': settings.GERENCIANET_CLIENT_SECRET,
        'sandbox': True  # Mude para False em produção
    }
    gn = Gerencianet(credentials)
    body = {
        'calendario': {'expiracao': 3600},
        'valor': {'original': f'{valor:.2f}'},
        'chave': 'sua_chave_pix',
        'infoAdicionais': [{'nome': 'Pagamento', 'valor': 'Pedido #1234'}]
    }
    response = gn.pix_create_charge(body)
    return response['loc']['location']
