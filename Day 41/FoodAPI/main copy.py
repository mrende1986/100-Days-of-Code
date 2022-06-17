import requests


api_key = "178dff743c0c4782aa31e3d500c3cd77"


endpoint2 = f"https://api.spoonacular.com/mealplanner/{api_key}/week/2020-06-01"

r = requests.get(endpoint2)
print(r)
#results = r.json()
# title = results[0]['title']
# print(title)