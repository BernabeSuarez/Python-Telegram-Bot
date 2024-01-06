import os
from dotenv import load_dotenv
import telebot


load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_API_TOKEN"))


# responder a los comandos
@bot.message_handler(commands=["start", "ayuda"])
def cmd_start(message):
    """mensaje de bienvenida del bot"""
    bot.send_message(
        message.chat.id,
        "Hola! Bienvenido, soy un bot, te paso una lista de las cosas que puedo ayudarte: \n responde:\n 1: si quieres un turno para tatuarte\n 2: Si quieres saber el costo de un tatuaje \n 3: Si quieres conocer los cuidados recomendados para tu nuevo tatuaje.\n 4 : Para salir",
    )


# responder a los mensajes
@bot.message_handler(content_types=["text"])
def resp_msj(message):
    """Intereactua con los mensajes recibidos"""
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible por el momento...")
    else:
        # lo que respondera a los textos
        if message.text.startswith("1"):
            bot.send_message(
                message.chat.id,
                "Para reservar un turno, enviar un mensaje al 2364513422, con la idea a realizar, si hay alguna imagen de referencia, tamaño aproximado o lugar del cuerpo a realizar el tatuaje",
            )
        elif message.text.startswith("2"):
            bot.send_message(
                message.chat.id,
                "Para presupuestar un tatuaje, es necesario saber el tamaño aproximado, y el diseño, partiendo de que hay un costo minimo fijo de base",
            )
        elif message.text.startswith("3"):
            bot.send_message(
                message.chat.id,
                "Los cuidados basicos son: No rascar, ni quitar la cascara, ponerle crema, y dejarse de hinchar las pelotas con el agua, pileta o mar",
            )
        elif message.text.startswith("4"):
            bot.send_message(
                message.chat.id,
                "Muchas gracias por contactarte",
            )


# Iniciar el bot
if __name__ == "__main__":
    print("Iniciando el bot...")
    bot.infinity_polling()
