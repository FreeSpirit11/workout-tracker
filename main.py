import requests
from datetime import datetime
import os


APP_ID="YOUR_APP_ID"
API_KEY="YOUR_API_KEY"
TOKEN=os.environ["YOUR_TOKEN_HERE"]
SHEET_ENDPOINT='ENTER_SHEET_ENDPOINT_HERE'
EXERCISE_ENDPOINT="ENTER_EXERCISE_ENDPOINT_HERE"

GENDER="YOUR_GENDER"
WEIGHT_KG=YOUR_WEIGHT
HEIGHT_CM=YOUR_HEIGHT
AGE=YOUR_AGE

now = datetime.now()
date_today=now.date().strftime("%d/%m/%Y")
time_now=now.time().strftime("%X")

exercise_text=input("Tell me which exercise u did: ")
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
person_info={
 "query":exercise_text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE,
}
response=requests.post(EXERCISE_ENDPOINT, headers=headers, json=person_info)
response.raise_for_status()
json_response=response.json()
exercises=json_response["exercises"]

for exercise in exercises:

    sheet_inputs={
        "workout":{
            "date":date_today,
            "time":time_now,
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories'],
            "exercise":exercise["user_input"].title(),
        }
    }
    sheety_headers = {
        "Authorization": f"Basic {os.environ['TOKEN']}"
    }
    sheety_response=requests.post(SHEET_ENDPOINT,
                                  json=sheet_inputs,
                                  headers=sheety_headers
                                  )
    sheety_response.raise_for_status()
    print(sheety_response.text)

