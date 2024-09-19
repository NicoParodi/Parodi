import random
def result(text):
    print(f"**********{text}**********")

def messi():
    options =["1", "2", "3"]
    cpu_ch = ["1", "2", "3"]
    
    while True:
        result("Choose rock(1), paper(2), scissors(3): ")
        user_ch = input()
        cpu_ch = random.choice(cpu_ch)
        print(cpu_ch)

        if user_ch not in options:
            result("not allowed, please enter a valid option")
            continue

        if user_ch == "quit":
            result("goodbye")
            break
        if user_ch == cpu_ch:
           result("its a tie, try again")

        elif((user_ch == "1") and (cpu_ch == "3")) or ((user_ch == "3") and (cpu_ch == "2")) or ((user_ch == "2") and (cpu_ch == "1")):
            result("you win")
        else:
            result("you lose")
messi()