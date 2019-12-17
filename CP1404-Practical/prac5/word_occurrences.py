def CountFrequency(my_list):
    freq = {}
    words = my_list.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    for key,value in freq.items():
        print("{} : {} ".format(key, value))


def main():
    my_list = input(print(" Please enter a string: "))
    print(CountFrequency(my_list))
main()