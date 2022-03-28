messages = {"messages": []}

import json
import settings
import tools


def is_new_message(text:str):  # sourcery skip: invert-any-all, use-any
    loops = 6
    numbers = 4
    slachs = loops - numbers
    text = text[0:loops]

    if len(text) != loops:
        return False

    if text.count("/") != slachs:
        return False

    characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/"]
    for letter in text:
        if letter not in characters:
            return False

    return True 


file = f"{settings.UNINTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.txt", "r", encoding=settings.ENCODING) as chat:
    chatIndex = len(chat.readlines())


file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "w", encoding=settings.ENCODING) as chat:
    chat.write("{\"messages\":[]}")



file = f"{settings.UNINTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
chat = open(f"{file}.txt", "r", encoding=settings.ENCODING)

for _ in range(chatIndex):

    txtmsg = tools.normalize(chat.readline(), settings.DELETE_CHARACTERS)

    if not is_new_message(txtmsg):
        lastMessage = messages["messages"][-1]
        lastMessage["msgContent"] += txtmsg
        continue


    # DATE 
    dateIndex = txtmsg.find("-")
    if dateIndex > -1:
        date = txtmsg[0:dateIndex-1]
    if dateIndex == -1:
        date = None
        dateIndex = 0

    # AUTHOR 
    authorIndex = txtmsg[dateIndex:len(txtmsg)].find(":")

    if authorIndex > -1:
        authorIndex += dateIndex
        author = txtmsg[dateIndex+2:authorIndex]
    elif authorIndex == -1:
        author = None
        authorIndex = dateIndex

    # CONTENT 
    msgContent = txtmsg[authorIndex+2:len(txtmsg)]

    # SAVE
    messages.get("messages").append({
        "date": date, 
        "author": author,
        "msgContent": msgContent
        })
    
    tools.show_percentage(_, chatIndex, settings.SHOW_STATUS_EACH)



messages = json.dumps(messages)
file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
interpretedChat = open(f"{file}.json", "w", encoding=settings.ENCODING)
interpretedChat.write(messages)

