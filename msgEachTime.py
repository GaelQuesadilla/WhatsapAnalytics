import json
import matplotlib.pyplot as plt
import datetime
import tools
import settings

file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "r", encoding=settings.ENCODING) as jsonFile:
  values = json.loads(jsonFile.read())

data={
  "dates":{
    "00":0,
    "01":0,
    "02":0,
    "03":0,
    "04":0,
    "05":0,
    "06":0,
    "07":0,
    "08":0,
    "09":0,
    "10":0,
    "11":0,
    "12":0,
    "13":0,
    "14":0,
    "15":0,
    "16":0,
    "17":0,
    "18":0,
    "19":0,
    "20":0,
    "21":0,
    "22":0,
    "23":0,
  },
}


for message in values["messages"]:

  date = tools.normalize_date(message["date"]) 

  time = str(date.strftime("%H"))

  if time not in data["dates"]:
    data["dates"][time] = 0

  data["dates"][time] += 1

print(data)


fig, ax = plt.subplots()
ax.plot(list(data["dates"].keys()), list(data["dates"].values()))
ax.set_xlabel("time")
ax.set_ylabel("messages")
plt.show()



