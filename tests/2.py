import json
from functools import reduce

# Is a list:
items = json.loads(open('../minecraft_data/items.json', 'r').read())

# Is a dict:
recipes = json.loads(open('../minecraft_data/recipes.json', 'r').read())

def getRecipesToMakeItem (id):
    str_int = str(id)
    if str_int in recipes.keys():
        return recipes[str_int]
    else:
        return ()

def flatten2DList (arrayWithArrays):
    return reduce(lambda x,y : x + y, arrayWithArrays)

# recipe ==> '2xCoal, 1xStick'
def getRecipeString (recipe):
    # Build a flat list of all ingredient identifiers
    flatList = ()
    if 'ingredients' in recipe.keys():
        flatList = recipe['ingredients']
    if 'inShape' in recipe.keys():
        flatList = flatten2DList(recipe['inShape'])
    if not(len(flatList)):
        return '(Unknown recipe)'    
    flatList = filter(lambda id: id != None, flatList)

    # Build a dictionary of total amount per item required for this recipe
    ingredientsDict = {}
    for id in flatList:
        strid = str(id)
        if (strid in ingredientsDict.keys()):
            ingredientsDict[strid] += 1
        else:
            ingredientsDict[strid] = 1

    # For every unique item, print a string of how much + name, and then join them with commas
    def getSingleTextForIngredient (id):
        item = items[int(id)]
        return f'{ingredientsDict[id]}×{item["displayName"]}'   
    return ', '.join(map(getSingleTextForIngredient, ingredientsDict.keys()))

def printItem (id):
    item = items[id]

    if not (item):
        print(f'Item {id} does not exist')
        return

    print(f"{item['displayName']} ({item['id']}, {item['name']})")

    for recipe in getRecipesToMakeItem(id):
        print(f" - {getRecipeString(recipe)}")


results = filter(lambda item : len(getRecipesToMakeItem(item['id'])) > 0, items)

for item in results:
    printItem(item['id'])