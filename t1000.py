import random

import requests
from flask import json
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

class User():
    id = ""
    marker = 0
    role = "noob"
    reputation = 0
    def __init__(self, id):
        self.id=id

    def answer(self, txt):
        txt = txt.lower()
        print(txt)
        print(self.id)
        print(self.marker)
        if txt == "начать":
            self.marker = 0
        if self.marker == 0:
            if txt == "начать":
                vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                                 keyboard='{"buttons": [], "one_time": true}', user_id=self.id,
                                 random_id=get_random_id())
                self.marker = 1
            else:
                vk.messages.send(message="Wanna play - let's play",
                                 user_id=self.id,
                                 random_id=get_random_id())
                vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                                 keyboard='{"buttons": [], "one_time": true}', user_id=self.id,
                                 random_id=get_random_id())
                self.marker = 1
        else:
            if self.marker//10 == 1 or self.marker == 1:
                if (txt == "привет, дружок пирожок" or
                txt == "привет дружок пирожок" or
                txt == "ну привет дружок пирожок" or
                txt == "ну привет, дружок пирожок"):
                    print("i got here")
                    vk.messages.send(message="кто ты?", user_id=event.user_id, random_id=get_random_id(),
                                     keyboard=open("keyboard.json", "r", encoding="UTF-8").read())
                    self.marker = 2
                else:
                    if self.marker == 1:
                        vk.messages.send(
                            user_id=event.user_id,
                            attachment="photo-206593708_457239017",
                            message='держи крепкую мужскую помощь',
                            random_id=get_random_id()
                        )
                        self.marker = 11
                    if self.marker == 11:
                        vk.messages.send(
                            user_id=event.user_id,
                            message='подумай получше, будь вежлив',
                            random_id=get_random_id()
                        )
            else:
                if self.marker == 2:
                    if txt == "fucking slave":
                        vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                         keyboard=open("key2.json", "r", encoding="UTF-8").read())
                        self.marker = 3
                        self.role = txt
                    if txt == "boy next door":
                        vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                         keyboard=open("key3.json", "r", encoding="UTF-8").read())
                        self.marker = 3
                        self.role = txt
                    if txt == "dungeon master":
                        vk.messages.send(message="nice to meet you, bro", user_id=self.id, random_id=get_random_id(),
                                         keyboard=open("key4.json", "r", encoding="UTF-8").read())
                        self.marker = 3
                        self.role = txt
                    elif self.marker == 2:
                        vk.messages.send(message="well, just love gachi", user_id=self.id, random_id=get_random_id())
                        self.marker = 3
                        self.role = txt
                    vk.messages.send(message="наверное тебе будет интересно", user_id=self.id,
                                     random_id=get_random_id(),
                                     keyboard=open("key5.json", "r", encoding="UTF-8").read())
                    self.marker = 4

                else:
                    if self.marker == 3:
                        vk.messages.send(message="наверное тебе будет интересно", user_id=self.id,
                                         random_id=get_random_id(),
                                         keyboard=open("key5.json", "r", encoding="UTF-8").read())
                        self.marker = 4
                    if self.marker == 4 and txt == "тру гачи мемы":
                        links = open('photos.json', 'r')
                        parsed_links = json.load(links)
                        vk.messages.send(
                            message="наслаждайся",
                            user_id=event.user_id,
                            attachment=random.choice(parsed_links["items"])['link'],
                            random_id=get_random_id()
                        )
                    if self.marker == 4 and txt == "right versions":
                        links = open('videos.json', 'r')
                        parsed_links = json.load(links)
                        vk.messages.send(
                            user_id=event.user_id,
                            message = random.choice(parsed_links["items"])['link'],
                            random_id=get_random_id()
                        )


                    #vk.messages.send(message="I didn't learn it yet", user_id=event.user_id, random_id=get_random_id())



user_base = []

users = open("users.json","r")

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print(len(user_base))
            print(user_base)
            new = True
            for i in range(len(user_base)):
                print(len(user_base))
                if user_base[i].id == event.user_id:
                    new = False
                    user_base[i].answer(event.text)
                    break
            if new:
                user = User(event.user_id)
                user.answer(event.text)
                user_base.append(user)
