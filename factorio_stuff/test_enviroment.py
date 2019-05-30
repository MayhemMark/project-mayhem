import json
from functools import reduce

def flatten2DList (arrayWithArrays):
	return reduce(lambda x,y : x + y, arrayWithArrays)

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
def test(input, expectedOutput) :
	actualOutput = doTheActualThing(input)
	actualOutput = set(map(lambda i: i['name'], actualOutput))

	expectedOutputString = ', '.join(expectedOutput)
	actualOutputString = ', '.join(actualOutput)
	print()
	if (actualOutputString != expectedOutputString):
		print('  ✗\t' + input + '\n\t' + actualOutputString)
		print()
	else: 
		print('  ✓\t' + input + '\n\t' + actualOutputString)

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

def recipeProducesItem (recipe, item):
	if type(recipe['products']) ==  0:
		print('Found a recipe without products')
		print(recipe)
        
	productsInRecipeThatAreTheItem = filter(lambda product: product['name'] == item['name'], recipe['products'])
	itemCanBeMadeWithRecipe = len(list(productsInRecipeThatAreTheItem)) > 0
	# print(f'Comparing {recipe["name"]} with {item["name"]}: {itemCanBeMadeWithRecipe}')
	# wtf?:
	return itemCanBeMadeWithRecipe


choice = input("type an item name:")
item = itemForSearchValue(choice)
itemRecipes = list(map(lambda rN: recipes[rN],recipes.keys()))
print('  Recipes in total: ' + str(len(itemRecipes)))
itemRecipes2 = list(filter(lambda r: recipeProducesItem(r, item), itemRecipes))
print('  Recipes after filter: ' + str(len(itemRecipes2)))

print('The result is:')
print(list(itemRecipes2))
