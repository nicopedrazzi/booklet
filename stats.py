def get_book_text(PATH):
    with open(PATH) as f:
        file_contents = f.read()
    return file_contents


def get_text(text):
    words = text.split()
    x = len(words)
    return words, x

def tot_let(dict):
    sum = 0
    for key,num in dict.items():
        if not key.isalpha():
            continue
        else:
            sum += num
    return sum


def get_letter_number(words):
    alphabet = {}
    for word in words:
        for letter in word:
            char = letter.lower()
            if char not in alphabet:
                alphabet[char]=1
            elif char in alphabet:
                alphabet[char] += 1
    return alphabet


def sort_dict(dict):
    list = []
    for key, value in dict.items():
        if not key.isalpha():
            continue
        list.append({"char": key, "num": value})
    list.sort(reverse=True, key=lambda x: x["num"])
    return list
    