
from flask import Flask, request
import requests


def send_message(chat_id, text):
    method = "sendMessage"
    token = ('1950227107:AAEjQ5jpG4rASpwjXjnx71P7TqMTPPpZ3TU')
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["POST"])
def receive_update():
    chat_id = request.json["message"]["chat"]["id"]
    send_message(chat_id, "Hello!")
    return "ok"
