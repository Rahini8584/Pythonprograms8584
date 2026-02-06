import random

# 1. Define quiz questions
# Each question is a tuple: (question, [options], correct_answer_index)
questions = [
    ("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], 0),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 1),
    ("What is 5 + 7?", ["10", "11", "12", "13"], 2),
    ("Who wrote 'Hamlet'?", ["Mark Twain", "Charles Dickens", "William Shakespeare", "J.K. Rowling"], 2),
    ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 1)] 
# 2. Shuffle questions
random.shuffle(questions)
# 3. Quiz logic
score = 0
for i, q in enumerate(questions, start=1):
    question, options, correct_index = q
    print(f"\nQuestion {i}: {question}")
    for idx, option in enumerate(options, start=1):
        print(f"  {idx}. {option}")
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")
    if answer - 1 == correct_index:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {options[correct_index]}")
print(f"\nYour total score: {score}/{len(questions)}")