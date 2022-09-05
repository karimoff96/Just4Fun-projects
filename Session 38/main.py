import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

APP_KEY = os.getenv("NT_APP_KEY")
APP_ID = os.getenv('NT_APP_ID')
GENDER = os.getenv('GENDER')
WEIGHT_KG = os.getenv('WEIGHT_KG')
HEIGHT_CM = os.getenv('HEIGHT_CM')
AGE = os.getenv('AGE')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv('sheet_endpoint')

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime('%X')

for exercises in response.json()['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercises["name"].title(),
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"]
        }
    }
    post = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=('username', 'password'))
    print(post.text)
