import telebot
from flask import Flask, request

API_TOKEN = '7558249369:AAF4A9L3Q9g0kLPT7wwH0BWasecImYlxrn8'  # ضع توكن البوت الخاص بك هنا
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# عندما المستخدم يرسل /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً!")

# استقبال الطلبات من تيليغرام عبر webhook
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# فقط لتجربة الاتصال
@app.route('/', methods=['GET'])
def index():
    return 'بوت تيليغرام يعمل!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
