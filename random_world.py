import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
user_guess = ""

print ("guess a world between: python, java, javascript, ruby, html, css")
while True:
    user_guess=input("enter your guess (type quit to exit):")

    if user_guess=="quit":
        print("The world was" + selected_word + "Thanks for playing!")
        break
    elif user_guess == selected_word:
        print ("Congratulation you won!")
        break
    else:
        print ("Wrong, try again")
        