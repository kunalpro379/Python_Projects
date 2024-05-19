
BOT_TOKEN = "6718811553:AAGFpd81zVJ6uws92JatHNYJz5K5UD_YtME"


import telebot
from collections import deque

bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()

# Queue to store users waiting to be paired
waiting_users_male = deque()
waiting_users_female = deque()

# Dictionary to store the chat IDs of connected users
connected_users = {}

# Dictionary to store the gender of users
user_gender = {}

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Hi {user_name}! Send /setgender to set your gender.")

# Handler for setting user gender
@bot.message_handler(commands=['setgender'])
def set_gender(message):
    user_chat_id = message.chat.id
    bot.reply_to(message, "Please set your gender (Male/Female).")
    bot.register_next_step_handler(message, process_set_gender_step)

def process_set_gender_step(message):
    user_chat_id = message.chat.id
    gender = message.text.strip().lower()
    if gender in ['male', 'female']:
        user_gender[user_chat_id] = gender
        bot.reply_to(message, f"Gender set as {gender.capitalize()}. Send /connect to start chatting.")
    else:
        bot.reply_to(message, "Invalid gender. Please set your gender as Male or Female.")

# Handler for the /connect command
@bot.message_handler(commands=['connect'])
def connect(message):
    if message.chat.id not in connected_users:
        if message.chat.id not in user_gender:
            bot.reply_to(message, "Please set your gender using /setgender command.")
        else:
            user_chat_id = message.chat.id
            user_gender_val = user_gender[user_chat_id]

            # Check if there are users of the opposite gender available
            if user_gender_val == 'male':
                if len(waiting_users_female) > 0:
                    partner_chat_id = waiting_users_female.popleft()
                    connect_users(user_chat_id, partner_chat_id)
                else:
                    # If no female users available, connect with any available user
                    if len(waiting_users_male) > 0:
                        partner_chat_id = waiting_users_male.popleft()
                        connect_users(user_chat_id, partner_chat_id)
                    else:
                        bot.send_message(user_chat_id, "No available users to connect. Please wait...")
            else:
                if len(waiting_users_male) > 0:
                    partner_chat_id = waiting_users_male.popleft()
                    connect_users(user_chat_id, partner_chat_id)
                else:
                    # If no male users available, connect with any available user
                    if len(waiting_users_female) > 0:
                        partner_chat_id = waiting_users_female.popleft()
                        connect_users(user_chat_id, partner_chat_id)
                    else:
                        bot.send_message(user_chat_id, "No available users to connect. Please wait...")

def connect_users(user_chat_id, partner_chat_id):
    user_name = bot.get_chat(user_chat_id).first_name
    partner_name = bot.get_chat(partner_chat_id).first_name
    connected_users[user_chat_id] = partner_chat_id
    connected_users[partner_chat_id] = user_chat_id
    bot.send_message(user_chat_id, f"Connected with {partner_name}! You can start chatting now.")
    bot.send_message(partner_chat_id, f"Connected with {user_name}! You can start chatting now.")

# Handler for the /disconnect command
@bot.message_handler(commands=['disconnect'])
def disconnect(message):
    user_chat_id = message.chat.id
    if user_chat_id in connected_users:
        partner_chat_id = connected_users.pop(user_chat_id)
        if partner_chat_id in connected_users:
            connected_users.pop(partner_chat_id)
            bot.send_message(user_chat_id, "You have been disconnected.")
            bot.send_message(partner_chat_id, "Your partner has disconnected.")
        else:
            bot.reply_to(message, "Error: Partner's chat ID not found.")
    else:
        bot.reply_to(message, "You are not currently connected to anyone.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    # Check if the user is connected
    if message.chat.id in connected_users and connected_users[message.chat.id]:
        # Send the message to the connected user
        bot.send_message(connected_users[message.chat.id], message.text)
    else:
        bot.reply_to(message, "You are not connected. Send /connect to start.")

# Handler for handling new chat members (assuming it's a private chat)
@bot.message_handler(func=lambda message: message.new_chat_members is not None and len(message.new_chat_members) > 0)
def handle_new_chat_member(message):
    bot.reply_to(message, "This is a private chat. To start chatting, send /connect.")

# Handler for handling inline queries
@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    pass  # Do nothing for now

# Start the bot
bot.polling()