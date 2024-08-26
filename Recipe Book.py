import random
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.grocery_list = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def search_recipe(self, query):
        return [recipe for recipe in self.recipes if query.lower() in recipe.name.lower()]

    def add_to_grocery_list(self, ingredients):
        for ingredient in ingredients:
            if ingredient not in self.grocery_list:
                self.grocery_list.append(ingredient)

    def remove_from_grocery_list(self, ingredient):
        if ingredient in self.grocery_list:
            self.grocery_list.remove(ingredient)

    def get_random_recipe(self):
        return random.choice(self.recipes)
recipe_book = RecipeBook()
recipe1 = Recipe("Spaghetti Carbonara",["spaghetti", "eggs", "bacon", "parmesan cheese", "garlic", "olive oil"],"1. Cook spaghetti until al dente. 2. Cook bacon in a large skillet until crispy. 3. In a bowl, whisk together eggs and parmesan cheese. 4. Add garlic to the bacon and cook for 1 minute. 5. Add spaghetti to the skillet and toss with bacon and garlic. 6. Pour the egg mixture over the spaghetti and toss until the eggs are cooked. Serve hot.")
recipe2 = Recipe("Chicken Parmesan",["chicken breast", "breadcrumbs", "parmesan cheese", "eggs", "marinara sauce", "mozzarella cheese"],"1. Preheat oven to 400°F. 2. Coat chicken breast in beaten eggs, then coat in breadcrumbs mixed with parmesan cheese. 3. Place chicken in a baking dish and bake for 20-25 minutes. 4. Spoon marinara sauce over chicken and top with mozzarella cheese. 5. Bake for an additional 10-15 minutes. Serve hot.")
recipe_book.add_recipe(recipe1)
recipe_book.add_recipe(recipe2)
query = "spaghetti"
search_results = recipe_book.search_recipe(query)
print("Search results for '{}':".format(query))
for recipe in search_results:
    print(recipe)
recipe = recipe_book.get_random_recipe()
print("Adding ingredients for '{}' to grocery list...".format(recipe))
recipe_book.add_to_grocery_list(recipe.ingredients)
print("Grocery list:", recipe_book.grocery_list)
ingredient = recipe.ingredients[0]
print("Removing '{}' from grocery list...".format(ingredient))
recipe_book.remove_from_grocery_list(ingredient)
print("Grocery list:", recipe_book.grocery_list)
