import requests
import random
import time
from datetime import datetime
from telegram import Bot

TOKEN = "8007319499:AAFGBS61UcM3t4Jb60a5X_wJgMCKYpMZfSQ"
CHAT_ID = "-3714429080"

bot = Bot(token=TOKEN)

inicio_msgs = [
    "☀️ Bom dia! Vamos começar mais um dia de ofertas e achados.",
    "🔥 Começando as ofertas de hoje!",
    "🚀 Dia novo, ofertas novas!"
]

fim_msgs = [
    "🌙 Encerrando as ofertas de hoje!",
    "🛑 As promoções de hoje ficam por aqui.",
    "📦 Até amanhã com mais ofertas!"
]

def enviar(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

def buscar_oferta():
    url = "https://api.mercadolibre.com/sites/MLB/search?q=smartphone"
    r = requests.get(url).json()

    item = random.choice(r["results"])

    return f"""
🔥 OFERTA

📦 {item['title']}
💰 R$ {item['price']}

🔗 {item['permalink']}
"""

inicio_enviado = False
fim_enviado = False

while True:
    agora = datetime.now()

    hora = agora.hour
    minuto = agora.minute

    if hora == 8 and minuto == 0 and not inicio_enviado:
        enviar(random.choice(inicio_msgs))
        inicio_enviado = True

    if hora >= 8 and hora < 20:
        enviar(buscar_oferta())
        time.sleep(random.randint(1800, 5400))

    if hora == 20 and minuto == 0 and not fim_enviado:
        enviar(random.choice(fim_msgs))
        fim_enviado = True

    if hora == 0:
        inicio_enviado = False
        fim_enviado = False

    time.sleep(60)
