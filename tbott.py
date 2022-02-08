import telebot
import cgi
import html
from pyowm import OWM
from http.server import HTTPServer, CGIHTTPRequestHandler


# from pyowm.utils import config
# from pyowm.utils import timestamps

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text1 = html.escape(text1)

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5186477446:AAEi6Ht91BnXA4qp2mtwO4Dv5htPjQKgDPc", parse_mode=None)
bot.send_message(805818310, text1)

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)


# You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    # bot.reply_to(message, "Howdy, how are you doing, "+message.text)
    print(message.text)
    try:
        city = message.text.lower().replace("/wdfrbot", "").strip()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        bot.send_message(message.chat.id, f"Температура {city.title()} {w.temperature('celsius')['temp']}"
                                          f"\n чувствуется как {w.temperature('celsius')['feels_like']}"
                                          f"\n ещё {w.detailed_status}")

    except:
        bot.send_message(message.chat.id, "Не знаю такого города")


bot.polling(none_stop=True)
httpd.serve_forever()