#!/usr/bin/env python

import argparse
import csv
import os
import re

def load_patterns(file):
    patterns = []
    f = open(file,"r")
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 2:
            patterns.append(row)
    f.close()
    return patterns

def make_symlink(path, dest):
    (dirs, file) = os.path.split(path)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    if not os.path.exists(path):
        os.symlink(dest, path)
        if not args.quiet:
            print("Created symlink from {0} -> {1}".format(path,dest))
    else:
        if not args.quiet:
            print("{0} already exists, skipping".format(path))

def build_symlinks(patterns, in_path, out_path):
    in_path = os.path.abspath(in_path)
    out_path = os.path.abspath(out_path)
    for root, dirs, files in os.walk(in_path):
        for file in files:
            path = os.path.join(root,file)
            abs_path = os.path.abspath(path)
            for pattern in patterns:
                if re.match(pattern[0],path):
                    mod_path = re.sub(pattern[0], pattern[1], path)
                    new_path = os.path.join(out_path, mod_path)
                    new_abs_path = os.path.abspath(new_path)
                    make_symlink(new_abs_path, abs_path)
                    break
                        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate symbolic links according to regular expression based rules")

    parser.add_argument("source", help="Path to scan for files")
    parser.add_argument("destination", help="Directory to create symlinks in")
    parser.add_argument("match", help="Regular expression to scan the target path for")
    parser.add_argument("substitution", help="Regular expression to create a file with")
    parser.add_argument("-p", "--patterns", help="Create symlinks quietly")
    parser.add_argument("-q", "--quiet", action="store_true", help="Create symlinks quietly")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

    global args
    args = parser.parse_args()

    patterns = []
    if args.patterns:
        patterns = load_patterns(args.patterns)
    else:
        patterns = [[args.match,args.substitution]]

    build_symlinks(patterns, args.source, args.destination)
