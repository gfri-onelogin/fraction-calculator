# What Is This?
This repository is a command-line tool that performs basic arithmetic operations on the provided
fractions and produces the result of those operations as a fraction.

## Specifications
* Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
* Operands and operators shall be separated by one or more spaces
* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
* Improper fractions and whole numbers are also allowed as operands
* Negative fractions will be indicated by a '-' directly before the fraction with no spaces

# How Do I Use It?
This repository contains an executable file called `fraction-calculator` that can be downloaded and
run. This file includes all necessary dependencies and *should* be able to run in any *nix-style shell.

# Unsolved Problems
* argparse is weird. Negative numbers are really hard to use here. If any of your inputs start with a `-`,
  it treats it as an option being passed to the parser. One way to get around this is to pass in all inputs
  quoted thusly: `"1/2 - -1/2"`. Note that the negative fraction needs to be second in order to make this work.
  This is unsupported, untested functionality as a simple `split()` is performed on your input in order to
  continue processing. Your mileage may vary.
