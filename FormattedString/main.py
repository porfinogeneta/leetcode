def formatText(text, width):
    res = ""
    sentences = []
    sen = []
    for word in text.split(" "):
        sen.append(word + " ")
        if word[-1] in ".?!":
            sentences.append(sen)
            sen = []
    res += "*" * (width + 2)
    for s in sentences:
        available = width
        res += "\n*  " # nowe zdanie to nowa linia, odstęp dwóch spacji oraz *
        available -= 2
        while s:
            word = s.pop(0)
            if available > len(word):
                res += word
                available -= len(word)
            else:
                res += available * " " + "*" # zabrakło miejsca, uzeupełniamy spacjami i * na końcu
                res += "\n*" # nowa linia to * na początku
                res += word
                available = width - len(word)
        # koniec zdania to uzupełnienie spacjami i zamknnięcie *
        res += " " * available + "*"
    # w ostaniej linii *
    res += "\n" + "*" * (width + 2)

    print(res)

formatText("Hello! My name is Tom. Would you like to format this text properly?", 16)