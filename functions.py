FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads a text file, while also returning
    a list of to-do items
    """
    with open(filepath, 'r') as document:
        todos_local = document.readlines()
    return todos_local


def write_todos(writing_data, filepath=FILEPATH):
    """
    Writes a list into the text file
    """
    with open(filepath, 'w') as document:
        document.writelines(writing_data)


if __name__ == "__main__":
    print("This is running directly from the script!")