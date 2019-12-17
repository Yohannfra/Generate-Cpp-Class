#!/usr/bin/python3

import sys
import os


class GenCppClass:
    def __init__(self):
        len_argv = len(sys.argv)
        if len_argv == 2 or len_argv == 3:
            self.lines = self.get_file_content(sys.argv[1])
            if not self.is_c_file(sys.argv[1]):
                self.class_name = self.get_class_name()
            else:
                self.class_name = None
            self.functions = self.get_functions()
            self.variables = self.get_variables()
            if len_argv == 2:
                self.generate_content(sys.argv[1])
            elif len_argv == 3:
                self.update_content(sys.argv[1], sys.argv[2])
        else:
            print(f"Usage: {sys.argv[0]} hpp_file [cpp_file]")
            exit(1)

    def is_c_file(self, fp):
        if ".h" in fp and ".hpp" not in fp:
            return True
        return False

    def get_file_content(self, fp):
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

    def get_class_name(self):
        for l in self.lines:
            if "class" in l:
                return l.strip().split()[1]
        print("Could not get class name")
        exit(1)

    def get_functions(self):
        functions = []

        for l in self.lines:
            if '(' in l and ')' in l and "typedef" not in l:
                functions.append(l.strip()[0:-1])
        return functions

    def get_variables(self):
        variables = []
        for l in self.lines:
            if ';' in l and '(' not in l and len(l.split()) > 1:
                variables.append(l.strip()[0:-1])
        return variables

    def generate_content(self, header_name):
        if header_name != "":
            print(f"#include \"{header_name.split('/')[-1]}\"\n")

        for f in self.functions:
            l = f.split()
            function_name = ' '.join(l[1:])
            if self.class_name != None:
                if len(l) >= 2:
                        print(f"{l[0]} {self.class_name}::{function_name}")
                else:
                    print(f"{self.class_name}::{l[0]}")
                print('{')
                if 'get' in function_name or 'Get' in function_name:
                    for v in self.variables:
                        v = v.split()
                        if v[1] in function_name and v[0] == l[0]:
                            print(f'    return {v[1]};')
                else:
                    print("")
                print("}\n")
            else:
                print(f"{l[0]} {function_name}")
                print('{\n\n}\n')

    def update_content(self, header_name, cpp_file):
        cpp_fc = self.get_file_content(cpp_file)

        for l in cpp_fc:
            l = l.strip()
            for f in self.functions:
                k = f.split()
                if len(k) >= 2:
                    k = f"{k[0]} {self.class_name}::{' '.join(k[1:])}"
                else:
                    k = f"{self.class_name}::{k[0]}"
                if k in l:
                    self.functions.remove(f)
        self.generate_content("")

if __name__ == "__main__":
    GenCppClass()
