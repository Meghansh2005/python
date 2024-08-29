
input_string = input("Enter a sequence of comma-separated words: ")


words = input_string.split(',')


words.sort()


sorted_words = ",".join(words)


print(sorted_words)
