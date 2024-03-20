def read_file(filename):
    arr1 = []
    # Open the file in read mode
    file = open(filename, "r")
    line = file.readline()
    # Read each line in the file
    while line:
        # Append each line to the array
        arr1.append((line.strip()))
        line = file.readline()
    file.close()
    return arr1


def get_menu_border(file_name):
    border_menu = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                border_menu.append(line.rstrip())  # Use rstrip() to remove trailing newline characters
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return border_menu


def print_sorted(arr):
    # Open a file for writing ('w' mode)
    with open('res/dict.txt', 'w') as file:
        # Write content to the file
        for i in range(len(arr)):
            file.write(str(arr[i]) + "\n")
        file.close()

