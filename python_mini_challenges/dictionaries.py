# dictionaries.py

def dictionary_operations():
    student = {
        "ID": 101,
        "Name": "Devangi",
        "Course": "Python",
        "Marks": 92
    }

    print("Student Dictionary")
    print("------------------")

    for key, value in student.items():
        print(f"{key}: {value}")

    student["Marks"] = 95
    student["City"] = "Delhi"

    print("\nUpdated Dictionary")
    print("------------------")

    for key, value in student.items():
        print(f"{key}: {value}")

    print("\nKeys:", student.keys())
    print("Values:", student.values())


if __name__ == "__main__":
    dictionary_operations()