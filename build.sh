#!/bin/sh

pyinstaller src/main.py -F -n fraction-calculator && cp dist/fraction-calculator . && rm -rf dist

[[ $(./fraction-calculator 1/2 + 1/2) == "1" ]] && echo "1/2 + 1/2 == 1"
[[ $(./fraction-calculator 1/2 - 1/2) == "0" ]] && echo "1/2 - 1/2 == 0"
[[ $(./fraction-calculator 1/2 * 1/2) == "1/4" ]] && echo "1/2 * 1/2 == 1/4"
[[ $(./fraction-calculator 1/2 / 1/2) == "1" ]] && echo "1/2 / 1/2 == 1"
