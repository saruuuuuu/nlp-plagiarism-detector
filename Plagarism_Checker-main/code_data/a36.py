def ask_question(question, options, answer):
    print(question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    user_answer = input("Your answer (1/2/3/4): ")
    
    if options[int(user_answer) - 1] == answer:
        return True
    return False

def main():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
            "answer": "Harper Lee"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        }
    ]

    print("Welcome to the Quiz!")
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your total score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
