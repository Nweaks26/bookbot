def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    chars = {}

    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars


def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:

        file_contents = f.read()
    
    print(count_words(file_contents))
    print(count_letters(file_contents))




main()