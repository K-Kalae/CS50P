import random


def main():

    score = 0
    level = get_level()

    for i in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        score += ver_answer(x,y)

    print("Score:", score)





def get_level():
    while True:
        try:
            tevel=int(input("Level: "))
            if tevel in [1,2,3]:
                return tevel


        except ValueError:
            pass




def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10**level - 1)



def ver_answer(x,y):
    tries = 0
    while tries<3:
        try:
            tries+=1
            ans=int(input(f"{x} + {y} = "))
            if ans == x + y:
                return 1
                break
            else:
                print("EEE")
        except ValueError:
            pass
    print(f"{x} + {y} = {x + y}")
    return 0






if __name__ == "__main__":
    main()
