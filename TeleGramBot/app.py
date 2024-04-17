from flask import Flask
import main
app = Flask(__name__)

@app.route('/')
def main():
    main.start_bot()
    return "Bot is running!"

if __name__ == '__main__':
    app.run()
