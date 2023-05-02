from flask import Flask
from flask import request
from flask import Response
import requests
from blueBike import get_nearby_bike_stations, get_user_lat_long, get_trip_price, get_station_information
import telebot

TOKEN = "6215179642:AAEcF18YXRNFN_U7YAlJyKtBSMcDjSJa2Wo"
bot = telebot.TeleBot(TOKEN)
 
app = Flask(__name__)
 
def tel_parse_message(message):
    print("message-->",message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
 
        return chat_id,txt
    except:
        print("NO text found-->>")

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
 
    return r

def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Which plan do you want to know about?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Annual",
                    "callback_data": "annual"
                },
                {
                    "text": "Monthly",
                    "callback_data": "monthly"
                },
                {
                    "text": "Adventure",
                    "callback_data": "adventure"
                },
                {
                    "text": "Single",
                    "callback_data": "single"
                }
            ]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r
def getInput(update):
    query = update.callback_query.data
    return query

@ app.route('/', methods=['GET', 'POST'])

# def handle_callback_query(update, context):
#     print(update.callback_query.data)
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text='[handle_callback_query] callback data: ' + update.callback_query.data)
def index():
    bot_welcome = """
               Welcome to Bluebike bot! I am here to assist you to find out the number of available bikes at near Blue Bike stations
               Let's get riding! 

               Here are the list of commands I can help you with:
               1. /station_info
               2. /nearby_station
               3. /bike_pricing
               
               """
    # rental_types = ['annual membership', 'monthly membership', 'adventure pass', 'single trip']
    rental_prices = {
                    'annual membership': """The Annual Membership is $13/month
                            (or $129 paid in full) and includes
                            unlimited 45-minute rides. If you keep a
                            bike out longer than 45 minutes at a
                            time, it's an extra $2.50 per additional
                            30 minutes.""", 
                    'monthly membership': """The Monthly Membership is $29 for 30-
                            day access and includes unlimited 45-
                            minute rides. If you keep a bike out
                            longer than 45 minutes at a time, it's an
                            extra $2.50 per additional 30 minutes.""",
                    'adventure pass': """The Adventure Pass is even better
                            than renting a bike! It's only $10 for 24-
                            hour Bluebikes access and includes
                            unlimited 2-hour rides. If you keep a
                            bike out longer than 2 hours at a time,
                            it's an extra $4 per additional 30
                            minutes.""",
                    'single trip': """The Single Trip fare includes one ride
                            up to 30 minutes for $2.95, so it's great
                            for quick trips on-the-go. If you need to
                            ride longer, it's an extra $4 per
                            additional 30 minutes."""
                     }
    
    if request.method == 'POST':
        msg = request.get_json()
        try:
            chat_id, txt = tel_parse_message(msg)
            txt = txt.lower()
            if txt == "hi":
                tel_send_message(chat_id,"Hello, world!")

            elif txt == "/start":
                tel_send_message(chat_id, bot_welcome)

            elif txt == "/nearby_station":
                tel_send_message(chat_id,"Please enter your current location for me to return the 10 nearest stations to you")
                
            elif txt == "curry student center":
                tel_send_message(chat_id, get_nearby_bike_stations('curry student center'))
            elif txt == "babson college":
                tel_send_message(chat_id, get_nearby_bike_stations('babson college'))
            elif txt == "boston commons":
                tel_send_message(chat_id, get_nearby_bike_stations('boston commons'))
                

            elif txt == "/station_info":
                tel_send_message(chat_id,"Please enter the station ID")
            elif txt == "3":
                tel_send_message(chat_id,"This station at Colleges of the Fenway - Fenway at Avenue Louis Pasteur is active and has 9 available bikes")


            elif txt == "/bike_pricing":
                tel_send_inlinebutton(chat_id)

                if response == "annual":
                    tel_send_message(chat_id, rental_prices['annual membership'])

                elif response == "monthly":
                    tel_send_message(chat_id, rental_prices['monthly membership'])

                elif response == "adventure":
                    tel_send_message(chat_id, rental_prices['Adventure pass'])

                else:
                    tel_send_message(chat_id, rental_prices['single trip'])
                    tel_send_message(chat_id, "Would you like to calculate the cost of a single trip?")
                    response = getInput()
                    if response:
                        if response.lower() == "yes":
                            tel_send_message(chat_id, "How many minutes will you be renting the bike for?")
                            response = getInput()
                            if response:
                                price = get_trip_price(int(response))
                                tel_send_message(chat_id, f"Your trip will cost approximately {price}")

            elif txt == "/single_trip":
                tel_send_message(chat_id, "How many minutes will you be renting the bike for?")
            elif txt == "30":
                price = get_trip_price(int(txt))
                tel_send_message(chat_id, f"Your trip will cost approximately {price}")

            else:
                tel_send_message(chat_id, 'Sorry, I dont get what you mean! Try sending me other commands instead.')
        except:
            print("from index-->")
 
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
    app.run(threaded=True)






# -------------------------------------


# from flask import Flask
# from flask import request
# from flask import Response
# import requests
# from blueBike import get_nearby_bike_stations, get_user_lat_long, get_trip_price, get_station_information
# import telebot

# TOKEN = "6215179642:AAEcF18YXRNFN_U7YAlJyKtBSMcDjSJa2Wo"
# bot = telebot.TeleBot(TOKEN)
 
# app = Flask(__name__)

# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, """
#                Welcome to Bluebike bot! I am here to assist you to find out the number of available bikes at near Blue Bike stations
#                Let's get riding! 

#                Here are the list of commands I can help you with:
#                1. /station_info
#                2. /nearby_station
#                3. /bike_pricing
#                """)

# @bot.message_handler(commands=['station_info'])
# def get_station_ID(message):
#     text = "Enter the Station ID you are at! It can be found at the bike station itself"
#     sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(sent_msg, get_station_info)

# def get_station_info(message):
#     station_id = message.text
#     station_info = get_station_information(station_id)
#     bot.send_message(
#         message.chat.id, station_info , parse_mode="Markdown")


# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# bot.infinity_polling()



 
# if __name__ == '__main__':
#     app.run(threaded=True)