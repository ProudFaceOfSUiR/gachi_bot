import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import urllib.request
import json
import urllib

def user_to_json(file):
    global user_base
    fh = open(file,"w")
    fh.write('{'+'\n'+'"users": ['+'\n')
    i = 0
    for users in user_base:
        i+=1
        txt = {
            "id": users.id,
            "role": str(users.role),
            "marker": users.marker,
            "reputation":users.reputation
        }
        # конвертируем в JSON:
        fh.write(json.dumps(txt))
        # в результате получаем строк JSON:
        if i != len(user_base):
            fh.write(",\n")
        else:
            fh.write("\n")
    fh.write("]\n}")


def new_link(link, file):
    new = True
    with open(file, "r") as file1:
        for line in file1:
            if link in line:
                new = False
    return new

def add_link(link, file):
    f = open(file, "r")
    contents = f.readlines()
    f.close()
    index = 2
    value = '\t'+'{"link": "'+link+'"},'+"\n"
    contents.insert(index, value)

    f = open(file, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def find_link(message):
    print("find link")
    words = message.split(" ")
    new_video = ""
    link = ""
    for i in words:#https://youtu.be/c9JNp6kdKqU
        print(i)
        try:
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
                    link = "https://www.youtube.com/watch?v="+txt
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
                    link = "https://www.youtube.com/watch?v=" + txt
            print(new_video)
        except BaseException:
            print("ok")
    return [new_video,link]

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
        print(str(self.id)+" "+str(self.marker)+" "+str(self.role)+" "+str(self.reputation))
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
                    self.role = "boy next door"
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
                    self.role = "dungeon master"
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
        elif self.marker == 4 and txt == "кто я такой?":
            if self.role == "fucking slave":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты "+str(self.role)+" твоя репутация "+str(self.reputation)+" до boy next door тебе " + str(100-self.reputation),
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
            elif self.role == "boy next door":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты "+str(self.role)+" твоя репутация "+str(self.reputation)+" до DUNGEON MASTER тебе " + str(300-self.reputation),
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
            if self.role == "dungeon master":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты "+str(self.role)+" твоя репутация "+str(self.reputation)+" ты, черт возьми, хорош",
                    random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
                )
        elif self.marker == 4 and txt == "gym":
            vk.messages.send(
                user_id=event.user_id,
                message="ты пришел в качалочку, закачай в меня больше тру гачи видосов, отправь ссылочку на настоящий гачи ремикс и смайлик на удачу ;-)",
                random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
            )
            self.marker = 41
        elif self.marker == 41 and txt == "выйти из качалочки":
            vk.messages.send(
                user_id=event.user_id,
                message="возвращайся, как захочешь",
                random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
            self.marker = 4
        elif self.marker == 41:
            check = find_link(raw_txt)
            check[0] = check[0].lower()
            if check[0] == "":
                vk.messages.send(
                    user_id=event.user_id,
                    message="это не ссылочка на музыку богов, ты обманул своего Мастера",
                    random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
                )
                self.reputation -= 50
                self.marker = 41
            elif "gachi" in check[0] or "гачи" in check or "right version" in check[0]:
                if new_link(check[1],"videos.json"):
                    vk.messages.send(
                        user_id=event.user_id,
                        message="неплохо, "+str(self.role),
                        random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
                    )
                    self.reputation+=40
                    self.marker = 41
                    add_link(check[1],"videos.json")
                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="ты хорош, но кто-то скинул эту ссылку раньше, поищи получше " + str(self.role),
                        random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
                    )
                    self.marker = 41
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="как-то не похоже на тру версию",
                    random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
                )
                self.role = 41
        elif self.marker == 42:
            vk.messages.send(
                user_id=event.user_id,
                message="кажется, ты что-то не дописал",
                random_id=get_random_id(), keyboard=open("key6.json", "r", encoding="UTF-8").read()
            )
            self.reputation -=50
            self.marker = 41

        elif self.id == 436111332 and txt == "save":
            user_to_json("users_backup.json")
            vk.messages.send(
                user_id=event.user_id,
                message="усе сох",
                random_id=get_random_id(), keyboard=open("key5.json", "r", encoding="UTF-8").read()
            )
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

with open('users_backup.json') as json_file:
    data = json.load(json_file)
    i = 0
    for p in data['users']:
        user_base.append(User(p['id']))
        user_base[i].role = p['role']
        user_base[i].marker = p['marker']
        user_base[i].reputation = p['reputation']
        i+=1

while True:
    for event in longpoll.listen():
        print(event.type)
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print(len(user_base))
            new = True
            for i in range(len(user_base)):
                if user_base[i].id == event.user_id:
                    new = False
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
