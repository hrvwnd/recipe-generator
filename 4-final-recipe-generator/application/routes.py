import requests
from application import app
from application.functions import add_or_delete_parts
import numpy as np
import json
@app.route("/",methods = ["GET", "POST"])
def final_recipe_parts():
    ingredients_service = requests.get("http://2-ingredient-generator:5002/")
    spare_ingredients_service = requests.get("http://2-ingredient-generator:5002/")
    method_service = requests.get("http://3-method-generator:5003/")
    post = add_or_delete_parts(ingredients_service, method_service, spare_ingredients_service)
    #post = np.asarray(post) # converts to array for json transfer
    json.dumps(post)
    return post