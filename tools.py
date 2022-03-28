from colorama import init, Fore
import datetime
init(autoreset=True)

def show_percentage(n:int, total:int, SHOW_STATUS_EACH = 50):
  if n % SHOW_STATUS_EACH == 0:
    print(Fore.CYAN + f"{round((n+1) / total * 100)} %")

  if n == total - 1:
    print(Fore.GREEN + "--100%")

  return None


def normalize(text, DELETE_CHARACTERS):

  for char in DELETE_CHARACTERS:
    text = text.replace(char, DELETE_CHARACTERS.get(char))
  return text


def normalize_date(date:str, strd:str = "%d/%m/%Y %I:%M %p"):

  date = date.replace("a. m.", "AM")
  date = date.replace("p. m.", "PM")
  date = date.replace(",", "")

  try:
    dateObj = datetime.datetime.strptime(date, strd)

  except Exception as e:
    print(f"Error -> {e}")
    dateObj = None

  return dateObj


colors = "b,g,r,c,m,y,k".split(",")