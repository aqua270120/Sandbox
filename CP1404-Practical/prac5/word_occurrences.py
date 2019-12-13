def word_count(str):
    counts = {}
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    words
    return counts
def main():
    text_input = input(print("Enter a string:"))
    print(word_count(text_input))
main()