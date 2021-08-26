# What Is This?
This repository is a command-line tool that performs basic arithmetic operations on the provided
fractions and produces the result of those operations as a fraction.

# Specifications
## Official
* Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
* Operands and operators shall be separated by one or more spaces
* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
* Improper fractions and whole numbers are also allowed as operands

## Things Got Weird And Specifications Changed
* Negative fractions will be indicated by a '-' directly before the fraction with no spaces
* Floats are not supported, only integers

# How Do I Use It?
This repository contains an executable file called [`fraction-calculator`](fraction-calculator) that can be downloaded and
run. This file includes all necessary dependencies and *should* be able to run in any *nix-style shell.

# Testing
Running the full test suite is painful as one of the tests runs the generated executable for something like 1600 test cases.
It's slow. Go get a coffee or a beer. We're approaching fall, a medium ale might be appropriate (why do we only get red ales
in the spring???). Or if you like something hoppier, I'm currently digging Elysian's Space Dust. If you're in the Mountlake
Terrace area, check out the menu at [Hemlock State](https://www.hemlockstate.com). I'm a little disappointed that I'm going
to have to wait for their barrel-aged Brew Tang Clan. It's delicious but definitely more appropriate to colder weather (IMO).

## You Really Want To Run The Tests
If you must, you'll need to ensure that pytest is installed on your system and run:
```
pytest tests/test_*
```

It's not elegant, but this project is 3 days old and will never see production.

# Unsolved Problems
1. Unable to handle more than 2 operands. I didn't have the time to handle the order of operations to the degree
   that I'd find sufficient.
1. The traditional help flag doesn't work here. In order to get argparse to ignore negative input without spending
   a ton of time on it I had to change the prefix character to `~`. You can get the help text to display by executing
   `./fraction-calculator ~~help`.
