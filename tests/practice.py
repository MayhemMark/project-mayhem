import json

item_dict = json.loads(open("./factorio_stuff/recipe-lister/item.json", "r").read())
recipe_dict = json.loads(open("./factorio_stuff/recipe-lister/recipe.json", "r").read())

item_keys = list(item_dict.keys())
recipe_keys = list(recipe_dict.keys())

#print(item_dict["compilatron-chest"])
#print(recipe_dict["sulfuric-acid"])

def iterate_itemkeys(item_keys):
    for i in item_keys:
        return i

print("item_dict= " + str(type(item_dict)))
print("recipe_dict= " + str(type(recipe_dict)))
print("item_keys= " + str(type(item_keys)))
print("recipe_keys= " + str(type(recipe_keys)))

print(item_dict.get(iterate_itemkeys(item_keys)))



