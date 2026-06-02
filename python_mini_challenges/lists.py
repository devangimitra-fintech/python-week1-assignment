# lists.py

def list_operations():
    numbers = [10, 20, 30, 40, 50]

    print("Original List:", numbers)

    numbers.append(60)
    print("After Append:", numbers)

    numbers.insert(2, 25)
    print("After Insert:", numbers)

    numbers.remove(40)
    print("After Remove:", numbers)

    print("Maximum Value:", max(numbers))
    print("Minimum Value:", min(numbers))
    print("Sum:", sum(numbers))

    numbers.sort()
    print("Sorted List:", numbers)

    numbers.reverse()
    print("Reversed List:", numbers)


if __name__ == "__main__":
    list_operations()