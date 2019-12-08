def main():
    #Change the first element to number 10
    numbers = [3, 1, 4, 1, 5, 9, 2]
    for n, i in enumerate(numbers):
        if i == 3:
            numbers[n] = 10
    print(numbers)

    for i in range(len(numbers)):
        if numbers[i] == 2:
            numbers[i] = 1
    print(numbers)




    x = numbers[2:len(numbers)]
    print(x)
    check = 9 in numbers
    print(check)



main()