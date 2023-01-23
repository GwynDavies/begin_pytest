#!/usr/bin/env python

import sys
from lmc.computer.computer import Computer
from lmc.application.error_fatal import ErrorFatal

if __name__ == '__main__':
    THIS_PROGRAM_NAME = sys.argv[0]

    if len(sys.argv) != 2:
        ErrorFatal.exit_fatal_error(
            f'File name not supplied: USAGE {THIS_PROGRAM_NAME} <filename>.lmcb')

    FILE_NAME = sys.argv[1]

    if not FILE_NAME.endswith('.lmcb'):
        ErrorFatal.exit_fatal_error(
            f'File name does not end with .lmcs - {FILE_NAME} - USAGE {THIS_PROGRAM_NAME} <filename>.lmcb')

    computer = Computer()
    computer.run(FILE_NAME)
