import telebot
from telebot import types
from time import gmtime, strftime
from weather import getWeatherByCityId

cmd_list = ["/help вывод списка текущих команд\r\n",
            "/time вывод текущего времени\r\n",
            "/start начало диалога\r\n",
            "/hi приветствие\r\n",
            "/weather погода в Москве\r\n"]


token = ''
bot = telebot.TeleBot(token)

# common functions
def getCurrentTime():
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime());
    return 'Текущее время:\r\n' + time

# Commands
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "Узнать текущее время", "Узнать погоду в Москве")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message: types.Message):
    bot.send_message(message.chat.id, ''.join(cmd_list))

@bot.message_handler(commands=['weather'])
def getWeather(message: types.Message):
    weather = getWeatherByCityId(524901)
    bot.send_message(message.chat.id, weather)

@bot.message_handler(commands=['time'])
def currentTimeCmd(message: types.Message):
    time = getCurrentTime()
    bot.send_message(message.chat.id, time)

@bot.message_handler(commands=['hi'])
def hi(message: types.Message):
    msg = 'Привет! Давай пообщаемся.'
    bot.send_message(message.chat.id, msg)

# Message responses
@bot.message_handler(content_types=['text'])
def answer(message: types.Message):
    print("Новое сообщение: ", message.text)
    if message.text.lower() == 'хочу':
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    if message.text.lower() == 'узнать текущее время':
        time = getCurrentTime()
        bot.send_message(message.chat.id, time)
    if message.text.lower() == 'узнать погоду в москве':
        city_id = 524901
        weather = getWeatherByCityId(city_id)
        bot.send_message(message.chat.id, weather)
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю')

bot.infinity_polling()