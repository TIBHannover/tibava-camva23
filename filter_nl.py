import os
import sys
import re
import argparse
import csv


def parse_args():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-i", "--input_path")
    parser.add_argument("-o", "--output_path")
    parser.add_argument("--prefix")
    parser.add_argument("--postfix")
    parser.add_argument("-k", "--key")
    args = parser.parse_args()
    return args


DICT_TYPE = 5
CONCEPT_NAME = 6
LOCALICATION = 7
SUB_DICT_TYPE = 8
DESCR = 9


def main():
    args = parse_args()

    concept_list = []
    with open(args.input_path) as f:
        reader = csv.reader(f)
        for line in reader:
            # if line[DICT_TYPE] == args.key:
            # print(line)
            concept_list.append(
                [line[DICT_TYPE], line[SUB_DICT_TYPE], line[LOCALICATION], line[CONCEPT_NAME], line[DESCR]]
            )

    prefix = args.prefix if args.prefix else ""
    postfix = args.postfix if args.postfix else ""

    with open(args.output_path, "w") as f:
        writer = csv.writer(f)
        for concept in concept_list:
            writer.writerow([x.strip() for x in concept])

    return 0


if __name__ == "__main__":
    sys.exit(main())
