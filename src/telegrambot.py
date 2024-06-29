import telebot
import scrapping
import time

# Chave API bot
CHAVE_API = "7226131459:AAFYpyhi2DuvQ0Yh4dtmYH6Qs3cKBXA1dy0"

bot = telebot.TeleBot(CHAVE_API)

# Função para enviar a mensagem
def enviar_mensagem():
    preco_atual = scrapping.get_atual_price()
    preco_anterior = scrapping.get_anterior_price()
    nome_atual = scrapping.get_name()
    desconto_atual = scrapping.get_desconto()

    texto = f"""Produto: {nome_atual}
Preço anterior: R${preco_anterior}
Preço atual: R${preco_atual}
Desconto: {desconto_atual}
Link: {scrapping.url}"""
    
    # Obtém a lista de todos os chats que o bot está ativo
    for chat in bot.get_updates():
        chat_id = chat.message.chat.id  # Obtém o ID do chat
        bot.send_message(chat_id, texto)  # Envia a mensagem para o chat correspondente

# Loop para enviar a mensagem a cada 10 segundos
while True:
    enviar_mensagem()
    time.sleep(10)