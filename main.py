def main():
    """ Main Program """
    menu()

    # Declare variable to loop through
    option = int(input("What would you like to do? "))

    while option != 0:
        
        if option == 1:
            print(1)
        elif option == 2:
            print(2)
        elif option == 3:
            print(3)
        elif option == 4:
            print(4)
        elif option == 5:
            print(5)
        else:
            print("That's an invalid option.")

    # Exit message
    print("Thank you for using the Job Application Tracker program!")

    return 0

# FUNCTIONS

def menu():
    
    print("Welcome to the Job Application Tracker!\n" \
    "1. Add new application\n" \
    "2. View all applications\n" \
    "3. Update application stauts\n" \
    "4. Delete an application\n" \
    "5. Search applications\n" \
    "0. Exit")

if __name__ == "__main__":
    main()