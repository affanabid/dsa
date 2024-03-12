def longest_prefix(words):
    prefix = ''
    first_word = words[0]
    for i in range(len(first_word)):
        letter = first_word[i]
        print(letter)
        count = 0
        for i in range(1, len(words)):
            current_word = words[i]
            for alp in current_word:
                print(alp, end=' ')
            print()
            # if letter == current_word[0]:
            #     count += 1
        print()
        # for j in range(len(word)):
        #     print(word[j], end=' ')
        # print()

words = ['flower', 'flow', 'fly']
longest_prefix(words)