import json
def add_link(link, file):
    f = open(file, "r")
    contents = f.readlines()
    f.close()
    index = 2
    value = '{"link": "'+link+'"},'+"\n"
    contents.insert(index, value)

    f = open(file, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

user_base =[]

class User():
    id = ""
    marker = 0
    role = "noob"
    reputation = 0
    def __init__(self, id):
        self.id=id

with open('users_backup.json') as json_file:
    data = json.load(json_file)
    i = 0
    for p in data['users']:
        user_base.append(User(p['id']))
        user_base[i].role = p['role']
        user_base[i].marker = p['marker']
        user_base[i].reputation = p['reputation']
        i+=1

def user_to_json(file, user_base):
    fh = open(file,"w")
    fh.write('{'+'\n'+'"users": ['+'\n')
    i = 0
    for users in user_base:
        i+=1
        txt = {
            "id": str(users.id),
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

user_to_json("users_backup.json", user_base)