# Problem 6: Words appearing in exactly one document
def unique_words_in_documents(*documents):
    all_words = set()
    word_count = {}
    for doc in documents:
        for word in doc:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    unique_words = {word for word, count in word_count.items() if count == 1}
    return unique_words

doc1 = {"apple", "banana", "cherry"}
doc2 = {"banana", "dragonfruit", "elderberry"}
doc3 = {"cherry", "fig", "grape"}

unique_words = unique_words_in_documents(doc1, doc2, doc3)
print("Words appearing in exactly one document:", unique_words)
