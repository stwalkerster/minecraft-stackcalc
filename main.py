#!/usr/bin/env python3
import sys
import math
import os.path

def usage() -> None:
    print(f"Usage: {sys.argv[0]} <file>|<itemcount>")
    pass


def calc_stack_size(items: int) -> str:
    stack_size = 64
    shulker_size = 27
    shulker_total = stack_size * shulker_size

    shulkers = math.floor(items / shulker_total)
    loose_items = items % shulker_total

    stacks = math.floor(loose_items / stack_size)
    loose_items = loose_items % stack_size

    return f"{shulkers} SB + {stacks:2} st + {loose_items:2}"

def handle_file(filename: str) -> None:
    data = open(filename, "r").read().splitlines()
    pass


def main() -> int:
    if len(sys.argv) != 2:
        usage()
        return 1

    if sys.argv[1].isdigit():
        print(calc_stack_size(int(sys.argv[1])))
        return 0

    if os.path.exists(sys.argv[1]):
        handle_file(sys.argv[1])
        return 0

    usage()
    return 1

if __name__ == "__main__":
    main()



