#!/usr/bin/env python
import argparse
import glob
import json
import os
import sys
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=argparse.FileType('r'),  nargs='?', default=sys.stdin)
parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?', default=sys.stdout)
args = parser.parse_args()

contents = args.input_file.read()
filename = args.input_file.name
methodname = filename.replace(".md", "")
dirname = os.path.basename(os.getcwd())

prolog_re = re.compile(".*^## ", re.M|re.S)
contents = prolog_re.sub("## ", contents, 1)
login_required_re = re.compile(r"[*]{2,2}User Login Required:[*]{2,2}\s*([A-Za-z]*).*")
login_required_line = login_required_re.search(contents)
if login_required_line and login_required_line.group(1) == "Yes":
    login_required = True
else:
    login_required = False
contents = login_required_re.sub("", contents, 1)

lines = contents.split("\n")
lastblank = False
in_examples = False
in_description = False
blank_re = re.compile("^\s*$")
example_re = re.compile("^Example ([^ ]*) (call|request)")
url_re = re.compile(r"[*]{2,2}URL:[*]{2,2}\s+`([A-Z]+)\s+[a-z./:]*v1\/([a-z._/-]*)")
summary_re = re.compile(r"###\s+Summary")
args.output_file.write("name: %s\nmethods:\n  - name: %s\n    summary:\n" % (dirname, methodname))
for line in lines:
    write = True
    match = blank_re.match(line)
    if match:
        if not lastblank:
            lastblank = True
        else: 
            write = False
    else:
        lastblank = False
        if summary_re.match(line):
            args.output_file.write("    description: |\n")
            in_description = True
            lastblank = True
            continue
        url = url_re.match(line)
        if url:
            in_description = False
            args.output_file.write("    url: %s\n" % url.group(2))
            if url.group(1) != "GET":
                args.output_file.write("    http-method: %s\n" % url.group(1))
            if login_required:
                args.output_file.write("    login-required: true\n" )
            continue
        else:
            pass
        examplestart = example_re.match(line)
        if examplestart:
            if not in_examples:
                args.output_file.write("    examples:\n")
                in_examples = True
            example_type = examplestart.group(1).lower()
            args.output_file.write("      - platform: %s\n        example: |\n" % ("rest" if (example_type == "curl") else  example_type))
    if write:
        if in_description:
            line = "        " + line
        if in_examples:
            line = "            " + line
        args.output_file.write(line + "\n")

