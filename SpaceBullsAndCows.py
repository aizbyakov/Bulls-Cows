import os
import random

DEBUG = False

def clear_console():
    """Clears the console screen."""
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')


def generate_secret(length):
    res = []
    
    for _ in range(s_lenght):
        res.append(0)
        
    s_idx = 0
    
    while s_idx < len(res):
        r = random.randint(0, 9)
        
        exists = False
        
        for j in range(0, s_idx):
            if res[j] == r:
                exists = True
                break
            
        if not exists:
            res[s_idx] = r
            s_idx = s_idx + 1
    
    return res


while True:
    print("\tThe starship Odyssey was trapped by an asteroid field, its navigation system locked. Captain Anya's only hope was to crack the alien mothership's encrypted communication before the asteroids hit. The mothership, hovering silently, sent back clues: Bulls and Cows. Anya's crew worked frantically, their guesses echoing through the silent cockpit. A 'bull' meant a correctly positioned digit in the mothership's code. A 'cow' meant a correct digit but in the wrong spot. With each flash of an asteroid, a new guess was sent. Anya, remembering her training, saw patterns in the feedback. She eliminated possibilities, narrowing the permutations.")
    print("\n")
    print("""Rules of the Game:
1. Mothership chooses a secret number with no repeating digits.
2. Player (the code-breaker) tries to guess the secret digit sequence.
3. After each guess, the Mothership provides hints:
    Bulls: The number of digits that are correct and in the right position.
    Cows: The number of digits that are correct but in the wrong position.
4. The code-breaker continues guessing based on the hints.
5. The game ends when the code-breaker correctly guesses all digits in the correct positions (bulls), winning the game.""")

    print("\n")
    print("\n")

    
    s_lenghtStr = input("Input length of the secret [2 - 9]\n>")

    s_lenght = 0

    if s_lenghtStr.isdigit():
        s_lenght = int(s_lenghtStr)
    
    if s_lenght < 2 or s_lenght > 9:
        print("Invalid secret's length\n")
        continue
        
    secret = generate_secret(s_lenght)
        
    if DEBUG:
        print(f"\n#\tSecret: {secret}\n")
    
    print(f"The secret has been generated with length {len(secret)}\n")
    print("\n")

    history = []

    while True:
        gStr = input("Your guess >")

        if not gStr.isdigit():
            print("You must enter digit sequense")
            continue
            
        if len(gStr) != len(secret):
            print(f"The lengh must be {len(secret)}")
            continue
        
        guess = []
        
        for d in gStr:
            guess.append(int(d))
    
        if DEBUG:
            print(f"\n#\tGuess: {guess}\n")

        countBulls = 0
        countCows = 0
        
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                countBulls = countBulls + 1
                
            for j in range(len(guess)):
                if j == i:
                    continue
                elif guess[i] == secret[j]:
                    countCows = countCows + 1
        
        print(f"\t\tB{countBulls} C{countCows}")
        
        history.append([guess, countBulls, countCows])
        
        if (countBulls == len(secret)):
            print("\n")
            print("Congratulations!!! You have revealed the secret!")
            print("\n")

            print("Game history:")
            
            for h in history:
                print(f"Guess: {h[0]} \t Bulls: {h[1]}   Cows: {h[2]}")
            
            print(f"Total guesses: {len(history)}")
            
            print("\n")
            break

    iStr = input("Do you want to play another game (Y/N)? >")
    
    if iStr.lower().startswith("y"):
        print("\n")
        print("BYE!")
        print("\n")
        break
            
    clear_console()
        