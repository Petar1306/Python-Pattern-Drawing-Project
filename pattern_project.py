# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    # TODO: Loop through rows and print increasing stars
    for i in range(1, rows + 1):
        print('*' * i)

elif choice == 2:  # Square with Hollow Center
    # TODO: Create a square with a hollow center
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

elif choice == 3:  # Diamond
    # TODO: Create a diamond shape using loops
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

elif choice == 4:  # Left-angled Triangle
    # TODO: Print decreasing stars for each row
    pass

elif choice == 5:  # Hollow Square
    # TODO: Similar to choice 2 but ensure perfect square logic
    pass

elif choice == 6:  # Pyramid
    # TODO: Center-align stars to form a pyramid
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

elif choice == 7:  # Reverse Pyramid
    # TODO: Create an upside-down pyramid
    pass

elif choice == 8:  # Rectangle with Hollow Center
    # TODO: Handle separate width and height inputs for rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    pass

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit
