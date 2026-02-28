def greet(name):
    return f"Hello {firstName} {lastName} !"

if __name__ == "__main__":
    firstName = input("Enter your firstname: ")
    lastName = input("Enter your lastname: ")

    print(greet(firstName, lastName))