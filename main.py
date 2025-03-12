#!/usr/bin/env python3
import sys
import math
import os.path

def usage() -> None:
    print(f"Usage: {sys.argv[0]} <file>|<itemcount>")
    pass


def stackable_size(item_name: str) -> int:
    if item_name in (
        # potions
        # filled buckets
        # items with durability
    ):
        return 1
    if item_name in (
        # snowballs
        # empty buckets
        # eggs
        # signs
        # hanging signs
        # ender pearls
    ):
        return 16

    return 64 # Probably correct for most things.


def calc_stack_size(items: int, item_name: str | None = None) -> str:
    stack_size = 64 if item_name is None else stackable_size(item_name)
    shulker_size = 27
    shulker_total = stack_size * shulker_size

    shulkers = math.floor(items / shulker_total)
    loose_items = items % shulker_total

    stacks = math.floor(loose_items / stack_size)
    loose_items = loose_items % stack_size

    return f"{shulkers} SB + {stacks:2} st + {loose_items:2}"

def handle_file(filename: str) -> None:
    data = open(filename, "r").read().splitlines()

    header = data[1].strip('|').strip()
    lines = [[c.strip() for c in l.split('|') if c.strip() != ''] for l in data[5:-3]]

    for l in lines:
        stack_size = calc_stack_size(int(l[1]), l[0])
        if stack_size.startswith('0 SB +'):
            stack_size = stack_size[len('0 SB +'):].strip()
        if stack_size.startswith('0 st +'):
            stack_size = stack_size[len('0 st +'):].strip()

        l.append(stack_size)

    name_length = max([len(l[0]) for l in lines])
    stack_length = max([len(l[4]) for l in lines])

    stack_length += max(len(header) - (name_length + stack_length + 3), 0)

    new_lines = (
        [
            "+-" + "".ljust(len(header), "-") + "-+",
            "| " + header + " |",
            "+-" + "".ljust(name_length, "-") + "-+-" + "".rjust(stack_length, "-") + "-+",
            "| " + "Item".ljust(name_length) + " | " + "Total".rjust(stack_length) + " |",
            "+-" + "".ljust(name_length, "-") + "-+-" + "".rjust(stack_length, "-") + "-+",
        ] +
        [f'| {l[0].ljust(name_length)} | {l[4].rjust(stack_length)} |' for l in lines] +
        [
            "+-" + "".ljust(name_length, "-") + "-+-" + "".rjust(stack_length, "-") + "-+",
            "| " + "Item".ljust(name_length) + " | " + "Total".rjust(stack_length) + " |",
            "+-" + "".ljust(name_length, "-") + "-+-" + "".rjust(stack_length, "-") + "-+",
        ]
    )

    for l in new_lines:
        print(l)


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



