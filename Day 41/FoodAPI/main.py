import requests

def getRecipeByIngredients(ingredients):
    payload = {
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': False,
        'number': 5,
        'ranking': 1
    }

    api_key = "178dff743c0c4782aa31e3d500c3cd77"

    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"
    endpoint2 = "https://api.spoonacular.com/recipes/findByIngredients"

    headers={
        "X-Mashape-Key": api_key,
        "X-Mashape-Host": "mashape host"
    }

    r = requests.get(endpoint2, params=payload, headers=headers)
    results = r.json()
    title = results[0]['title']
    print(title)

getRecipeByIngredients('apple')