import telebot
import config
import parcer_hse_descripton
import universal_parcer_for_directions
from telebot import types


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    stick_in = open('stick_in.webp', 'rb')
    bot.send_sticker(message.chat.id, stick_in)

    # keyboard

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Смотреть программы обучения")
    item2 = types.KeyboardButton("Меня не интересует поступление")
    markup.add(item1, item2)

    if message.from_user.last_name == None:
        mess = f'Привет, {message.from_user.first_name}! Хочешь посмотреть образовательные программы?'
    else:
        mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Хочешь посмотреть ' \
               f'образовательные программы?'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def processing(message):
    angry_tyan = open('angry_tyan.webp', 'rb')
    sad_tyan = open('sad_tyan.webp', 'rb')
    interest_girl = open('interest_girl.webp', 'rb')
    if message.chat.type == 'private':
        if message.text == 'Смотреть программы обучения':
            markup = types.InlineKeyboardMarkup(row_width=2)
            for hse_dir in parcer_hse_descripton.all_directions_with_urls:
                item = types.InlineKeyboardButton(f'{str(hse_dir)}',
                                                  callback_data=parcer_hse_descripton.all_directions_with_urls[
                                                      hse_dir])
                markup.add(item)
            bot.send_sticker(message.chat.id, interest_girl)
            bot.send_message(message.chat.id, 'Выбирай программу, которая тебя интересует, и жми на кнопку!😉',
                             reply_markup=markup)

        elif message.text == 'Меня не интересует поступление':
            bot.send_sticker(message.chat.id, sad_tyan)
            bot.send_message(message.chat.id, "Боту грустно... Давай лучше все-таки выбирать направления для учебы")
        else:
            bot.send_message(message.chat.id, "Ты втираешь мне какую-то дичь")
            bot.send_sticker(message.chat.id, angry_tyan)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            for hse_dir_urls in parcer_hse_descripton.all_directions_with_urls:
                if call.data == parcer_hse_descripton.all_directions_with_urls[hse_dir_urls]:
                    url = parcer_hse_descripton.all_directions_with_urls[hse_dir_urls]
                    print(url)
                    local = universal_parcer_for_directions.Parse(url)
                    bot.send_message(call.message.chat.id, local.parcing())

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбирай программу, которая тебя интересует, и жми на кнопку!😉",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
