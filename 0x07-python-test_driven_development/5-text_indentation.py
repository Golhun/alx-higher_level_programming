#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = (".", "?", ":")
    final_text = ""
    
    for char in text:
        if char in chars:
            final_text += f"{char}\n\n"
        else:
            final_text += char

    print(final_text)
