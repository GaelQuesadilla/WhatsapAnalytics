import settings
import json

file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "r", encoding=settings.ENCODING) as jsonFile:
    values = json.loads(jsonFile.read())


data = {
    "users": {},
    "total_messages": 0 
}

users = {"users":{}}

for message in values["messages"]:
    author = message["author"]

    if author in data["users"]:
        data["users"][author]["total_messages"] += 1
    else:
        data["users"][author] = {"total_messages": 1}

    data["total_messages"] += 1



file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}stadistics"
with open(f"{file}.json", "w", encoding=settings.ENCODING) as jsonFile:
    users = json.dumps(data, indent=4)
    jsonFile.write(users)