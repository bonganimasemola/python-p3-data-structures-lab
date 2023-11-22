spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    
    for spicy_food in spicy_foods:
        names.append(spicy_food["name"])
        
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    
    for spicy_food in spicy_foods:
        
        if spicy_food['heat_level'] > 5:
            spiciest_foods.append(spicy_food)
            
    return spiciest_foods
   

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food['name']
        cuisine = spicy_food['cuisine']
        heat_level = spicy_food['heat_level']
        
        heat_emojis = "🌶" * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for spicy_food in spicy_foods:
        
        if spicy_food['cuisine'] == cuisine:
            return spicy_food
        
    return None
    
    
def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food['heat_level'] > 5:
            name = spicy_food['name']
            cuisine = spicy_food['cuisine']
            heat_level = spicy_food['heat_level']
            heat_emojis = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)
    
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food['heat_level']
        
    if num_spicy_foods == 0:
        return 0
    else:
        return total_heat_level // num_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
