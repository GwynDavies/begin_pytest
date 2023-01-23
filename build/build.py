#!/usr/bin/env python

import sys
import subprocess


def run_it(cmd: str) -> int:
    print("\n")
    print(" .- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -.")
    print("'                                                                                                                 `")
    print(f"- RUNNING COMMAND -> {cmd:92} -")
    print(".                                                                                                                 .")
    print(" `- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'")
    print()

    subprocess.call(cmd, shell=True)


def do_tests():
    run_it('pytest -vv --cov --cov-report term-missing ../lmc/test')


def do_lint():
    run_it('pylint --verbose --disable "C0114,C0115,C0116,R0903,C0301,R0913" --recursive y ../lmc')
    run_it('pylint --verbose --disable "C0114,C0115,C0116,R0903,C0301,R0913" --recursive y ../bin')
    run_it('pylint --verbose --disable "C0114,C0115,C0116,R0903,C0301,R0913" --recursive y .')


def do_format():
    run_it("autopep8 -r -i ../lmc")
    run_it("autopep8 -r -i ../bin")
    run_it("autopep8 -r -i .")


def do_docs():
    run_it("pdoc --o ../docs ../lmc")


def usage(command_line: str):
    print("")
    print(".****************************************************************************************************************.")
    print("'                                                                                                                 '")
    print("| Unable to process command line :                                                                                |")
    print("|                                                                                                                 |")
    print(f'| USAGE:     {"build.py               ... run all below":100} |')
    print(f'|            {"build.py  test         ... run pytest":100} |')
    print(f'|            {"build.py  lint         ... run pylint":100} |')
    print(f'|            {"build.py  format       ... run autopep8":100} |')
    print(f'|            {"build.py  docs         ... run pdoc":100} |')
    print("|                                                                                                                 |")
    print(f"| Received:  {command_line:100} |")
    print(".                                                                                                                 .")
    print("'****************************************************************************************************************'")
    print("\n\n")


def run_with_argument(target, command_line):
    if target.lower() == "test":
        do_tests()
    elif target.lower() == "lint":
        do_lint()
    elif target.lower() == "format":
        do_format()
    elif target.lower() == "docs":
        do_docs()
    else:
        usage(command_line)


def run_all():
    do_tests()
    do_lint()
    do_format()
    do_docs()


def main():
    command_line = " ".join(sys.argv)
    number_arguments = len(sys.argv)

    if number_arguments == 1:
        run_all()
    elif number_arguments == 2:
        target = sys.argv[1]
        run_with_argument(target, command_line)
    else:
        usage(command_line)


if __name__ == "__main__":
    main()
