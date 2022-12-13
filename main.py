import requests

APP_ID = "d5dea061"
API_KEY = "7f7127f4e3df0448207a618a1c763da1"
GENDER = "male"
AGE = 34
WEIGHT_KG = 73
HEIGHT_CM = 180

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

input_text = input("Tell me which exercises you did: ")

params = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=params, headers=header)
data = response.json()
print("data")
