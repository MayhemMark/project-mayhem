import json
from functools import reduce

def flatten2DList (arrayWithArrays):
	return reduce(lambda x,y : x + y, arrayWithArrays, [])

items = json.loads(open("./recipe-lister/item.json", "r").read())
recipes = json.loads(open("./recipe-lister/recipe.json", "r").read())
technology = json.loads(open("./recipe-lister/technology.json", "r").read())

# smartphone
#    (dit OF dat) EN true
#    OF
#   	plastic EN nogwat
def doTheActualThing (recipeName):
	# 1. zoek de technology waar recipeName als effect "unlock-recipe" voorkomt
	discoveredTechs = list(filter(
		# Keep all techs that have TRUE that at least one effect is 'unlock-recipe' for recipeName:
		lambda tech: any(map(
			lambda effect: effect['type'] == 'unlock-recipe' and effect['recipe'] == recipeName,
			tech['effects']
		)),
		# An iterable of all techs
		map(lambda techName: technology[techName], technology.keys())
	))

	def wasTechDiscovered (techName):
		requiredTechNames = list(map(lambda t: t['name'], discoveredTechs))
		try:
			requiredTechNames.index(techName)
			return False
		except:
			return True

	# 2. voor elke technologie, zoek de prerequisites op
	def discoverPrerequisiteTechs (inputTechs):
		techsRequiredForNewTechs = flatten2DList(
			map(lambda tech: [] if type(tech['prerequisites']) == dict else tech['prerequisites'], inputTechs)
		)
		if type(techsRequiredForNewTechs) == dict:
			techsRequiredForNewTechs = []

		# Keep only techs that were NOT already discovered
		techsRequiredForNewTechs = list(filter(
			wasTechDiscovered,
			techsRequiredForNewTechs
		))

		if(len(techsRequiredForNewTechs) == 0):
			return

		techsRequiredForNewTechs = list(map(lambda tN: technology[tN], techsRequiredForNewTechs))

		# Remember that we have now found these fuckers
		discoveredTechs.extend(techsRequiredForNewTechs)

		# For everything that is new, see if there is even more stuff to find
		discoverPrerequisiteTechs(techsRequiredForNewTechs)
		
	discoverPrerequisiteTechs(discoveredTechs)

	return discoveredTechs

# TESTS:

# test('basic-transport-belt', [
# 	'basic-logistics'
# ])
# test('transport-belt', [
# 	'logistics',
# 	'basic-logistics',
# 	'logistics-0'
# ])
# test('express-transport-belt', [
# 	'basic-logistics',
# 	'logistics-0'
# 	'logistics'
# ])
# test('artillery-wagon', [
# 	'basic-logistics',
# 	'logistics-0'
# 	'logistics'
# ])

# Technologies --verwijzen naar--> Recipes 
def itemForSearchValue(value):
	return items[choice]

# returns TRUE if "item" can be made using "recipe"
def recipeProducesItem (recipe, item):
	productsInRecipeThatAreTheItem = filter(lambda product: product['name'] == item['name'], recipe['products'])
	return len(list(productsInRecipeThatAreTheItem)) > 0


choice = input("type an item name:")
item = itemForSearchValue(choice)
print(f'''
You selected item:
  Name: '{item['name']}'
  Type: '{item['type']}'
  Order: '{item['order']}'
  Localized: {item['localised_name']}
  Fuel value: {int(item['fuel_value'])}''')

if (item['fuel_value']) != 0:
	print(f'''  Fuel category: {item["fuel_category"]}
  Fuel acceleration: {item["fuel_acceleration_multiplier"]}
  Fuel top speed: {item["fuel_top_speed_multiplier"]}
''')

itemRecipes = list(map(lambda rN: recipes[rN],recipes.keys()))
itemRecipes2 = list(filter(lambda r: recipeProducesItem(r, item), itemRecipes))
print(f'{str(len(itemRecipes2))} out of {str(len(itemRecipes))} recipes can be used to make {item["name"]}')

print('Testing every recipe')
for recipe in itemRecipes2:
	recipeInfo = doTheActualThing(recipe['name'])
	print(f'''
  Recipe: {recipe['name']}
  Tech tree: {', '.join(set(map(lambda i: i['name'], recipeInfo)))}
''')