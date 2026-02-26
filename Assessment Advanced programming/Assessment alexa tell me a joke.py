import random

def loadJokes(filename):
    """Load jokes from the text file"""
    try:
        with open(filename, 'r') as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if joke.strip()]
    except FileNotFoundError:
        print(f"File {filename} not found. Creating sample file...")
        createSampleJokes(filename)
        return loadJokes(filename)

def createSampleJokes(filename):
    """Create a sample jokes file"""
    sample_jokes = [
        "Why don't programmers like nature?It has too many bugs.",
        "Why did the developer go broke?Because he used up all his cache.",
        "What's a pirate's favorite programming language?You'd think it's R, but it's actually the C.",
        "Why do Java developers wear glasses?Because they don't C#.",
        "How many programmers does it take to change a light bulb?None, that's a hardware problem.",
        "Why did the smartphone go to therapy?It lost its contacts and couldn't find itself.",
        "What do you call a computer that sings?A Dell.",
        "Why was the JavaScript developer sad?Because he didn't Node how to Express himself.",
        "What's the object-oriented way to become wealthy?Inheritance.",
        "Why do programmers prefer dark mode?Because light attracts bugs.",
        "How do you comfort a JavaScript bug?You console it.",
        "Why did the function break up with the variable?She had constant arguments.",
        "What did the router say to the doctor?It hurts when IP.",
        "Why don't backers ever win at poker?They always get dealt a stack overflow.",
        "What's a programmer's favorite hangout place?Foo Bar.",
        "Why did the computer keep freezing?It left its Windows open.",
        "What do you call 8 hobbits?A hobbyte.",
        "Why was the cell phone wearing glasses?It lost its contacts.",
        "How does a computer get drunk?It takes screenshots.",
        "Why did the PowerPoint presentation cross the road?To get to the other slide."
    ]
    with open(filename, 'w') as file:
        for joke in sample_jokes:
            file.write(joke + '\n')
    print(f"Created {filename} with sample jokes!")

def parseJoke(joke_line):
    """Parse joke into setup and punchline"""
    if '?' in joke_line:
        parts = joke_line.split('?', 1)
        setup = parts[0] + '?'
        punchline = parts[1].strip()
        return setup, punchline
    return joke_line, ""

def tellJoke(jokes):
    """Select and tell a random joke"""
    if not jokes:
        print("No jokes available!")
        return
    
    joke = random.choice(jokes)
    setup, punchline = parseJoke(joke)
    
    print(f"\n{setup}")
    
    if punchline:
        input("Press Enter to see the punchline... ")
        print(f"{punchline}\n")
    else:
        print()

def main():
    """Main function to run the joke program"""
    print("="*50)
    print("ALEXA JOKE TELLER")
    print("="*50)
    
    # Load jokes from file
    jokes = loadJokes('randomJokes.txt')
    
    print(f"\nLoaded {len(jokes)} jokes!")
    print("Say 'Alexa tell me a joke' to hear a joke")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if 'quit' in user_input or 'exit' in user_input:
            print("\nGoodbye! Thanks for the laughs!")
            break
        elif 'alexa' in user_input and 'joke' in user_input:
            tellJoke(jokes)
        elif user_input:
            print("Say 'Alexa tell me a joke' to hear a joke!")

if __name__ == "__main__":
    main()