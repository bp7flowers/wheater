import telebot
from pyowm import OWM
from http.server import HTTPServer, CGIHTTPRequestHandler

# from pyowm.utils import config
# from pyowm.utils import timestamps

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5186477446:AAEi6Ht91BnXA4qp2mtwO4Dv5htPjQKgDPc", parse_mode=None)

# You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    # bot.reply_to(message, "Howdy, how are you doing, "+message.text)
    print(message.text)
    try:
        city = message.text.lower().replace("/wdfrbot", "").strip()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        bot.send_message(message.chat.id, w.temperature('celsius')['feels_like'])

    except:
        bot.send_message(message.chat.id, "Не знаю такого города")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
