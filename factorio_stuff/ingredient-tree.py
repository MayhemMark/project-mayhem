import json

class Collection(list):
	def __init__(self, initialIter):
		for x in list(initialIter):
			self.append(x)

	def __repr__(self):
		return f'COLLECTION [{",".join(map(lambda x: str(x), self))}]'

	def add (self, ob):
		if ob in self:
			 raise Exception('This item already exists')

		self.append(ob)

	def getByName (self, name):
		return next(x for x in self if x.name == name)

	def getAll (self):
		return self

	def filter(self, fn):
		return filter(fn, self.getAll())

itemsCollection = Collection([])
recipeCollection = Collection([])
techCollection = Collection([])

class Item:
	def __init__(self, itemJson):
		self.name = itemJson['name']
		self.localised_name = itemJson['localised_name']
		self.type = itemJson['type'] if 'type' in itemJson else 'fluid'
		self.fuel_value = itemJson['fuel_value']
	
	def __repr__(self):
		return f'<ITEM {self.type} {self.name}>'

	def getRecipesToCreate (self):
		return recipeCollection.filter(lambda recipe: self in recipe.getProductItems())

	def getRecipesToUse (self):
		return recipeCollection.filter(lambda recipe: self in recipe.getIngredientItems())

class Recipe:
	def __init__(self, recipeJson):
		self.name = recipeJson['name']
		self.category = recipeJson['category']
		self.ingredients = recipeJson['ingredients']
		self.products = recipeJson['products']
		self.energy = recipeJson['energy']
	
	def __repr__(self):
		return f'<RECIPE {self.name}>'

	def getIngredientItems (self):
		return map(lambda ing: itemsCollection.getByName(ing['name']), self.ingredients)

	def getProductItems (self):		
		return map(lambda ing: itemsCollection.getByName(ing['name']), self.products)

	def getTechToUse (self):
		return techCollection.filter(lambda tech: self in tech.getRecipeUnlocks())

class Technology:
	def __init__(self, technologyJson):
		self.name = technologyJson['name']
		self.localised_name = technologyJson['localised_name']
		self.effects = technologyJson['effects']
		self.prerequisites = technologyJson['prerequisites']
	
	def __repr__(self):
		return f'<TECHNOLOGY {self.name}>'

	def getRecipeUnlocks (self):
		unlocks = list(filter(lambda x: x['type'] == 'unlock-recipe', self.effects))
		unlocks = list(map(lambda x: x['recipe'], unlocks))
		return recipeCollection.filter(lambda recipe: recipe.name in unlocks)


itemsJson = json.loads(open("./recipe-lister/item.json", "r").read())
for itemName in itemsJson.keys():
	itemsCollection.add(Item(itemsJson[itemName]))

fluidsJson = json.loads(open("./recipe-lister/fluid.json", "r").read())
for itemName in fluidsJson.keys():
	itemsCollection.add(Item(fluidsJson[itemName]))

recipesJson = json.loads(open("./recipe-lister/recipe.json", "r").read())
for recipeName in recipesJson.keys():
	recipeCollection.add(Recipe(recipesJson[recipeName]))

technologyJson = json.loads(open("./recipe-lister/technology.json", "r").read())
for technologyName in technologyJson.keys():
	techCollection.add(Technology(technologyJson[technologyName]))

item = itemsCollection.getByName('iron-plate')

print(f'''
You selected item:
  Name: '{item.name}'
  Type: '{item.type}'
  Localized: {item.localised_name}
  Fuel value: {int(item.fuel_value)}
''')


print('Can be crafted with:')
for recipe in item.getRecipesToCreate():
	print(f'''
  Recipe: {recipe}
  Ingredients: {Collection(recipe.getIngredientItems())}
  Tech tree: {Collection(recipe.getTechToUse())}
  Produces: {Collection(recipe.getProductItems())}
''')


print('Can be used to craft:')
for recipe in item.getRecipesToUse():
	print(f'''
  Recipe: {recipe}
  Ingredients: {Collection(recipe.getIngredientItems())}
  Tech tree: {Collection(recipe.getTechToUse())}
  Produces: {Collection(recipe.getProductItems())}
''')

# print(f'''
# 	All recipes: {recipeCollection}
# 	Recipe: {recipe}
# 	Requires: {recipe.getIngredientItems()}
# 	Produces: {recipe.getProductItems()}
# ''')

# for item in recipe.getIngredientItems():
# 	print(f'''
# 		Recipes for {item.name}: {item.getRecipesToCreate()}
# 	''')



