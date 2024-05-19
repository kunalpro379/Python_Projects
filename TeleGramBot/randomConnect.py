
BOT_TOKEN = "6718811553:AAGFpd81zVJ6uws92JatHNYJz5K5UD_YtME"

import json
import os
import telebot
from collections import deque

bot = telebot.TeleBot(BOT_TOKEN)


import random


# Queue to store users waiting to be paired
waiting_users = deque()

# Dictionary to store the chat IDs of connected users
connected_users = {}

# Dictionary to store the usernames of connected users
connected_usernames = {}

# Handler for the /start command
# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    user_username = message.from_user.username
    user_id = message.from_user.id
    print(f"User ID: {user_id}, Username: {user_username}, Name: {user_name}")
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
        bot.reply_to(message, f"Gender set as {gender.capitalize()}. Send /connect to start chatting.")
    else:
        bot.reply_to(message, "Invalid gender. Please set your gender as Male or Female.")

# Handler for the /connect command
@bot.message_handler(commands=['connect'])
def connect(message):
    if message.chat.id not in connected_users:
        user_chat_id = message.chat.id
        user_username = message.from_user.username
        waiting_users.append((user_chat_id, user_username))
        
        if len(waiting_users) >= 2:
            user1_data = waiting_users.popleft()
            user2_data = waiting_users.popleft()
            
            user1_chat_id, user1_username = user1_data
            user2_chat_id, user2_username = user2_data
            
            connected_users[user1_chat_id] = user2_chat_id
            connected_users[user2_chat_id] = user1_chat_id
            
            connected_usernames[user1_chat_id] = user2_username
            connected_usernames[user2_chat_id] = user1_username
            
            user1_name = bot.get_chat(user1_chat_id).first_name
            user2_name = bot.get_chat(user2_chat_id).first_name
            
            bot.send_message(user1_chat_id, f"Connected with {user2_name}! You can start chatting now.")
            bot.send_message(user2_chat_id, f"Connected with {user1_name}! You can start chatting now.")
            
            # Print JSON data of connected users
            connected_data = {
                user1_chat_id: {
                    "username": user1_username,
                    "name": user1_name
                },
                user2_chat_id: {
                    "username": user2_username,
                    "name": user2_name
                }
            }
            print(json.dumps(connected_data, indent=4))
            
            # Print pairs of connected usernames
            print(f"Connected users: {user1_username} and {user2_username}")
        else:
            bot.send_message(user_chat_id, "Waiting for another user to connect...")

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