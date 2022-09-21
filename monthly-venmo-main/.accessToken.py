from venmo_api import Client
import venmo_api
import os
from dotenv import load_dotenv
from utils import get_env, env_vars, get_month, Venmo, Telegram


load_dotenv()
#os.getenv(key=venmo_api.)
at = get_env("JTOKEN")
print(at)
#print("My Token:", access_token)

venmo = Venmo(at)
#cjtoken = venmo_api.get_user_id(user="CJZesty")
cjToken = venmo.get_user_id_by_username("CJZesty")
print("Cj token:", cjToken)

e_token = venmo.get_user_id_by_username("Imgrana1")
print("Een token:", e_token)

m_token= venmo.get_user_id_by_username("Mitchell-Schaffer-2")
print("mitch token:", m_token)

mi_token = venmo.get_user_id_by_username("Michael-Ciccarone-1")
print("mikelToken:", mi_token)

r_token = venmo.get_user_id_by_username("Ryan-Lehmann-6")
print("ryan token",r_token)
