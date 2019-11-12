#!/usr/bin/python


with open ("testfile.txt", "rb") as file:
    data = file.read()

for i in data:
    print format(ord(i), 'b'),
