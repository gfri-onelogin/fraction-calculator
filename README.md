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
Start by cloning the repository to your local machine:
```
git clone https://github.com/gfri-onelogin/fraction-calculator.git
```

There's 2 ways to use this calculator: an executable and using the run script

## Executable
This repository contains an executable file called [`fraction-calculator`](fraction-calculator)
that can be downloaded and run. This file includes all necessary dependencies and *should*
be able to run in any *nix-style shell.

```
./fraction-calculator 9/2 - -1_3/4
6_1/4
```

### MacOS Executable Issues
If you decide to download the executable on its own, MacOS is going to tell you that I'm
distributing malware. Don't believe them! It's safe! 😉

To add the file to your security exceptions, open Finder, navigate to the file  and ctrl+click
the file and click Open. You'll be asked if you actually want to use it.

You'll also need to ensure that it's executable:
```
chmod 755 /path/to/where/you/downloaded/fraction-calculator
```

Note: It's way easier to just [clone the repo](#how-do-i-use-it).

## Run Script
Using the run script just abstracts the python command to run a module away from the user. This
is not the preferred method of testing the app because I don't know what version of python you're
rocking or if you have all the required dependencies.

```
./run.sh
```

# Testing
Running the full test suite is painful as one of the tests runs the generated executable for
something like 1600 test cases. It's slow. Go get a coffee or a beer. We're approaching fall,
a medium ale might be appropriate (why do we only get red ales in the spring???). Or if you
like something hoppier, I'm currently digging Elysian's Space Dust. If you're in the Mountlake
Terrace area, check out the menu at [Hemlock State](https://www.hemlockstate.com). I'm a little
disappointed that I'm going to have to wait for their barrel-aged Brew Tang Clan. It's delicious
but definitely more appropriate to colder weather (IMO).

## You Really Want To Run The Tests
If you must, you'll need to ensure that you've updated the executable by running `./build.sh`, and
that pytest is installed on your machine. Then run:
```
pytest tests/test_*
```

It's not elegant, but this project isn't meant for production.

# Building An Updated Executable
I decided to use [`pyinstaller`](https://www.pyinstaller.org) because it's really easy to use
and I don't need all the configurability and features of the more complex utilities that will
package things up in an executable (looking at you [pyoxidizer](https://pyoxidizer.readthedocs.io/en/stable/)).

In order to build using `pyinstaller`, you'll need to install it. Follow their directions, or
just `pip install pyinstaller`.

From there, you can run `./build.sh` from the root of the repo or `pyinstaller src/__main__.py`.
See the [pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html#options) for available options.

# Unsolved Problems
1. Unable to handle more than 2 operands. I didn't have the time to handle the order of operations
   to the degree that I'd find sufficient.
1. The traditional help flag doesn't work here. In order to get argparse to ignore negative input
   without spending a ton of time on it I had to change the prefix character to `~`. You can get
   the help text to display by executing `./fraction-calculator ~~help` or `./run.sh ~~help`
