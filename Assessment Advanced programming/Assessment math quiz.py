import random

def displayMenu():
    """Display the difficulty level menu"""
    print("\n" + "="*40)
    print("WELCOME TO THE MATHS QUIZ")
    print("="*40)
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    print("="*40)
    
    while True:
        choice = input("\nSelect difficulty (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice! Please enter 1, 2, or 3.")

def randomInt(difficulty):
    """Generate random numbers based on difficulty level"""
    if difficulty == 1:  # Easy: single digit (0-9)
        return random.randint(0, 9)
    elif difficulty == 2:  # Moderate: double digit (10-99)
        return random.randint(10, 99)
    else:  # Advanced: 4-digit (1000-9999)
        return random.randint(1000, 9999)

def decideOperation():
    """Randomly decide between addition or subtraction"""
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    """Display the problem and get user's answer"""
    print(f"\n{num1} {operation} {num2} = ", end="")
    try:
        answer = int(input())
        return answer
    except ValueError:
        return None

def isCorrect(user_answer, correct_answer, attempt):
    """Check if answer is correct and display appropriate message"""
    if user_answer == correct_answer:
        if attempt == 1:
            print("✓ Correct! Well done!")
            return True, 10
        else:
            print("✓ Correct on second attempt!")
            return True, 5
    else:
        if attempt == 1:
            print("✗ Incorrect. Try again!")
            return False, 0
        else:
            print(f"✗ Incorrect. The correct answer was {correct_answer}")
            return False, 0

def displayResults(score):
    """Display final score and grade"""
    print("\n" + "="*40)
    print("QUIZ RESULTS")
    print("="*40)
    print(f"Your final score: {score}/100")
    
    # Determine grade
    if score >= 90:
        grade = "A+"
        comment = "Outstanding!"
    elif score >= 80:
        grade = "A"
        comment = "Excellent work!"
    elif score >= 70:
        grade = "B"
        comment = "Well done!"
    elif score >= 60:
        grade = "C"
        comment = "Good effort!"
    elif score >= 50:
        grade = "D"
        comment = "Keep practicing!"
    else:
        grade = "F"
        comment = "Need more practice!"
    
    print(f"Grade: {grade}")
    print(f"Comment: {comment}")
    print("="*40)

def main():
    """Main function to run the quiz"""
    play_again = True
    
    while play_again:
        # Display menu and get difficulty
        difficulty = displayMenu()
        
        total_score = 0
        questions_answered = 0
        
        # Quiz loop - 10 questions
        while questions_answered < 10:
            # Generate random numbers and operation
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()
            
            # Calculate correct answer
            if operation == '+':
                correct_answer = num1 + num2
            else:
                correct_answer = num1 - num2
            
            print(f"\nQuestion {questions_answered + 1}/10")
            
            # First attempt
            user_answer = displayProblem(num1, num2, operation)
            
            if user_answer is None:
                print("Invalid input! Please enter a number.")
                continue
            
            is_correct, points = isCorrect(user_answer, correct_answer, 1)
            
            if is_correct:
                total_score += points
                questions_answered += 1
            else:
                # Second attempt
                print("Try one more time:")
                user_answer = displayProblem(num1, num2, operation)
                
                if user_answer is None:
                    print("Invalid input! Moving to next question.")
                    questions_answered += 1
                    continue
                
                is_correct, points = isCorrect(user_answer, correct_answer, 2)
                total_score += points
                questions_answered += 1
        
        # Display final results
        displayResults(total_score)
        
        # Ask if user wants to play again
        print("\nWould you like to play again?")
        response = input("Enter 'yes' to continue or any other key to quit: ").lower()
        play_again = response == 'yes' or response == 'y'
    
    print("\nThank you for playing! Goodbye!")

if __name__ == "__main__":
    main()