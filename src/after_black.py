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

    for filename in args.filenames:
        with open(filename, "r") as file:
            lines = file.readlines()

            for line_no, line in enumerate(lines):
                for test in test_list:
                    if test in line:
                        print(f"{filename} - Line {line_no}: {line}")
                        retval = 1
    return retval


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
