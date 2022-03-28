
from typing import Text
import settings
import json
import random

file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "r", encoding=settings.ENCODING) as jsonFile:
    values = json.loads(jsonFile.read())


class author_colors():
    def __init__(self):
        self.users = {}

    def get_color(self, user):
        if user in self.users:
            return self.users[user]
        else:
            return self.createUser(user)

    def createUser(self, user):
        colors = ["red", "green", "blue", "yellow", "cyan", "purple"]
        userColor = random.choice(colors)
        self.users[user] = userColor

        return userColor

class html():
    def __init__(Self):
        pass

    def tag_h1(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h1 class="{classList}" id="{idList}">{innerHtml}</h1>"""
        return tag

    def tag_h2(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h2 class="{classList}" id="{idList}">{innerHtml}</h2>"""
        return tag

    def tag_h3(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h3 class="{classList}" id="{idList}">{innerHtml}</h1>"""
        return tag

    def tag_h4(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h4 class="{classList}" id="{idList}">{innerHtml}</h4>"""
        return tag

    def tag_h5(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h5 class="{classList}" id="{idList}">{innerHtml}</h5>"""
        return tag

    def tag_h6(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<h6 class="{classList}" id="{idList}">{innerHtml}</h6>"""
        return tag

    def tag_div(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<div class="{classList}" id="{idList}">{innerHtml}</div>"""
        return tag

    def tag_span(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<span class="{classList}" id="{idList}">{innerHtml}</span>"""
        return tag

    def tag_a(Self, classList = "", idList = "", href="", innerHtml= ""):
        tag = f"""<a class="{classList}" id="{idList}" href="{href}">{innerHtml}</a>"""
        return tag

    def tag_button(Self, classList = "", idList = "", innerHtml= ""):
        tag = f"""<button class="{classList}" id="{idList}">{innerHtml}</button>"""
        return tag

    def personalized_tag(Self, tag:str):
        return tag


t = html()
colors = author_colors()

def write(messages, page = 1, numberPages= 1):
    messagesDivInnerHtml = ""
    for message in messages:

        author = t.tag_div(f"author {colors.get_color(message['author'])}", "", message["author"])
        date = t.tag_div("date", "", message["date"])
        content = t.tag_div("msgContent", "", message["msgContent"])
        fullMsg = t.tag_div("message", "", f"{author}\n{content}\n{date}")

        messagesDivInnerHtml += fullMsg

    messagesDiv = t.tag_div("box", "messagesContainer", messagesDivInnerHtml)


    indexSelector = t.personalized_tag(f"""
    <input type="number" id="indexSelector" value="{page}" min="1" max="{numberPages}">""")

    indexReturner = t.tag_button("btn", "indexReturnButton", "Select")

    link1 =t.tag_a("", "", "#start", "Go to head")
    link2 =t.tag_a("", "", "#end", "Go to end")
    links = t.tag_div("", "links", f"{link1}{link2}")
    optionBox = t.tag_div("box", "options", f"{indexSelector}{indexReturner} {links}")

    body = f"""
    {t.tag_h1("title", "", f"Page {page} / {numberPages}")}
    {messagesDiv}
    {optionBox}
    """

    htmlFileValue = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../index.css">
        <title>Chat</title>
    </head>
    <body>
        <div class="d-none" id="start"></div>
        {body}
        <div class="d-none" id="end"></div>
        <script src="../index.js"></script>
    </body>
    </html>
    """

    file = f"{settings.HTML_CHATS_DIR}{settings.CHAT_NAME}"
    with open(f"{file}-{page}.html", "w", encoding="utf-8") as html:
        html.write(htmlFileValue)


pages =  len(values["messages"]) / settings.NEW_PAGE_EACH
if pages > round(pages):
    pages += 0.5

pages = round(pages)

for page in range(pages):
    messages = values.get("messages")[
        page * settings.NEW_PAGE_EACH : (page + 1) * settings.NEW_PAGE_EACH
        ]
    print(messages)
    print("\n\n")

    write(messages, page + 1, pages)