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
print("9. Exit")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    for i in range(1, rows + 1):
        print('*' * i)

elif choice == 2:  # Square with Hollow Center
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

elif choice == 3:  # Diamond
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

elif choice == 4:  # Left-angled Triangle
    for i in range(rows, 0, -1):
        print('*' * i)

elif choice == 5:  # Hollow Square
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

elif choice == 6:  # Pyramid
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

elif choice == 7:  # Reverse Pyramid
    for i in range(rows, 0, -1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

elif choice == 8:  # Rectangle with Hollow Center
    # TODO: Handle separate width and height inputs for rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    pass

elif choice == 9:  # Allow the user to exit
    print('Goodbye')
else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit
