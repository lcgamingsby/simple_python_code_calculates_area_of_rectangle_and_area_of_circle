while True:
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            raise ValueError("Invalid input! Length and width must be positive.")
        else:
            area = length * width
            print("The area of the rectangle is:", area)
            break

    except ValueError as e:
        print(e)
        print("Please enter valid input!")