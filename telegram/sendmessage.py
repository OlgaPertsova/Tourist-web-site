import requests
from .models import *


def send_tg(tg_name, tg_email, tg_tel, tg_nik, tg_people, tg_date):
    settings = TgSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = "https://api.telegram.org/bot"
    method = api + token + "/sendMessage"

    if (text.find("{") and text.find("}")
            and text.find("[")
            and text.find("]")
            and text.find("(")
            and text.find(")")
            and text.find("-")
            and text.find("--")
            and text.find("=")
            and text.find("+")
            and text.rfind("{")):
        part_1 = text[:text.find("{")]
        part_2 = text[text.find("}") + 1:text.find("[")]
        part_3 = text[text.find("]") + 1:text.find("(")]
        part_4 = text[text.find(")") + 1:text.find("-")]
        part_5 = text[text.find("*") + 1:text.find("=")]
        part_6 = text[text.find("+") + 1:text.rfind("{")]

        text_slice = (part_1 + tg_name +
                      part_2 + tg_email +
                      part_3 + str(tg_tel) +
                      part_4 + tg_nik +
                      part_5 + str(tg_people) +
                      part_6 + str(tg_date))
    else:
        text_slice = text

    try:
        req = requests.post(method, data={
            'chat_id': chat_id,
            'text': text_slice
        })
    finally:
        if req.status_code != 200:
            print("Ошибка отправки")
        elif req.status_code == 500:
            print("Ошибка сервера")
        else:
            print("Сообщение отправлено")

