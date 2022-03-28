import json
from matplotlib import markers
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
import tools
import settings

file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "r", encoding=settings.ENCODING) as jsonFile:
  values = json.loads(jsonFile.read())

users = []
data = {
  "simplyfied":{}
}
data2 = {
  "simplyfied":{}
}

for message in values["messages"]:
  author = message["author"]

  if author not in users:
    users.append(author)
    data[author] = {}
    data2[author] = {}

#CREATE ALL DATES
d = tools.normalize_date(values["messages"][0]["date"])
if settings.END_TODAY:
  end = datetime.datetime.now()
else:
  end = tools.normalize_date(values["messages"][-1]["date"]) 

while d <= end:
  date = datetime.datetime.strftime(d,'%d/%m/%Y')
  for user in list(data.keys()):
    data[user][date]= 0
  d += datetime.timedelta(days=1)

print(data.keys())

# COUNT MESSAGES EACH DAY
for message in values["messages"]:

  date = tools.normalize_date(message["date"]) 

  time = str(date.strftime("%d/%m/%Y"))

  author = message["author"]

  if time not in data["simplyfied"]:
    data["simplyfied"][time] = 0

  if time not in data[author]:
    data[author][time] = 0

  data[author][time] += 1
  data["simplyfied"][time] += 1


# Count messages each {RESOLUTION}

for user in list(data.keys()):
  for i in range(len(list(data[user].keys()))):
    # date = list(data["simplyfied"].keys())[i]
    # value = list(data["simplyfied"].values())[i]

    sum = 0
    nullValues = 0
    if i % settings.RESOLUTION == 0:
      for j in range(settings.RESOLUTION):
        try:
          date = list(data[user].keys())[i+j]
          sum += list(data[user].values())[i+j]
        except:
          nullValues += 1
      date = list(data[user].keys())[i]
      prom = sum/(settings.RESOLUTION-nullValues)
      data2[user][str(date)] = prom


fig, ax = plt.subplots()
totalColor = "#30303030"
handles =  [mpatches.Patch(label='Total')]

ax.plot_date(
  [tools.normalize_date(date, strd="%d/%m/%Y") for date in list(data["simplyfied"].keys())], 
  list(data["simplyfied"].values()), 
  color=totalColor, 
  label="Total", 
  marker="", 
  linestyle="-")



for _ in range(len(list(data.keys()))):
  user = list(data.keys())[_]

  if user is None:
    continue

  handles.append(mpatches.Patch(label=user, color=tools.colors[_]))
  ax.plot_date(
    [tools.normalize_date(date, strd="%d/%m/%Y") for date in list(data2[user].keys())], 
    list(data2[user].values()),
    label=user,
    marker="", 
    linestyle="-",
    color=tools.colors[_]
  )

ax.legend(handles=handles)
ax.set_xlabel("time")
ax.set_ylabel("messages")

fig.autofmt_xdate()
plt.show()



