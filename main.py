import os
from dotenv import load_dotenv
import telebot
import google.generativeai as genai

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_API_TOKEN"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ver la lista de modelos de Gemini
# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)

# model = genai.GenerativeModel("gemini-pro")
# response = model.generate_content("What is the meaning of life?")
# print(response.text)


def gemini_consult(query):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text


# responder a los comandos
@bot.message_handler(commands=["start"])
def cmd_start(message):
    """mensaje de bienvenida del bot"""
    bot.send_message(
        message.chat.id,
        "Hola soy un bot, puedes ingresar comando /cuidados para ver el cuidado de un tatuaje nuevo, comando /significado para conocer el significado de tatuajes, pero ademas como Soy una Inteligencia artificial, puedes consultarme sobre lo que quieras saber",
    )


@bot.message_handler(commands=["significado"])
def cmd_significado(message):
    """responde al comando significado"""
    bot.send_message(
        message.chat.id,
        "Para consultar el significado de un tatuaje, escribe significado de tatuajes de, y el tatuaje que te interresa",
    )


@bot.message_handler(commands=["cuidados"])
def cmd_significado(message):
    """responde al comando cuidados"""
    bot.send_message(
        message.chat.id,
        "Para cuidar tu tatuaje nuevo:\nQuitar el film, y enjuagar con agua.\nDejar descubierto y poner una fina capa de crema.\n No rascar, ni quitar la cascara \n No exponer al sol, agua de mar o pileta\n continuar los cuidados por dos semanas\n",
    )


# responder a los mensajes
@bot.message_handler(content_types=["text"])
def resp_msj(message):
    try:
        if message.text.lower() == "gracias":
            bot.send_message(
                message.chat.id,
                "De nada, si necesitas cualquier cosa escribe comando /start",
            )
        else:
            response = gemini_consult(message.text)
            bot.send_message(message.chat.id, response)
    except ValueError:
        print("Ha ocurrido un error", ValueError)


# Iniciar el bot
if __name__ == "__main__":
    print("Iniciando el bot...")
    bot.infinity_polling()
