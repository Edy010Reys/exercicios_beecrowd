b = True
while True:
    cases = int(input())
    if cases == 0:
        break
    if b:
        b = False
    else:
        print('')
    list_words = []
    list_spaces = []
    while cases > 0:
        cases -= 1
        word = input().strip()
        list_words.append(word)
        list_spaces.append(len(word))
    max_space = max(list_spaces)
    for item in list_words:
        print(item.rjust(max_space))
