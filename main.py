from pathlib import Path

import telebot
from telebot import types

from config import TOKEN


bot = telebot.TeleBot(TOKEN)
BACK_TO_QUESTIONS = "Назад к вопросам"
CERTIFICATE_SAMPLE_QUESTION = "Образец электронного сертификата"
BASE_DIR = Path(__file__).resolve().parent
CERTIFICATE_SAMPLE_PATH = BASE_DIR / "assets" / "certificate_sample.png"

FAQ_ANSWERS = {
    "Как записаться на стрельбу?": (
        "Для брони нужны: ФИО, телефон, количество гостей "
        "(в т.ч. несовершеннолетних), дата, время.\n\n"
        "Выберите локацию: закрытый тир (нарезное оружие) "
        "или открытый стенд (гладкоствольное оружие: по движущимся "
        "и стационарным мишеням; перерыв 14:00-16:00).\n\n"
        "Укажите желаемые услуги. Либо услуги можно выбрать на месте."
    ),
    "Как оформить электронный сертификат?": (
        "Для оформления электронного сертификата в стрелковом "
        "комплексе \"300 метров\" (тир) необходимо предоставить "
        "следующие данные покупателя: фамилию, имя и отчество, "
        "адрес электронной почты, контактный номер телефона, "
        "а также указать желаемый номинал сертификата "
        "(100, 200, 300 или 500 рублей).\n\n"
        "Срок действия сертификата составляет один год "
        "с даты приобретения."
    ),
    "Возрастные ограничения?": (
        "Несовершеннолетним предоставляются услуги с письменного "
        "согласия законных представителей и в их присутствии "
        "(согласие подписывается у нас).\n\n"
        "Для несовершеннолетних услуги:\n"
        "- Пневматическая винтовка с 6-7 лет.\n"
        "- Малокалиберный карабин с 12 лет.\n"
        "- Малокалиберный пистолет, карабин Сайга-9, "
        "охотничье ружье с 14 лет.\n"
        "- Автомат и другое оружие с 16 лет и по согласованию "
        "с инструктором, исходя из антропометрических данных "
        "несовершеннолетнего лица."
    ),
    "Стоимость услуг?": (
        "Пистолеты - 8 р/1 выстрел.\n"
        "Карабины-автоматы - 10 р/1 выстрел.\n"
        "Винтовки - 13 р/1 выстрел.\n\n"
        "Также есть скидочные комплекты. Подробнее в Instagram "
        "или на сайте."
    ),
    "Наш инстаграм": "https://www.instagram.com/300metrov_by/",
}


def create_faq_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for question in FAQ_ANSWERS:
        keyboard.add(types.KeyboardButton(question))
    keyboard.add(types.KeyboardButton(CERTIFICATE_SAMPLE_QUESTION))
    return keyboard


def create_back_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(BACK_TO_QUESTIONS))
    return keyboard


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Выберите интересующий вопрос:",
        reply_markup=create_faq_keyboard(),
    )


@bot.message_handler(func=lambda message: message.text in FAQ_ANSWERS)
def answer_faq(message):
    bot.send_message(
        message.chat.id,
        FAQ_ANSWERS[message.text],
        reply_markup=create_back_keyboard(),
    )


@bot.message_handler(func=lambda message: message.text == CERTIFICATE_SAMPLE_QUESTION)
def send_certificate_sample(message):
    with CERTIFICATE_SAMPLE_PATH.open("rb") as certificate_file:
        bot.send_photo(
            message.chat.id,
            certificate_file,
            caption="Образец электронного сертификата",
            reply_markup=create_back_keyboard(),
        )


@bot.message_handler(func=lambda message: message.text == BACK_TO_QUESTIONS)
def back_to_questions(message):
    bot.send_message(
        message.chat.id,
        "Выберите интересующий вопрос:",
        reply_markup=create_faq_keyboard(),
    )


if __name__ == "__main__":
    bot.infinity_polling()
