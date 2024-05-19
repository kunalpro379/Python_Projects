TOKEN="7167763972:AAGSVaRyj4h7D7N8CHROqEbU1U8gxEFu6IY"
import telebot
import time

# Your bot's API token

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Dictionary to store bot-related data
bot_data = {}

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot started. Send the username of the bot you want to connect and send messages to.")

# Handler for connecting to the provided bot username
@bot.message_handler(func=lambda message: True)
def connect_to_bot(message):
    # Extract the username from the message
    provided_bot_username = message.text.strip()

    # Retrieve information about the provided bot
    provided_bot_info = bot.get_chat(provided_bot_username)

    if provided_bot_info.type == "private" and provided_bot_info.is_bot:
        # If the provided username corresponds to a bot, send a confirmation message
        bot.reply_to(message, f"Provided bot username set to {provided_bot_username}. Send a message to start forwarding.")

        # Store the provided bot username for future use
        bot_data["provided_bot_username"] = provided_bot_username
    else:
        # If the provided username does not correspond to a bot, send an error message
        bot.reply_to(message, "Invalid bot username. Please provide a valid username of a bot.")

# Handler for forwarding messages to the provided bot
@bot.message_handler(func=lambda message: True)
def forward_message_to_provided_bot(message):
    provided_bot_username = bot_data.get("provided_bot_username")
    if provided_bot_username:
        # Forward the message to the provided bot
        bot.send_message(provided_bot_username, message.text)
    else:
        # If the provided bot username is not set, send an error message
        bot.reply_to(message, "No bot username provided. Use /start to set the bot username.")

# Start the bot
bot.polling()