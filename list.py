#Homogeneus List

integers = [1, 2, 3, 8, 33]

animals = ["dog", "cat", "goat(messi)"]

names = ["Roger", "Sam", "Messi"]

floats = [2.2, 4.5, 9.8, 10.8]

#Heterogeneus List

numbers_animals_names = [2, "cat", 34.33, "Messi"]

list_lists = [[1, 2, 3], ["cat", "dog", "giraffe"]]

#How to access an element in a list

list = [3, 22, 30, 5.3, 20]

print(list[2])
print(list[0])
print(list[1])
print(list[4])
print(list[-1])

words = [
    "apple", "banana", "grape", "orange", "kiwi",
    "peach", "melon", "berry", "plum", "cherry",
    "mango", "papaya", "lemon", "lime", "coconut",
    "pineapple", "pomegranate", "apricot", "fig", "date",
    "avocado", "nectarine", "quince", "tangerine", "persimmon",
    "carrot", "broccoli", "spinach", "lettuce", "kale",
    "pepper", "cucumber", "zucchini", "eggplant", "radish",
    "potato", "tomato", "onion", "garlic", "beet",
    "turnip", "squash", "pumpkin", "sweetpotato", "asparagus",
    "celery", "brussels", "cauliflower", "artichoke", "parsnip",
    "chard", "fennel", "jicama", "rutabaga", "yams",
    "chicken", "beef", "pork", "fish", "shrimp",
    "tofu", "ham", "turkey", "lamb", "duck",
    "bacon", "salami", "venison", "crab", "lobster",
    "squid", "octopus", "clams", "mussels", "oysters",
    "cheese", "yogurt", "milk", "cream", "butter",
    "bread", "bagel", "croissant", "tortilla", "pasta",
    "rice", "quinoa", "barley", "couscous", "bulgur",
    "sugar", "salt", "pepper", "spice", "herb",
    "vinegar", "oil", "mustard", "ketchup", "mayo",
    "syrup", "honey", "jam", "salsa", "pesto",
    "soup", "stew", "curry", "sushi", "pizza",
    "burger", "taco", "wrap", "salad", "sandwich",
    "cookie", "cake", "pie", "brownie", "pudding",
    "icecream", "gelato", "sorbet", "donut", "muffin",
    "waffle", "pancake", "crepe", "cobbler", "strudel",
    "chocolate", "vanilla", "strawberry", "caramel", "mint",
    "almond", "cashew", "walnut", "peanut", "pistachio",
    "hazelnut", "sunflower", "pumpkinseed", "chia", "flaxseed",
    "safflower", "coconutwater", "soy", "almondmilk", "oatmilk",
    "matcha", "espresso", "latte", "cappuccino", "tea",
    "juice", "smoothie", "cocktail", "punch", "soda",
    "water", "sparkling", "lemonade", "icedtea", "coffee",
    "wine", "beer", "whiskey", "vodka", "rum",
    "gin", "brandy", "tequila", "champagne", "liqueur",
    "fruitcake", "cheesecake", "flan", "browniebites", "tart",
    "truffle", "candy", "caramelcorn", "popcorn", "marshmallow",
    "s'mores", "granola", "trailmix", "jerky", "snack",
    "breakfast", "brunch", "lunch", "dinner", "feast",
    "banquet", "buffet", "picnic", "barbecue", "cookout",
    "potluck", "reunion", "gathering", "celebration", "party",
    "event", "meeting", "conference", "symposium", "forum",
    "discussion", "workshop", "class", "lecture", "seminar"]

print(words[-74])

#List slicing

list = [1, 2, 3, 4, 5]

print(list[:])
print(list[1:3])
print(list[2:-1])

list = [3, 22, 30, 5.3, 20]

#update a list

science = ["art", "chemistry","math"]
science [0] = "Biology"
science [-1] = "Geology"
print(science)

integers = [2, 4, 9, 20, 27]
integers.remove(4)
print(integers)

integers.pop(3)
print(integers)

list_names = ["Joseph", "Alan", "Pablo", "Roger", "Moroni", "Levi", "Nico", "Abinadi", "Dan", "Angel"]
list_names.append("Benja")
print(list_names)

list_of_squares = []
for int in range (1, 10):
    square = int **2
    list_of_squares.append(square)

print(list_of_squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#[expression for int in list if condition]
squared2 = [item**2 for item in range(1, 10)]
print(squared2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in numbers:
    print(numbers**3)

cubic = [num**3 for num in numbers]
print(cubic)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = [num*2 for num in numbers if num%2 == 0]
print (doubled_numbers)
