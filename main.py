import requests
from datetime import datetime
import os

APP_ID = os.environ["WT_APP_ID"]
API_KEY = os.environ["WT_API_KEY"]

GENDER = "male"
AGE = 34
WEIGHT_KG = 73
HEIGHT_CM = 180

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["WT_SHEET_ENDPOINT"]
input_text = input("Tell me which exercises you did: ")

params = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=header)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['WT_TOKEN']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
