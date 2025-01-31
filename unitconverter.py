while True:  # Start a loop
    # Ask for user input
    miles = float(input("Enter a length in miles: "))
    kilometers = float(input("Enter a length in kilometers: "))

    # Perform conversions
    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    # Display results
    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

    # Ask if the user wants to convert again
    repeat = input("Do you want to convert another? Please type 'yes' or 'no': ").strip().lower()

    # Check if the user wants to exit
    if repeat != 'yes':  # If the user does not type 'yes', exit the loop
        print("Thanks for using the converter, Goodbye!")
        break  # Exit the loop
    else:
        print("Converting again,")  
