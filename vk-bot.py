import random

import requests
from requests import session
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
import time

vk_session = vk_api.VkApi(token='ddb5080ac5e999ff2bb1e3b466d0e58c4f36df8fcf0b081267c4d433500162660200ea980b97efc8c1a4c')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def welcumm():
    marker = 0
    for event in longpoll.listen():
        marker2 = False
        user_id = ''
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and \
                (not marker2 or user_id == event.user_id):
            user_id = event.user_id
            marker2 = True
            answer = event.text.lower().rstrip().lstrip()
            print(answer)
            if answer == "начать":
                vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                                 keyboard='{"buttons": [], "one_time": true}', user_id=event.user_id,
                                 random_id=get_random_id())
                marker = 1
            elif marker == 0:
                vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                                 keyboard='{"buttons": [], "one_time": true}', user_id=event.user_id,
                                 random_id=get_random_id())
                print(event.text)
                marker = 1
            elif (marker // 10 == 1 or marker == 1) and (answer == "привет, дружок пирожок" or
                                                         answer == "привет дружок пирожок" or
                                                         answer == "ну привет дружок пирожок" or
                                                         answer == "ну привет дружок-пирожок"):
                vk.messages.send(message="кто ты?", user_id=event.user_id, random_id=get_random_id(),
                                 keyboard=open("keyboard.json", "r", encoding="UTF-8").read())
                marker = 2

            elif marker == 1 and (answer != "привет, дружок пирожок" or
                                  answer != "привет дружок пирожок" or
                                  answer != "ну привет дружок пирожок" or
                                  answer != "ну привет дружок-пирожок"):
                vk.messages.send(
                    user_id=event.user_id,
                    attachment="photo-206593708_457239017",
                    message='держи крепкую мужскую помощь',
                    random_id=get_random_id()
                )
                marker = 11

            elif marker == 2 and answer == "fucking slave":
                vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                 keyboard=open("key2.json", "r", encoding="UTF-8").read())
                marker = 3

            elif marker == 2 and answer == "boy next door":
                vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                 keyboard=open("key3.json", "r", encoding="UTF-8").read())
                marker = 3

            elif marker == 2 and answer == "dungeon master":
                vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                 keyboard=open("key4.json", "r", encoding="UTF-8").read())
                marker = 3

            elif marker == 2:
                vk.messages.send(message="well, just love gachi", user_id=event.user_id, random_id=get_random_id())
                marker = 3
            if marker == 3:
                return user_id
                break


u_id = welcumm()
print(u_id)


class User():
    id = ""
    marker = 0

    def __init__(self, id):
        self.id = id


user_base = []
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        new = True
        for i in user_base:
            if user_base[i].id == event.user_id:
                new = False
        if new:
            user = User(event.user_id)
            user_base.append(user)



