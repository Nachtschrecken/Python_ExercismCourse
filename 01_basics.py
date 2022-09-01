"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual):
    EXPECTED_BAKE_TIME - actual
    pass

    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

def preparation_time_in_minutes(layers):
    layers * PREPARATION_TIME
    pass

    """
    takes the number of layers you want to add to the
    lasagna as an argument and returns how many minutes you
    would spend making them. Assume each layer takes 2 minutes
    to prepare.
    """

def elapsed_time_in_minutes(layers, actual):
    actual + preparation_time_in_minutes(layers)
    pass

    """
    elapsed_time_in_minutes() function that has two parameters:
    
    number_of_layers (the number of layers added to the lasagna)
    and
    elapsed_bake_time (the number of minutes the lasagna has been baking in the oven).
    
    This function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already spent
    baking in the oven.
    """