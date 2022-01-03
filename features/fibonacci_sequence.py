
def fibonacci_index(index):
    """
    Returns fibonacci sequence with the given index being the last value.
    if the value passed to it is None it will do nothing and it will return [0, 1]
    if the value passed to it is less than 3.
    """
    if index:
        initial_sequence = [0, 1]
        if index < 3:
            return initial_sequence
        else:
            while len(initial_sequence) < index:
                next = initial_sequence[-2] + initial_sequence[-1]
                initial_sequence.append(next)
            return initial_sequence
    pass


def fibonacci_until(values_until):
    """
    Returns all fibonacci sequence values before the given number.
    if the value passed to it is None it will do nothing.
    """

    if values_until:
        initial_sequence = [0, 1]
        while initial_sequence[-1]+initial_sequence[-2] < values_until:
            next = initial_sequence[-2] + initial_sequence[-1]
            initial_sequence.append(next)
        return initial_sequence
    pass
