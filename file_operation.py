with open('data.txt', 'r') as file:
    text = file.read()
    words = text.split()
    print(len(words))