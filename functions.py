

TODO_FILE_PATH = "todos.txt"

def get_todos(filepath=TODO_FILE_PATH):
    """
    Read todos from a file.

    Args:
        filepath (str): The path to the file from which the todos will be read.

    Returns:
        list[str]: A list of todos read from the file.
    """
    with open(filepath, "r") as file:
            todos = file.readlines()
    return todos

def write_todos(todos_argument,filepath=TODO_FILE_PATH ):
    """
    Write todos to a file.

    Args:
        filepath (str): The path to the file where the todos will be written.
        todos_argument (list[str]): The list of todos to be written to the file.

    Returns:
        None
    """
    with open(filepath, "w") as file:
            file.writelines(todos_argument)   
            
            
if __name__== "__main__":
    print("hello")
    print(get_todos())