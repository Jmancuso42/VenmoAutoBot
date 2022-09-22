from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, get_day, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """


  

  #print(tfa)

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, e_friend_id, c_friend_id, m_friend_id, r_friend_id, mi_friend_id = actualVars
  #print(otp)
  access_token = Client.get_access_token(username='jmancuso142@gmail.com',
                                        password='#uclid3an')
  print(access_token)

  day = get_day(now)
  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "Een",
      "id": e_friend_id,
    },
    {
      "name": "CJ",
      "id": c_friend_id,
    },
    {
      "name": "Mike",
      "id": m_friend_id,
    },

    {
      "name": "Mitch",
      "id": mi_friend_id,
    },

    {
      "name": "Ryan",
      "id": r_friend_id,
    },

  ]

  successfulRequests = []
  expectedRequests = len(friends)
  
  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = f"It is {day} of {month}, which is riiight before youtube wants their blood money, so pay up by the 22nd <3" 
    amount = 3.60
    message = f"""Good news

I have successfully requested money from {name}.

— Lil Joe
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
