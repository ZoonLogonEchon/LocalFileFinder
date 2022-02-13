import argparse
import os
import re
import sys

def print_match_found(line_num, fpath, match_pos):
    print(f"Match found in file {fpath} in line {line_num + 1} at pos {match_pos}")

def find_local_files(start_dir, fname_regex, search_str_regex):
    if not os.path.isdir(start_dir):
        print(f"${start_dir} is not a directory")
        sys.exit(1)

    for dirpath, _, filenames in os.walk(start_dir):
        relevant_fnames = filter(lambda fname: True if re.search(fname_regex, fname) else False, filenames)
        for relevant_fname in relevant_fnames:
            fpath = os.path.join(dirpath, relevant_fname)
            with open(fpath, "r") as f:
                for idx, line in enumerate(f):
                    match = re.search(search_str_regex, line)
                    if match:
                        print_match_found(idx, fpath, match.pos)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('start_dir', type=str,
                        help='an integer for the accumulator')
    parser.add_argument('fname_regex', type=str,
                        help='regex')
    parser.add_argument('search_str_regex', type=str,
                        help='an integer for the accumulator')

    args = parser.parse_args()
    find_local_files(args.start_dir, args.fname_regex, args.search_str_regex)