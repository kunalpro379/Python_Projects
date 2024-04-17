from flask import Flask
import main  # Assuming main.py contains the code for your Telegram bot

app = Flask(__name__)

@app.route('/')
def start_bot():
    main.start_bot()
    return 'Telegram bot started!'

if __name__ == '__main__':
    app.run()
