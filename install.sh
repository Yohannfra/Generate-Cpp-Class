#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

chmod +x ./gen_cpp_class.py
cp gen_cpp_class.py /usr/bin/gen_cpp_class
