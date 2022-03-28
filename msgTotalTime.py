import json
from matplotlib import markers
import matplotlib.pyplot as plt
import datetime
import tools
import settings

file = f"{settings.INTERPRETED_CHATS_DIR}{settings.CHAT_NAME}"
with open(f"{file}.json", "r", encoding=settings.ENCODING) as jsonFile:
  values = json.loads(jsonFile.read())

data ={
  "dates":{}
}

#CREATE ALL DATES
d = tools.normalize_date(values["messages"][0]["date"]) 
if settings.END_TODAY:
  end = datetime.datetime.now()
else:
  end = tools.normalize_date(values["messages"][-1]["date"]) 

while d <= end:
    data["dates"][datetime.datetime.strftime(d,'%d/%m/%Y')] = 0 
    d += datetime.timedelta(days=1)

print(data["dates"])

# COUNT MESSAGES EACH DAY
for message in values["messages"]:

  date = tools.normalize_date(message["date"]) 

  time = str(date.strftime("%d/%m/%Y"))

  if time not in data["dates"]:
    data["dates"][time] = 0

  data["dates"][time] += 1


# Count messages each {RESOLUTION}
dataDate2 = []
dataMsg2 = []
data2 = {
  "dates":{}
}

for i in range(len(list(data["dates"].keys()))):
  # date = list(data["dates"].keys())[i]
  # value = list(data["dates"].values())[i]

  sum = 0
  nullValues = 0
  if i % settings.RESOLUTION == 0:
    for j in range(settings.RESOLUTION):
      try:
        date = list(data["dates"].keys())[i+j]
        sum += list(data["dates"].values())[i+j]
      except:
        nullValues += 1
    date = list(data["dates"].keys())[i]
    prom = sum/(settings.RESOLUTION-nullValues)
    data2["dates"][str(date)] = prom


fig, ax = plt.subplots()
ax.plot_date(
  [tools.normalize_date(date, strd="%d/%m/%Y") for date in list(data["dates"].keys())], 
  list(data["dates"].values()), 
  color="#70707060", 
  label="total", 
  marker="", 
  linestyle="-")

ax.plot_date(
  [tools.normalize_date(date, strd="%d/%m/%Y") for date in list(data2["dates"].keys())], 
  list(data2["dates"].values()),  
  color="#6930a0ff", 
  label="simple",
  marker="", 
  linestyle="-"
  )
ax.set_xlabel("time")
ax.set_ylabel("messages")

fig.autofmt_xdate()
plt.show()



