#!/usr/bin/env python

import sys
from lmc.assembler.assembler import Assembler
from lmc.application.error_fatal import ErrorFatal

if __name__ == '__main__':
    THIS_PROGRAM_NAME = sys.argv[0]

    if len(sys.argv) != 2:
        ErrorFatal.exit_fatal_error(
            f'File name not supplied: USAGE {THIS_PROGRAM_NAME} <filename>.lmcs')

    FILE_NAME = sys.argv[1]

    if not FILE_NAME.endswith('.lmcs'):
        ErrorFatal.exit_fatal_error(
            f'File name does not end with .lmcs - {FILE_NAME} - USAGE {THIS_PROGRAM_NAME} <filename>.lmcs')

    assembler = Assembler()
    assembler.run(FILE_NAME)
