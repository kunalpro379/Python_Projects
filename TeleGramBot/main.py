import telebot

BOT_TOKEN = "6554382026:AAFOlcl-ZnDRedCjTrfVPhjQcRhqJqyWNxE"
bot = telebot.TeleBot(BOT_TOKEN)

# Define a dictionary to store user information
user_info = {}

# Define a handler for the /start command
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

# Define a handler for all messages
@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    chat_id = message.chat.id
    if user_info[chat_id]['name'] is None:
        user_info[chat_id]['name'] = message.text
        bot.reply_to(message, f"Nice to meet you, {user_info[chat_id]['name']}. What's your gender? (Male/Female)")
    elif user_info[chat_id]['gender'] is None:
        gender = message.text.lower()
        if gender in ['male', 'female']:
            user_info[chat_id]['gender'] = gender
            privacy_message = "Your privacy will be maintained. You will be connected with anonymous peers. Start the conversation with /startconv."
            bot.reply_to(message, privacy_message)
            # Send user details to the server
            send_user_details(chat_id)
        else:
            bot.reply_to(message, "Please enter a valid gender (Male/Female).")

# Define a handler for the /startconv command
@bot.message_handler(commands=['startconv'])
def start_conversation(message):
    chat_id = message.chat.id
    if user_info[chat_id]['gender'] is not None:
        bot.reply_to(message, "Waiting for connection...")

# Define a function to send user details to the server
def send_user_details(chat_id):
    try:
        import socket
        # Connect to the server
        server_host = '127.0.0.1'  # Change this to the server's IP address if it's running on a different machine
        server_port = 5050
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        
        # Send user details to the server
        name = user_info[chat_id]['name']
        gender = user_info[chat_id]['gender']
        client_socket.sendall(str(chat_id).encode())
        client_socket.sendall(name.encode())
        client_socket.sendall(gender.encode())
        
        # Close the connection
        client_socket.close()
    except Exception as e:
        print(f"Error sending user details: {e}")

# Start the bot
bot.infinity_polling()
