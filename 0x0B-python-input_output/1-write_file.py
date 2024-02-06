#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Function writes in txt format, returns number of chars written.

    Arguments:
        filename (str): name of file to write to (default is empty string).
        text (str): text to write to file (default is empty string).

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    write_file()
