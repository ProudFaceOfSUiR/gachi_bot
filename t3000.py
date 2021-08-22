import random
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import urllib.request
import json
import urllib


def find_link(message):
    print("find link")
    words = message.split(" ")
    new_video = ""
    for i in words:#https://youtu.be/c9JNp6kdKqU
        print(i)
        try:
            print(i.find("youtube"))
            if "youtube.com" in i or "youtube.ru" in i:
                print("ch1")
                txt = i.split('=')[1]
                print(txt)
                params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % txt}
                url = "https://www.youtube.com/oembed"
                query_string = urllib.parse.urlencode(params)
                url = url + "?" + query_string
                with urllib.request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                    new_video = data['title']
            else:
                print("ch2")
                txt = i.split('/')[3]
                print(txt)
                params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % txt}
                url = "https://www.youtube.com/oembed"
                query_string = urllib.parse.urlencode(params)
                url = url + "?" + query_string
                with urllib.request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                    new_video = data['title']
            print(new_video)
        except BaseException:
            print("ok")
    return new_video

class User():
    id = ""
    marker = 0
    role = "noob"
    reputation = 0
    def __init__(self, id):
        self.id=id

    def answer(self, txt):
        raw_txt = txt
        txt = txt.lower()
        print(txt)
        print(self.id)
        print(self.marker)
        if txt == "начать":
            self.marker = 0
        if self.marker == 0 and txt == "начать":
            vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                             keyboard='{"buttons": [], "one_time": true}', user_id=self.id,
                             random_id=get_random_id())
            self.marker = 1
        elif self.marker == 0 and txt != "начать":
            vk.messages.send(message="Wanna play - let's play",
                             user_id=self.id,
                             random_id=get_random_id())
            vk.messages.send(message='поздоровойся, как полагается настоящему любителю мужской крепкой дружбы',
                             keyboard='{"buttons": [], "one_time": true}', user_id=self.id,
                             random_id=get_random_id())
            self.marker = 1
        elif (self.marker//10 == 1 or self.marker == 1) and (txt == "привет, дружок пирожок" or
                txt == "привет дружок пирожок" or
                txt == "ну привет дружок пирожок" or
                txt == "ну привет, дружок пирожок"):
            vk.messages.send(message="кто ты?", user_id=event.user_id, random_id=get_random_id(),
                             keyboard=open("keyboard.json", "r", encoding="UTF-8").read())
            self.marker = 2
        elif self.marker == 1 and not (txt == "привет, дружок пирожок" or
                txt == "привет дружок пирожок" or
                txt == "ну привет дружок пирожок" or
                txt == "ну привет, дружок пирожок"):
            vk.messages.send(
                user_id=event.user_id,
                attachment="photo-206593708_457239017",
                message='держи крепкую мужскую помощь',
                random_id=get_random_id()
            )
            self.marker = 11
        elif self.marker == 11:
            vk.messages.send(
                user_id=event.user_id,
                message='подумай получше, будь вежлив',
                random_id=get_random_id()
            )
        elif self.marker == 2:
            if txt == "fucking slave":
                vk.messages.send(message="nice to meet you, bro", user_id=event.user_id, random_id=get_random_id(),
                                 keyboard=open("key2.json", "r", encoding="UTF-8").read())
                self.marker = 3
                self.role = txt
            elif txt == "boy next door":
                if self.reputation < 100:
                    vk.messages.send(message="NoNoNo you are not gachi-man", user_id=event.user_id,
                                     random_id=get_random_id(),
                                     keyboard=open("key2.json", "r", encoding="UTF-8").read())
                    self.marker = 3
                    self.role = "fucking slave"
                else:
                    vk.messages.send(message="nice to meet you, bro", user_id=event.user_id,
                                     random_id=get_random_id(),
                                     keyboard=open("key3.json", "r", encoding="UTF-8").read())
                    self.marker = 3
            elif txt == "dungeon master":
                if self.reputation < 100:
                    vk.messages.send(message="NoNoNo you are not gachi-man", user_id=event.user_id,
                                     random_id=get_random_id(),
                                     keyboard=open("key2.json", "r", encoding="UTF-8").read())
                    self.marker = 3
                    self.role = "fucking slave"
                elif self.reputation < 300:
                    vk.messages.send(message="oh no, it's not your dungeon", user_id=event.user_id,
                                     random_id=get_random_id(),
                                     keyboard=open("key3.json", "r", encoding="UTF-8").read())
                    self.marker = 3
                else:
                    vk.messages.send(message="nice to meet you, bro", user_id=self.id, random_id=get_random_id(),
                                     keyboard=open("key4.json", "r", encoding="UTF-8").read())
                    self.marker = 3
            else:
                vk.messages.send(message="no, you have no more choices", user_id=self.id, random_id=get_random_id())
                self.marker = 2
                self.role = txt
            vk.messages.send(message="наверное тебе будет интересно", user_id=self.id,
                             random_id=get_random_id(),
                             keyboard=open("key5.json", "r", encoding="UTF-8").read())
            self.marker = 4

        elif self.marker == 3:
            vk.messages.send(message="наверное тебе будет интересно", user_id=self.id,
                             random_id=get_random_id(),
                             keyboard=open("key5.json", "r", encoding="UTF-8").read())
            self.marker = 4
        elif self.marker == 4 and txt == "тру гачи мемы":
            links = open('photos.json', 'r')
            parsed_links = json.load(links)
            vk.messages.send(
                message="наслаждайся",
                user_id=event.user_id,
                attachment=random.choice(parsed_links["items"])['link'],
                random_id=get_random_id(),keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
        elif self.marker == 4 and txt == "right versions":
            links = open('videos.json', 'r')
            parsed_links = json.load(links)
            vk.messages.send(
                user_id=event.user_id,
                message = random.choice(parsed_links["items"])['link'],
                random_id=get_random_id(),keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
        elif self.marker == 4 and txt == "gym":
            vk.messages.send(
                user_id=event.user_id,
                message="ты пришел в качалочку, закачай в меня больше тру гачи видосов, отправь ссылочку на настоящий гачи ремикс и смайлик на удачу ;-)",
                random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
            self.marker = 41
            print(self.id)
        elif self.marker == 41:
            print(txt)
            check = find_link(raw_txt)
            check = check.lower()
            if check == "":
                vk.messages.send(
                    user_id=event.user_id,
                    message="это не ссылочка, ты обманул своего Мастера",
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
                self.reputation -= 50
                self.marker = 4
            elif "gachi" in check or "гачи" in check or "right version" in check:
                vk.messages.send(
                    user_id=event.user_id,
                    message="неплохо, "+str(self.role),
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
                self.reputation+=40
                self.marker = 4
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="как-то не похоже на тру версию",
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
                self.role = 4
        elif self.marker == 42:
            vk.messages.send(
                user_id=event.user_id,
                message="кажется, ты что-то не дописал",
                random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
            self.reputation -=50
            self.marker = 4
        elif self.marker == 4:
            vk.messages.send(
                user_id=event.user_id,
                message="welcome to the club",
                random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )


vk_session = vk_api.VkApi(token='ddb5080ac5e999ff2bb1e3b466d0e58c4f36df8fcf0b081267c4d433500162660200ea980b97efc8c1a4c')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

user_base = []

with open('users.json') as json_file:
    data = json.load(json_file)
    i = 0
    for p in data['users']:
        user_base.append(User(p['id']))
        user_base[i].role = p['role']
        user_base[i].marker = p['marker']
        user_base[i].reputation = p['reputation']
        i+=1

print(user_base[0].id)
print(user_base[0].marker)

while True:
    for event in longpoll.listen():
        print(event.type)
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print(len(user_base))
            print(user_base)
            new = True
            for i in range(len(user_base)):
                print(len(user_base))
                if user_base[i].id == event.user_id:
                    new = False
                    print("ans1")
                    if event.text:
                        user_base[i].answer(event.text)
                    else:
                        user_base[i].marker = 42
                        user_base[i].answer("")
                    break
            if new:
                print("new")
                user = User(event.user_id)
                user.answer(event.text)
                user_base.append(user)
