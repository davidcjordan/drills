#!/usr/bin/env python3

import os, sys

def print_files_starting_with(prefix="DRL"):
    # Get the list of files in the current directory
    files = sorted(os.listdir('.'))

    # Iterate through each file
    for file in files:
        if file.startswith(prefix):
            try:
                with open(file, 'r') as f:
                    first_line = f.readline().strip()
                    print(f"{file} {first_line}")
            except Exception as e:
                print(f"Error reading file {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prefix = sys.argv[1]
    else:
        prefix = "DRL"

    print_files_starting_with(prefix)
