"""
Strategy:   Build classes independently and let inheritance
            discover itself
Examlpe:    Validators

Why don't professional chess player think more then 2 steps ahead?
Why not think 10 steps ahead?

The reason is that each move teaches you something new about the
state of the game. In essence, you are walking through a fog and
with each step, in the fog, more of the path is revealed.

A lot of coding problems are similiar to chess move problems,
where you can't see the end. Therefore fully planning the solution in
advance often times does NOT work. Unless the problem is a well-known
problem with documented patters. A better approach to planning is using
agile methods to let the solutions discover themselves.

Problem:    Build a collection of data validation utilities
            using descriptors.

Example:

    class Resource:
        resource_id = Number(minvalue=0)
        name = String(minsize=2, maxsize=20)
        category = OneOf('pending', 'idle', 'active', 'shutdown')
"""
# Contruct custom validator classes
# Don't plan ahead nor should you use inheritence early
class Number:
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Expected {value!r} to be at least {self.minvalue!r}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Expected {value!r} to be no more than {self.maxvalue!r}')
        setattr(obj, self.private_name, value)


class String:
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, (str)):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Expected {value!r} to be no smaller than {self.minsize!r}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Expected {value!r} to be no bigger than {self.maxsize!r}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f'Expected {self.predicate!r} to be true for {value!r}')
        setattr(obj, self.private_name, value)


# Given the patterns that have appeared 
# use Inheritence to abstract the classes
# and add a new Validator class
from abc import ABC, abstractmethod


class Validator(ABC):
    """Descriptor for managed attribute access.

    Verifies that new value meets various type and range restrictions.
    """
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        """Test various restrictions as needed."""


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or floar')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Expected {value!r} to be at least {self.minvalue!r}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Expected {value!r} to be no more than {self.maxvalue!r}')

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, (str)):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Expected {value!r} to be no smaller than {self.minsize!r}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Expected {value!r} to be no bigger than {self.maxsize!r}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f'Expected {self.predicate!r} to be true for {value!r}')


"""Exercise 1:  Create a new validator class, that inherits from Validator,
                and supply a validate method."""

# Example solution:
class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')

"""Exercise 2:  Create a practical example of a new real class that
                make use of the data validators above."""

# Example solution:
class Component:
    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf('wood', 'metal', 'plastic')
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


def main():
    """Create instances of the application class.

    Create invalid instances of the class and see if the descriptors
    prevent them from being created.
    """
    c1 = Component('Widget', 'metal', 'plastic')    # Blocked: 'Widget' is not all uppercase

    c2 = Component('WIDGET', 'metle', 5)            # Blocked: 'metle' is misspelled

    c3 = Component('WIDGET', 'metle', -5)           # Blocked: -5 is negative

    c4 = Component('WIDGET', 'metle', 'V')          # Blocked: 'V' is not a number

    c5 = Component('WIDGET', 'metal', 5)            # Allowed: The inputs are valid


if __name__ == "__main__":
    main()
