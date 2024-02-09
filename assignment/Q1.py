def palindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[-1]:
        return False
    new_string =string[1:-1]
    return palindrome(new_string)

def main():
    strings = ["nitin", "amama", "affan", "hannah", "hamzah"]
    for string in strings:
        print(string, end=": ")
        if palindrome(string) == True:
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")

if __name__ == "__main__":
    main()