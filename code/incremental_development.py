"""
Strategy:   Incremental development
Example:    Tree walker

Feyneman method:

    1. Write down the problem
    2. Think very hard.
    3. Write down the answer.

Problem to be solved: Given a target find the path to it, starting with
any node in a tree:

    tree['two'][3]['seven'] -> 7

Strategy: Solve related but simpler problem > Incremental development.
"""

TREE = {
    'one': [
        'abc',
        'def',
        'ghi',
        {
            'four': 4,
            'five': 5,
        },
    ],
    'two': [
        'jkl',
        'mno',
        'BLUE',
        {
            'six': 6,
            'seven': 7,
        }
    ],
    'three': [
        'qrs',
        'BLUE',
        'BLUE',
        {
            'eight': 'BLUE',
            'nine': 9,
        }
    ],
}

# Start by solving the simplest problem then
# develop the solution incrementally.
def count_target_1(target, node):
    """Check if the node is the target."""
    if target == node:
        return 1
    return 0


def count_target_2(target, node):
    """Count occurences of the target in nested list."""
    if target == node:
        return 1
    if isinstance(node, list):
        return sum(count_target_2(target, subnode) for subnode in node)
    return 0


def count_target_3(target, node):
    """Count occurences of the target in nested list or dict."""
    if target == node:
        return 1
    if isinstance(node, list):
        return sum(count_target_3(target, subnode) for subnode in node)
    if isinstance(node, dict):
        return sum(count_target_3(target, subnode) for subnode in node.values())
    return 0


# Use the lagoc from simpler solved problems
# to solve a more complex problem.
def path_to_target(target, node):
    """Print the path to the target.

    Use enumerators index to reference the pathway to the target.
    """
    if target == node:
        return f' -> {target!r}'
    elif isinstance(node, list):
        for i, subnode in enumerate(node):
            path = path_to_target(target, subnode)
            if path:
                return f'[{i}]{path}'
    elif isinstance(node, dict):
        for key, subnode in node.items():
            path = path_to_target(target, subnode)
            if path:
                return f'[{key}]{path}'
    return ''


def main():
    """ Excerice in understanding.

    Before running the print functions, try to understand the code
    and write down what the return value for each function.

        "This is not a hard problem, but this is methodology that
         scales very well to hard problems.""
                                                - Raymond Hetinger
    """

    p = print

    p(count_target_1('blue', 'green'))

    p(count_target_1('blue', 'blue'))

    p(count_target_1('red', ['red', 'blue', 'red', 'red']))

    p(count_target_2('blue', ['red', 'blue', 'red', 'red']))

    p(count_target_2('purple', ['red', 'blue', 'red', 'red']))

    p(count_target_2('red', ['red', ['blue', 'red'], 'red']))

    p(count_target_3('red', TREE))

    p(count_target_3('BLUE', TREE))

    p(path_to_target('abc', 'abc'))

    p(path_to_target('abc', ['?', '?', '?', 'abc', '?']))

    p(path_to_target('abc', ['x', ['?', '?', '?', 'abc', '?']]))

    p(path_to_target('abc', TREE))

    p(path_to_target(7, TREE))


if __name__ == "__main__":
    main()
