# files i/o practice

f = open("_file.txt")
data = f.read()

content_changed = data.replace("Hey", "Hello")

f = open("_file.txt", "w")
f.write(content_changed)
print("File content changed successfully.")
f.close()


with open("1fulltesting.txt") as f:
    current_content = f.read()

if ("This" in current_content):
    a = current_content.replace("This", "That")
else:
    print("This word is not present in the file.")

with open("1fulltesting.txt", "w") as f:
    f.write(a)
    print("File content changed successfully.")



with open("1fulltesting.txt") as f:
    content1 = f.read()
    a1 = content1.upper()

with open("1fulltesting.txt", "w") as f:
    f.write(a1)
    print(a1)
    print("File content changed successfully.")


def game2person():
    player1 = int(input("Enter player 1 score: "))
    player2 = int(input("Enter player 2 score: "))

    if player1 > player2:
        result = f"player 1 is winner with a score of: {player1}"
    elif player1 < player2:
        result = f"player 2 is winner with a score of: {player2}"
    else:
        result = "draw"

    print(result)
    return result

if __name__ == "__main__":
    result = game2person()
    with open("score.txt", "w") as f:
        f.write(result)

# lets make same game with password privacy so player 2 not see player 1 score

def gameprivacy():
    import getpass

    player1 = int(getpass.getpass("Enter player 1 score: "))
    player2 = int(getpass.getpass("Enter player 2 score: "))

    if player1 > player2:
        result1 = f"player 1 is winner with a score of: {player1}"
    elif player1 < player2:
        result1 = f"player 2 is winner with a score of: {player2}"
    else:
        result1 = "draw"

    print(result1)
    return result1

with open("score.txt", "w") as f:
    f.write(gameprivacy())
f.close()


