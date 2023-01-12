# устанавливаем Flask
from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)


# Как только открывается раздел слэш(/) выполняется функция,
# а ее  результат отобразится в браузере
@app.route('/')
def main_page():
    return 'Hello, welcome to my chat!!!'


all_messages = []


# from datetime import datetime

def add_message(sender, text):
    from datetime import datetime
    #current_datetime = datetime.now()
    #current_hour = current_datetime.hour
    #current_minute = current_datetime.minute
    #current_time = f"{current_datetime.hour}:{current_minute}"
    new_message = {
        'name': sender,
        'text': text,
        'time': datetime.now().strftime('%H:%M'),
    }
    all_messages.append(new_message)




@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}  # Сообщения отобразятся в формате JSON



# HTTP-GET запрос
# /send_message?name=Mike&text=Hello
@app.route('/send_message')
def send_message():
    name = request.args.get('name')
    text = request.args.get('text')
    add_message(name, text)
    # ДЗ: добавить проверку имени и текста и выдавать ошибку
    return 'Message Sent'

@app.route('/chat')
def chat_page():
    return render_template('chat.html')


# Сохранение и загрузка сообщений

app.run()
