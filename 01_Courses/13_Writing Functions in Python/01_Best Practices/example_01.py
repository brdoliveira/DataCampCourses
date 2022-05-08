import inspect

def function_name(arguments):
    """ DOCSTRING
    Description of what the function does.

    Description of the arguments, if any.

    Description of the return value(s), if any.

    Description of errors raised, if any.

    Optional extra notes or example of usage.
    """

# Google style - description
def function(arg_1,arg_2=42):
    """
    Description of what the function does.

    Args:
        arg_1 (str): Description of arg_1 that can break onto the next line
        if needed.
        arg_2 (int, optional): Write optional when an argument has a default
        value.

    Returns:
        bool: Optional description of the return value
        Extra lines are not indented.

    Raises:
        ValueError: Include any error types that the function intentionally
        raises.

    Notes:
        See https://www.datacamp.com/community/tutorials/docstrings-python
        for more info.
    """

# Numpydoc
def function(arg_1,arg_2=42):
    """
    Description of what the function does.

    Parameters
    ----------
    arg_1 : expected type of arg_1
        Description of arg_1.
    arg_2 : int, optional
        Write optional when an argument has a default value.
        Default=42.
    
    Returns
    -------
    The type of the return value
        Can include a description of the return value.
        Replace "Returns" with "Yields" if this function is a generator.
    """

# Retrieving docstrings
def the_answer():
    """ Return the answer to life,
    the universe, and everything.

    Returns:
        int
    """
    return 42

print(the_answer.__doc__)

# Or :

print(inspect.getdoc(the_answer)) 