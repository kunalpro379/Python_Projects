from collections import defaultdict
import os
import telebot

BOT_TOKEN = "6554382026:AAFOlcl-ZnDRedCjTrfVPhjQcRhqJqyWNxE"
bot = telebot.TeleBot(BOT_TOKEN)
user_info = {}
waiting_messages = defaultdict(list)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "🌟 Welcome to our Chat Bot! 🌟\n\n"
        "I'm here to help you connect with others while ensuring your privacy. "
        "Let's get started!\n\n"
        "First, please tell me your name."
    )
    bot.reply_to(message, welcome_message)
    user_info[message.chat.id] = {'name': None, 'gender': None}

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    chat_id = message.chat.id
    if user_info[chat_id]['name'] is None:
        user_info[chat_id]['name'] = message.text
        bot.reply_to(message, "Nice to meet you, {}. What's your gender? (Male/Female)".format(user_info[chat_id]['name']))
    elif user_info[chat_id]['gender'] is None:
        gender = message.text.lower()
        if gender in ['male', 'female']:
            user_info[chat_id]['gender'] = gender
            privacy_message = "Your privacy will be maintained. You will be connected with anonymous peers. Start the conversation with /startconv."
            bot.reply_to(message, privacy_message)
        else:
            bot.reply_to(message, "Please enter a valid gender (Male/Female).")

@bot.message_handler(commands=['startconv'])
def start_conversation(message):
    chat_id = message.chat.id
    if user_info[chat_id]['gender'] is not None:
        waiting_messages[chat_id].append(message)
        bot.reply_to(message, "Waiting for connection...")

@bot.message_handler(commands=['stopconv'])
def stop_conversation(message):
    bot.reply_to(message, "Connection stopped. Press /start to start a new conversation.")
    chat_id = message.chat.id
    user_info[chat_id] = {'name': None, 'gender': None}
    if chat_id in waiting_messages:
        del waiting_messages[chat_id]

@bot.message_handler(func=lambda msg: True)
def handle_waiting_messages(message):
    chat_id = message.chat.id
    if chat_id in waiting_messages and len(waiting_messages[chat_id]) > 0:
        for waiting_message in waiting_messages[chat_id]:
            bot.reply_to(waiting_message, "Connection started! Type your message or press /stopconv to end the conversation.")
        del waiting_messages[chat_id]

bot.infinity_polling()
