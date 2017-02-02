# pylint: disable=invalid-name

""""Dragon's Curve
http://www.codewars.com/kata/53ad7224454985e4e8000eaa

The dragon's curve is a self-similar fractal which can be obtained by a
recursive method.

Starting with the string D0 = 'Fa', at each step simultaneously perform the
following operations:

    replace 'a' with: 'aRbFR'
    replace 'b' with: 'LFaLb'

For example (spaces added for more visibility) :

    1st iteration: Fa -> F aRbF R
    2nd iteration: FaRbFR -> F aRbFR R LFaLb FR

After n iteration, remove 'a' and 'b'. You will have a string with 'R','L',
and 'F'. This is a set of instruction. Starting at the origin of a grid
looking in the (0,1) direction, 'F' means a step forward, 'L' and 'R' mean
respectively turn left and right. After executing all instructions, the
trajectory will give a beautifull self-replicating pattern called
'Dragon Curve'

The goal of this kata is to code a function wich takes one parameter n, the
number of iterations needed and return the string of instruction as defined
above. For example:

    n=0, should return: 'F'
    n=1, should return: 'FRFR'
    n=2, should return: 'FRFRRLFLFR'

n should be a number and non-negative integer. All other case should return
the empty string: ''.
"""


def change(char):
    """Change char according dragon pattern rules

    Args:
        char (str): Character to be changed

    Returns:
        str: New character

    Examples:
        >>> change('a')
        'aRbFR'
    """
    return 'aRbFR' if char == 'a' else 'LFaLb' if char == 'b' else char


def Dragon(num, pattern='Fa'):
    """Recursive construct dragons curve pattern

    Args:
        num (int): Number of iterations
        pattern (str): Current pattern string

    Returns:
        str: Dragons curve pattern

    Examples:
        >>> Dragon(4)
        'FRFRRLFLFRRLFRFRLLFLFRRLFRFRRLFLFRLLFRFRLLFLFR'
    """
    if not isinstance(num, int) or num < 0:
        return ''
    if num == 0:
        return pattern.replace('a', '').replace('b', '')
    else:
        pattern = ''.join(change(char) for char in pattern)
        return Dragon(num - 1, pattern)