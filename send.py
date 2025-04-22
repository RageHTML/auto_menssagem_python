import requests
import time

# Configurações da API
id_instance = "7105230683"
api_token = "dd9b6c8fed124d179bae01d4b0bd8eea4dacec202d6b4a8f96"
base_url = f"https://api.green-api.com/waInstance{id_instance}"

def get_auth_status():
    """Verifica o status de autenticação da instância"""
    status_url = f"{base_url}/getStateInstance/{api_token}"
    try:
        response = requests.get(status_url, timeout=10)
        response.raise_for_status()  # Verifica se houve erro HTTP
        return response.json().get('stateInstance')
    except Exception as e:
        print(f"Erro ao verificar status: {e}")
        return None

def send_message(chatId, message):
    """Envia mensagem através da Green-API"""
    # Verifica autenticação
    status = get_auth_status()
    if status != "authorized":
        print("Sessão não autenticada. Por favor escaneie o QR Code:")
        print(f"QR URL: {base_url}/qr/{api_token}")
        return False
    
    # Prepara a requisição
    url = f"{base_url}/sendMessage/{api_token}"
    payload = {"chatId": chatId, "message": message}
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        if response.status_code == 200:
            return True
        print(f"Erro na API: {response.status_code} - {response.text}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False

# Mensagem longa (letra da música Ben 10)
mensagem = """A história começou
Quando um relógio esquisito
Grudou no pulso dele vindo lá do infinito
Agora tem poderes e com eles faz bonito
É o Ben 10
(Ben 10, Ben 10, Ben 10)

Se acaso encontrá-lo, você vai se admirar
Diante de seus olhos ele vai se transformar
Em um ser alienígena
Que bota pra quebrar
É o Ben 10
(Ben 10)

Com seus poderes vai combater
Os inimigos e vai vencer
Ele não foge de medo ou dor
Moleque muito irado
Seja onde for
É o Ben 10"""

# Loop de envio com tratamento aprimorado
while True:
    print("\nTentando enviar mensagem...")
    
    if send_message("5583991028769@c.us", mensagem):
        print("✅ Mensagem enviada com sucesso!")
    else:
        print("❌ Falha no envio - Verifique acima os erros")
    
    # Intervalo entre envios (reduzido para 3 segundos conforme seu código original)
    time.sleep(0.1)