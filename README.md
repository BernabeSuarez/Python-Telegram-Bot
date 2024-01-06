# Bot de Telegram para Consultas sobre Tatuajes

Este es un bot de Telegram creado en Python para ofrecer información sobre turnos, costos y cuidados relacionados con tatuajes.

## Requisitos

- Python
- `python-telegram-bot` (instalable a través de `pip install python-telegram-bot`)
- Archivo `.env` con la variable `TELEGRAM_API_TOKEN` configurada

## Descripción

Este bot utiliza la librería `python-telegram-bot` para interactuar con usuarios de Telegram. Responde a comandos y mensajes de texto proporcionando información sobre reservas de turnos, presupuestos para tatuajes y cuidados posteriores.

## Configuración

1. Clona este repositorio: `git clone https://github.com/tu_usuario/tu_proyecto.git`
2. Crea un archivo `.env` y agrega tu token de la API de Telegram: `TELEGRAM_API_TOKEN=TU_TOKEN_AQUÍ`
3. Instala las dependencias: `pip install python-telegram-bot`
4. Ejecuta el archivo `bot.py` para iniciar el bot.

## Uso

El bot responde a los siguientes comandos:

- `/start` o `/ayuda`: Muestra un mensaje de bienvenida con las opciones disponibles.
- Texto: Responde a mensajes de texto específicos proporcionando información detallada sobre turnos, costos y cuidados para tatuajes.

## Contribuciones

Si deseas contribuir:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature`)
3. Haz commit de tus cambios (`git commit -am 'Agrega funcionalidad'`)
4. Sube la rama (`git push origin feature`)
5. Abre un Pull Request.

## Créditos

Este proyecto utiliza la librería `python-telegram-bot` para la interacción con la API de Telegram.
