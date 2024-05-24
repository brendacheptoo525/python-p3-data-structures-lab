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
    return [food['name'] for food in spicy_foods]

# Example usage
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]
print(get_names(spicy_foods))  # Output: ["Green Curry", "Buffalo Wings", "Mapo Tofu"]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

# Example usage
print(get_spiciest_foods(spicy_foods))
# Output: [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_str = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_str}")

# Example usage
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

# Example usage
print(get_spicy_food_by_cuisine(spicy_foods, "American"))  # Output: {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))  # Output: {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# Example usage
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)

# Example usage
print(get_average_heat_level(spicy_foods))  # Output: 6

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# Example usage
new_spicy_food = {"name": "Jalapeno Poppers", "cuisine": "Mexican", "heat_level": 4}
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)
