def sol(string1, string2):
    idx = -1
    for index, char in enumerate(string2):
        # Check if the characters at the current index are different
        if char != string1[index]:
            idx = index
            break
    # If no extra character is found in the loop, it's the last character in str1
    if idx == -1:
        idx = len(string1) - 1
    alphabet = string1[idx]

    new_string1 = ''
    for i in range(len(string1)):
        if i != idx:
            new_string1 += string1[i]

    if new_string1 != string2:
        return 0
    
    # dict1 = {}
    # for i in range(len(string1)):
    #     char = string1[i]
    #     if char in dict1:
    #         dict1[char].append(i)
    #     else:
    #         dict1[char] = []
    #         dict1[char].append(i)

    dict2 = {}
    for i in range(len(string2)):
        char = string2[i]
        if char in dict2:
            dict2[char].append(i)
        else:
            dict2[char] = []
            dict2[char].append(i)

    if alphabet in dict2:
        array = dict2[alphabet]
        ans = ''
        ans += str(len(array))
        for n in array:
            ans += f'{n} '
        return ans
    else:
        return f'1\n{idx}'        



if __name__ == "__main__":
    
    string1 = input()
    string2 = input()
    
    print(sol(string1 , string2))


