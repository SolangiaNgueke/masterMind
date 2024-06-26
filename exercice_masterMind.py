from random import *

def secret_list(niv=4, color=6):
	secret=[str(randint(1,color)) for i in range (niv)]
	return secret

#print(secret_list())

def player_combination():
    while True:
        proposition = input("Proposez une combinaison de 4 chiffres (1-6) : ")
        if len(proposition) != 4:
            print("La combinaison doit être de 4 chiffres.")
            continue  # Loop again instead of returning False
        for char in proposition:
            if char not in '123456':
                print("Les chiffres doivent être entre 1 et 6.")
                break  # Break the for loop to prompt for input again
        else:
            return list(proposition)

#print(player_combination())

def verification(secret, guess):
    correct, incorrect = 0, 0
    secret_copy = secret[:]
    guess_copy = guess[:]

    for i in range(4):
        if guess[i] == secret[i]:
            correct += 1
            secret_copy[i] = guess_copy[i] = None

    for i in range(4):
        if guess_copy[i] and guess_copy[i] in secret_copy:
            incorrect += 1
            secret_copy[secret_copy.index(guess_copy[i])] = None

    return correct, incorrect


def play():

    secret = secret_list()
    nbr = 10

    print("Bienvenue au jeu Mastermind !")
    print("Vous devez deviner une combinaison de 4 chiffres entre 1 et 6.")
    print(f"Vous avez {nbr} tentatives pour deviner la combinaison secrète.")

    for nb in range(1, nbr + 1):
        print(f"\nTentative {nb}/{nbr}")
        player_proposition = player_combination()
        correct, incorrect = verification(secret, player_proposition)

        print(f"Indices : bien placés {correct} et mal placés {incorrect} ")

        if correct== 4:
            print("Félicitations vous avez réussi :)")
            break
    else:
        print("les tentatives sont épuisées")
        print(f"La combinaison secrète était : {''.join(secret)}")

if __name__ == "__main__":
    play()
