"""
Strategy:   Chunking and Aliasing
Example:    Random module

Chunking:   Grouping related items together so that someone can
remember them more easily. Grouping different bits of
information together into more manageable or meaningful chunks.

The Magical Number 7, +- 2: Article by George A .Miller about human
capacity for remembering number of objects in the short-term memory.

Aliasing:   Take an existing thing you know, link the knowledge to
that and through aliasing you have two refrences to the same piece
of data.

Author's note:

The processing of chunking and aliasing can be exemplified by the date.
Take 8 numbers for example, that is 1 or more objects then what an
average human can remember on a bad/average day. Instead we can chunk
the objects into specific grouping:

    14082023 > 14, 08, 2023

The 8 digit number was grouped into; 'day', 'month' and 'year'. The
numbers can be proccessed further by aliasing the collection of numbers
into a single reference:

    14, 08, 2023 > 14-08-2023

Now we have aliased the group of numbers into a single  reference
called 'date'. The registers needed to comprehend the 8 orginal
numbers went down from 8 > 3 > 1, by chunking and aliasing.

"""
from random import *

def main():
    """Example code.

    The examples below show what reducing cognitive overload can do for
    readability and comprehension. Find ways to chunk code into groups
    then alias the information into a concept (reference).
    """
    p = print

    # Get a random number of a specific range
    p(random())                         # 0.0 <= x < 1.0

    p(50 + random() * 200)              # 50.0 <= x < 250.0

    p(50 + random() * 200)              # 50.0 <= x < 250.0


    # Chunking the above examples
    p(uniform(50, 250))                 # 50.0 <= x < 250.0


    # Get a random number of a specific range in multples of 5
    p(int(random() * 200))              # 0 <= x < 200

    p(int(random() * 200) * 5)          # 0 <= x < 1000  in multiples of 5

    p(5000 + int(random() * 200) * 5)   # 5000 <= x < 6000  in multiples of 5


    # Alias a portion of the above examples in python using range function
    p(list(range(10)))                  # [0, 1, 2, 3, ,4 ,5 ,6 ,7 ,8 ,9]

    p(list(range(5, 10)))               # [10, 11, 12, ... 99]

    p(list(range(10, 100, 5)))          # [10, 15, 20, ... 95]


    # Chunking and aliasing process
    p(5000 + int(random() * 200) * 5)   # 5000 <= x < 6000  in multiples of 5

    p(list(range(5000, 60000, 5)))      # [5000, 5005, 5010, ... 5995]

    p(randrange(5000, 6000, 5)          # 5000 <= x < 6000  in multiples of 5


    # Get a random outcome out of a set of choices
    outcomes = ['win', 'lose', 'draw', 'double', 'try again']

    p(len(outcomes))                    # 5

    p(random())                         # 0.0 <= x < 1.0

    p(random() * len(outcomes))         # 0.0 <= x < 5.0

    p(int(random() * len(outcomes)))    # 0 <= x < 5

    p(outcomes[int(random() * len(outcomes))])  # ['win, 'lose', ...]


    # Chunking and aliasing process
    p(outcomes[randrange(len(outcomes))])       # ['win, 'lose', ...]  

    p(choice(outcomes)                          # ['win, 'lose', ...] 


    # Run multiple outcomes
    p([outcomes[int(random() * len(outcomes))] for i in range(10)]) # 10x O

    p([outcomes[randrange(len(outcomes))] for i in range(10)])      # 10x O

    p([choice(outcomes) for i in range(10)])                        # 10x O

    p(choice(outcomes, k=10))                                       # 10x O


def exercise():
    """Exercise in understanding.

    Write a simple game of rock, paper while implementing your new
    found knowledge of chunking and aliasing.

    The game logic is provided as is, while the solution is provided
    at the bottom of the file.
    """
    # Your code goes here 

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()
    exercise()

"""
    Solution down below.












    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    computer_choice = choice(options)

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
"""
