import random
def guessNumber(num, ip):
        if ip > num:
            print("Too High")
        elif ip < num:
            print("Too Low")
        elif ip == num:
            print("Congrats, you guessed it right")
            exit(0)
if __name__ == '__main__':
    num = random.randint(1, 20)
    chance = 5

while chance > 0:
    ip = int(input("Guess the number between 1 & 20: "))
    guessNumber(num, ip)
    chance -= 1
print("Sorry you are out of turn, you loose")