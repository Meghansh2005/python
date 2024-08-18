
def analyze_sentence(sentence):
    word_count = 0
    digit_count = 0
    uppercase_count = 0
    lowercase_count = 0

   
    words = sentence.split()
    word_count = len(words)

    
    for char in sentence:
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return word_count, digit_count, uppercase_count, lowercase_count

# Input: Get the sentence from the user
sentence = input("Enter a sentence: ")


word_count, digit_count, uppercase_count, lowercase_count = analyze_sentence(sentence)


print(f"This sentence has {word_count} words")
print(f"This sentence has {digit_count} digits")
print(f" {uppercase_count} upper case letters")
print(f" {lowercase_count} lower case letters")
