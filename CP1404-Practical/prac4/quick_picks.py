import random
max_num_per_line = 6
MIN = 1
MAX = 45
def main():
    number_picks = int(input(print("How many quick picks")))
    if number_picks <= 0:
        print("Invalid number.Please try again")
        number_picks = int(input(print("How many quick picks")))
    for i in range(number_picks):
        quick_pick = []
        for j in range(max_num_per_line):
            number = random.randint(MIN,MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()