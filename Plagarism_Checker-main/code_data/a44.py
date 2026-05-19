def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {answer}")
    return score

def main():
    questions = {
        "What is the capital of France? ": "Paris",
        "What is 2 + 2? ": "4",
        "What is the largest ocean on Earth? ": "Pacific",
        "What year did the Titanic sink? ": "1912"
    }
    
    print("Welcome to the Quiz!")
    score = run_quiz(questions)
    print(f"You scored {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
