
BOT_TOKEN = "6718811553:AAGFpd81zVJ6uws92JatHNYJz5K5UD_YtME"
import telebot
from collections import deque


# Create a bot instance
bot = telebot.TeleBot(BOT_TOKEN)

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
    bot.reply_to(message, "Hi! Send /connect to start chatting with a user of the opposite gender.")

# Handler for the /connect command
@bot.message_handler(commands=['connect'])
def connect(message):
    if message.chat.id not in connected_users:
        if message.chat.id not in user_gender:
            bot.reply_to(message, "Please set your gender using /setgender command.")
        else:
            user_chat_id = message.chat.id
            user_gender_val = user_gender[user_chat_id]
            
            if user_gender_val == 'male':
                if len(waiting_users_female) > 0:
                    partner_chat_id = waiting_users_female.popleft()
                    connected_users[user_chat_id] = partner_chat_id
                    connected_users[partner_chat_id] = user_chat_id
                    bot.send_message(user_chat_id, "Connected! You can start chatting now.")
                    bot.send_message(partner_chat_id, "Connected! You can start chatting now.")
                else:
                    waiting_users_male.append(user_chat_id)
                    bot.send_message(user_chat_id, "Waiting for a female user to connect...")
            else:
                if len(waiting_users_male) > 0:
                    partner_chat_id = waiting_users_male.popleft()
                    connected_users[user_chat_id] = partner_chat_id
                    connected_users[partner_chat_id] = user_chat_id
                    bot.send_message(user_chat_id, "Connected! You can start chatting now.")
                    bot.send_message(partner_chat_id, "Connected! You can start chatting now.")
                else:
                    waiting_users_female.append(user_chat_id)
                    bot.send_message(user_chat_id, "Waiting for a male user to connect...")

# Handler for setting user gender
@bot.message_handler(commands=['setgender'])
def set_gender(message):
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

# Handler for the /disconnect command
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
