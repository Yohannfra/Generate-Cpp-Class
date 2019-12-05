#!/usr/bin/python3

import sys
import os


def get_file_content(fp):
    if os.path.isfile(fp) == False:
        print(f"{fp} : File not found")
        exit(1)
    try:
        f = open(fp, 'r')
        l = f.readlines()
        f.close()
        return l
    except:
        print("Could not open file")
        exit(1)


def get_class_name(lines):
    for l in lines:
        if "class" in l:
            return l.strip().split()[1]
    print("Could not get class name")
    exit(1)


def get_functions(lines):
    functions = []

    for l in lines:
        if '(' in l and ')' in l:
            functions.append(l.strip()[0:-1])
    return functions


def generate_content(functions, class_name, header_name):
    if header_name != "":
        print(f"#include \"{header_name.split('/')[-1]}\"\n")

    for f in functions:
        l = f.split()
        if len(l) >= 2:
            print(f"{l[0]} {class_name}::{' '.join(l[1:])}")
        else:
            print(f"{class_name}::{l[0]}")
        print("{\n\n}\n")


def update_content(functions, class_name, header_name, cpp_file):
    cpp_fc = get_file_content(cpp_file)

    for l in cpp_fc:
        l = l.strip()
        for f in functions:
            k = f.split()
            if len(k) >= 2:
                k = f"{k[0]} {class_name}::{' '.join(k[1:])}"
            else:
                k = f"{class_name}::{k[0]}"
            if k in l:
                functions.remove(f)
    generate_content(functions, class_name, "")


def main(argv):
    len_argv = len(argv)
    if len_argv == 2 or len_argv == 3:
        lines = get_file_content(argv[1])
        class_name = get_class_name(lines)
        functions = get_functions(lines)
        if len(argv) == 2:
            generate_content(functions, class_name, argv[1])
        elif len(argv) == 3:
            update_content(functions, class_name, argv[1], argv[2])
    else:
        print(f"Usage: {argv[0]} hpp_file [cpp_file]")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
