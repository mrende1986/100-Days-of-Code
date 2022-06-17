import requests

APP_ID = "b3241a9c"
API_KEY = "89a788b1a8393fab98fb362c642838b5"

GENDER = 'Male'
WEIGHT_KG = "77"
HEIGHT_CM = "155"
AGE = "35"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post('https://trackapi.nutritionix.com/v2/natural/exercise',json=parameters, headers=headers)
result = response.json()
print(result)

# ------------------------------Sheetly -------------------------------------- #

from datetime import datetime

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheetlyurl = 'https://api.sheety.co/e5a384cfe0fceb8a85b34f908a1fe55b/workoutTracking/workouts'

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheetly_response = requests.post(sheetlyurl, json=sheet_inputs)

    print(sheetly_response.text)