import time
import random

def run_quiz():
    # defining quiz questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Rome"],
            "answer": "B",
            "fun_fact": "Fun fact: The Eiffel Tower grows about 6 inches in summer due to thermal expansion!"
        },
        {
            "question": "How many hearts does an octopus have?",
            "options": ["A) 1", "B) 2", "C) 3", "D) 8"],
            "answer": "C",
            "fun_fact": "Octopuses have three hearts, nine brains, and blue blood. Talk about over-engineered!"
        },
        {
            "question": "What is the airspeed velocity of an unladen swallow?",
            "options": ["A) 20 mph", "B) 24 mph", "C) African or European?", "D) What do you mean? A swallow carrying a coconut?"],
            "answer": "C",
            "fun_fact": "This is a famous reference from Monty Python and the Holy Grail. The correct answer is about 24 mph for a European swallow."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "C",
            "fun_fact": "Mars is red due to iron oxide (rust) on its surface. Basically, it's a giant rusty rock!"
        },
        {
            "question": "If you're waiting for the waiter, aren't you the waiter?",
            "options": ["A) That's deep", "B) Mind blown", "C) I need to sit down", "D) All of the above"],
            "answer": "D",
            "fun_fact": "This philosophical dilemma has puzzled diners for centuries. The real question is: who gets the tip?"
        },
        {
            "question": "What is the largest mammal on Earth?",
            "options": ["A) African Elephant", "B) Blue Whale", "C) Your mom", "D) Giraffe"],
            "answer": "B",
            "fun_fact": "The blue whale's heart is so big, a human could swim through its arteries. Option C might be a close second though."
        },
        {
            "question": "Why did the chicken cross the road?",
            "options": ["A) To get to the other side", "B) It was fleeing KFC", "C) To prove it wasn't chicken", "D) To deliver this quiz question"],
            "answer": "A",
            "fun_fact": "This is actually the original and correct answer to the ancient joke. The others are just modern interpretations."
        }
    ]
    
    # to shuffle questions for variety
    random.shuffle(questions)
    score = 0
    
    print("Welcome to the Absolutely Serious (Mostly) Quiz Game!")
    print("You'll be asked a series of very important questions.")
    print("Some are serious, some are silly, all are fun!\n")
    time.sleep(2)
    
    for i, q in enumerate(questions[:5], 1):  # Use only 5 questions
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        if user_answer == q["answer"]:
            print("\n✅ Correct! Well done!")
            score += 1
        else:
            print(f"\n❌ Incorrect! The correct answer was {q['answer']}.")
        
        print(f"\n{q['fun_fact']}")
        time.sleep(3)
    
    # Calculate final score with humorous feedback
    percentage = (score / 5) * 100
    
    print("\n\nQuiz complete! Let's see how you did...")
    time.sleep(1)
    print(f"\nYour score: {score}/5 ({percentage}%)")
    
    if percentage == 100:
        print("Perfect score! Are you cheating or just brilliant?")
    elif percentage >= 80:
        print("Excellent! You're clearly both knowledgeable and fun at parties.")
    elif percentage >= 60:
        print("Good job! You know some stuff, and that's better than nothing.")
    elif percentage >= 40:
        print("Not bad! At least you're trying, and that's what counts.")
    else:
        print("Well... at least you had fun, right? Maybe try watching some educational comedy shows?")
    
    print("\nThanks for playing the Absolutely Serious (Mostly) Quiz Game!")

if __name__ == "__main__":
    run_quiz()