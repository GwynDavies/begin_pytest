#!/usr/bin/env python
import os
from time import sleep

# define our clear function


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
        _ = os.system('clear')
        print()


class Program:
    def add_two_numbers(self):
        self._run_program('add_two_numbers')

    def count_down(self):
        self._run_program('count_down')

    def print_self(self):
        self._run_program('print_self')

    def square_number(self):
        self._run_program('square_number')

    def subtract_two_numbers(self):
        self._run_program('subtract_two_numbers')

    def exiting(self):
        print('Exiting ...')
        sleep(3)
        clear()

    def _run_program(self, name):
        clear()
        print("\n Assemble ... ")
        os.system(f'python ./assembler.py ./programs/{name}.lmcs')
        sleep(3)
        clear()
        print("\n Run on computer ... ")
        os.system(f'python ./computer.py ./programs/{name}.lmcb')
        sleep(3)
        clear()


def main():
    program = Program()

    ans = True
    while ans:
        clear()

        print("""

+---------------------------+
| Assemble and run programs |
+---------------------------+


    1. Program to add two numbers

    2. Program to countdown

    3. Program to print self

    4. Program to square a number (enter 0 to stop)

    5. Program to subtract 2 numbers

    q. Quit     

        """)
        ans = None
        ans = input("What would you like to do? ")

        if ans == "1":
            program.add_two_numbers()
        elif ans == "2":
            program.count_down()
        elif ans == "3":
            program.print_self()
        elif ans == "4":
            program.square_number()
        elif ans == "5":
            program.subtract_two_numbers()
        elif ans == "q":
            program.exiting()
            ans = None
        else:
            print("\n Not Valid Choice Try again")
            sleep(3)


if __name__ == '__main__':
    main()
