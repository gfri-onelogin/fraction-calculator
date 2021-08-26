#!/bin/sh

pyinstaller src/main.py -F -n fraction-calculator && cp dist/fraction-calculator . && rm -rf dist && ./fraction-calculator 1 + 1/2
