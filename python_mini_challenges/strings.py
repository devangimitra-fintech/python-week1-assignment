# strings.py

def string_operations():
    text = input("Enter a string: ")

    print("\nString Operations")
    print("-----------------")
    print("Original String :", text)
    print("Upper Case      :", text.upper())
    print("Lower Case      :", text.lower())
    print("Length          :", len(text))
    print("Reversed String :", text[::-1])
    print("Title Case      :", text.title())

    word = input("\nEnter a word to search: ")

    if word in text:
        print(f"'{word}' found in the string.")
    else:
        print(f"'{word}' not found in the string.")


if __name__ == "__main__":
    string_operations()