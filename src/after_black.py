from __future__ import annotations

import argparse
import sys
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0

    test_list = [
        '" "',
        '" f"',
        '" r"',
        '" f\'',
        '" r\'',
        '" \'',
        "' '",
        "' f'",
        "' r'",
        "' f\"",
        "' r\"",
        "' \"",
    ]

    potential_issues = 0

    for filename in args.filenames:
        with open(filename, "r") as file:
            lines = file.readlines()

            for line_no, line in enumerate(lines):
                for test in test_list:
                    if test in line:
                        position = line.index(test)

                        if (
                            # for blah = " " + blah situations
                            line[position+3:].lstrip().startswith("+") or
                            # for replace("", " ") situations
                            line[position+3:].lstrip().startswith(")") or
                            # for replace(" ", "_") situations
                            line[position-1] == "("
                        ):
                            pass
                        else:
                            potential_issues += 1
                            print(f"{filename} - Line {line_no+1} (pos: {position}): {line.lstrip()}".rstrip())
                            retval = 1

    return retval


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
