def reverse(string):
    if len(string) == 0:
        return 0
    new_string = string[1:]
    reverse(new_string)
    print(string[0], end=" ")

def main():
    strings = ["affan", "data", "science", "afernoon", "pucit"]
    for string in strings:
        print(f"{string}: ", end=" ")
        reverse(string)
        print()

if __name__ == "__main__":
    main()