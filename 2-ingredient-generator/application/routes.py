from application import app 
from application.functions import random_list_item, random_number_generator, \
    vegetarian, list_of_ingredients
from json import dumps

@app.route('/', methods=["GET", "POST"])
def generate_recipe_ingredients():
    post = list_of_ingredients()
    post = dumps(post)
    #post = post.text
    return post

#print (generate_recipe_ingredients())
#print (dumps(generate_recipe_ingredients()))