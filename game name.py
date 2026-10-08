import random


def main():

    series = ["Manipur", "Kangleipak", "Meitreibak", "Sanaleibak"]
    word = random.choice(series)
    pos = random.sample(range(len(word)), 2)
    display = []

    for i in range(len(word)):
        if i in pos:
            display.append(word[i])
        else:
            display.append("_")
    while "_" in display:
        print(" ".join(display))
        user = input("Enter a word : ")

        if user.isalpha() and len(user) == 1:

            if user in word:
                for i in range(len(word)):
                    if user == word[i]:
                        display[i] = user
            else:
                print("Wrong guess")
        else:
            print("Plesase enter a single word")
    else:
        print(f"You have done it. You have sucessfully guess the word {word}")


if __name__ == "__main__":
    main()
