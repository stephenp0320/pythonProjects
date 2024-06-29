import random


breakfast = [
    "Scrambled Eggs",
    "Oatmeal",
    "Cereal",
    "Pancakes",
    "Yogurt",
    "Granola",
]

drinks = [
    "Water",
    "Coffee",
    "Tea",
    "Orange Juice",
    "Green Juice",
    "Smoothie",
]

lunch = [
    "Sandwich", 
    "Salad",
    "Soup",
    "Quinoa Bowl",
    "Burrito",
    "Buddha Bowl",
]

dinner = [
    "Chicken",
    "Steak",
    "Pasta",
    "Pizza",
    "Tacos",
    "Burgers",
]

snacks = [
    "Fruit",
    "Veggies",
    "Chips",
    "Cookies",
    "Nuts",
    "Cheese",
]

def create_meal_plan():
    for day in range(7):
        print(f"Day {day + 1}")
        print("Breakfast: ", random.choice(breakfast), "&", random.choice(drinks))
        print("Lunch: ", random.choice(lunch), "&", random.choice(drinks))
        print("Dinner: ", random.choice(dinner), "&", random.choice(drinks))
        print("Snack: ", random.choice(snacks), "&", random.choice(drinks))
        print()

def restart():
    while True:
        answer = input("Would you like to create another meal plan? (yes/no) ")
        if answer == "yes":
            create_meal_plan()
        else:
            break
    
def rate_meal():
    print("rate the meal from 1 to 5")
    rating = input("enter rating: ")
    if int(rating) > 3:
        print("Great to hear you enjoyed the meal!")
    else:
        print("We are sorry to hear that, you can try again!")
        restart()

def main():
    create_meal_plan()
    rate_meal()
   


if __name__ == "__main__":
    main()