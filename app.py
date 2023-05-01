from flask import Flask
from flask import request
from flask import Response
import requests
# import telegram
from blueBike import get_user_lat_long
# import telebot

 
TOKEN = "6205125004:AAFK5Gqn5AHJPGQRR5KW-7yPsGFJLrspPow"
app = Flask(__name__)
# bot = telebot.TeleBot(TOKEN)
 
# @app.route('/{}'.format(TOKEN), methods=['POST'])
# def respond():
#    # retrieve the message in JSON and then transform it to Telegram object
#    update = telegram.Update.de_json(request.get_json(force=True), bot)

#    chat_id = update.message.chat.id
#    msg_id = update.message.message_id

#    # Telegram understands UTF-8, so encode text for unicode compatibility
#    text = update.message.text.encode('utf-8').decode()
#    # for debugging purposes only
#    print("got text message :", text)
#    # the first time you chat with the bot AKA the welcoming message
#    if text == "/start":
#        # print the welcoming message
#        bot_welcome = """
#        Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
#        """
#        # send the welcoming message
#        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)


#    else:
#        try:
#            # clear the message we got from any non alphabets
#            text = re.sub(r"\W", "_", text)
#            # create the api link for the avatar based on http://avatars.adorable.io/
#            url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
#            # reply with a photo to the name the user sent,
#            # note that you can send photos by url and telegram will fetch it for you
#            bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
#        except Exception:
#            # if things went wrong
#            bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

#    return 'ok'


    


# @bot.message_handler(commands=['start', 'sup'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")


def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r

def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
        'caption': "This is a sample image"
    }
 
    r = requests.post(url, json=payload)
    return r

def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Which link would you like to visit?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "google", "url": "http://www.google.com/"},
                    {"text": "youtube", "url": "http://www.youtube.com/"}
                ]
            ]
        }
    }
 
    r = requests.post(url, json=payload)
 
    return r


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)

        if txt == "hi":
            tel_send_message(chat_id,"Hello!!")
        if txt == "nearby station":
            tel_send_message(chat_id,"The nearest bike station to you is")


        elif txt == "image":
            tel_send_image(chat_id)
        elif txt == "inlineurl":
            tel_send_inlineurl(chat_id)
        elif txt == "/start":
            tel_send_message(chat_id, "Hey there, how can I help you out here?")
        else:
            tel_send_message(chat_id,'from webhook')
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)