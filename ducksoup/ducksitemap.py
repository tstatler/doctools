#! /usr/bin/env python
import argparse
import glob
import json
import os
import sys
import re

jsonstart_re = re.compile("^Ext.data.JsonP\[\'[^']*\'\][^(]*\(")
jsonend_re = re.compile("\);[ \t]*$")

class FileWriter:
    def __init__(self, outfile, baseurl=""):
        self.file = outfile
        if baseurl and not baseurl.endswith("/"):
            baseurl = baseurl + "/"
        self.baseurl = baseurl

    def write(self, url):
        self.file.write(self.baseurl + url.replace("#!", "?_escaped_fragment_="))

    def close(self):
        self.file.close()

def jsonp_decode(filename):
    file=open(filename)
    if not file:
        print "Couldn't open file ?!!?!?"
    contents=file.read()
    if not contents:
        print "No contents!"
    jsonp = jsonstart_re.sub("", contents, 1)
    jsonp = jsonend_re.sub("", jsonp, 1)
    try:
        return json.loads(jsonp)
    except:
        print "Failed to parse %s\n" % ( filename )
    finally:
        file.close()

def process_classes(dir, outfile):
    files = glob.glob(os.path.join(dir, "*.js"))
    for file in files:
        classobj = jsonp_decode(file)
        if classobj and "name" in classobj:
            outfile.write(("#!/api/%s\n" % (classobj["name"])))
            if "members" in classobj:
                members = classobj["members"]
                for type in [ "property", "method", "event" ]:
                    if type in members:
                        for item in members[type]:
                            if "name" in item and len(item["name"]) > 0:
                                outfile.write("#!/api/%s-%s-%s\n" % (classobj["name"], type, item["name"]))
                            else:
                                print "Error: class %s -- found %s with no name." % (classobj["name"], type)
        else:
            print "No contents for class or no classname in file: %s\n" % file
        if classobj and "html" in classobj:
            try:
                classfilename = classobj["name"] + ".html"
                classfile = open(classfilename, "w")
                classfile.write(classobj["html"])
            except:
                print "Error writing file %s" % classfilename
            finally:
                classfile.close()

    
def process_guides(guidesdir, outfile):
    os.chdir(guidesdir)
    print "Guides dir is: " + guidesdir
    dirs = filter(os.path.isdir, os.listdir("."))
    print "Processing guides, dirs is: %s" % dirs
    for dir in dirs:
        guide = jsonp_decode(os.path.join(dir, "README.js"))
        if guide:
            outfile.write("#!/guide/%s\n" % (dir))
        else:
            print "No contents for guide %s\n" % dir

cwd = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('--base_url', '-b', default="")
parser.add_argument('input_dir', nargs='?', default=cwd)
parser.add_argument('output_dir', nargs='?', default=cwd)
args = parser.parse_args()

if not os.path.isdir(args.input_dir):
    print "Error: not a directory: %s" ( args.input_dir )
    exit(1)

if os.path.isdir(args.output_dir):
    outfile = FileWriter(open(os.path.join(args.output_dir, "sitemap.ugly"), "w"), args.base_url)
else:
    print "Error: not a directory: %s" ( args.output_dir )
    exit(1)

classdir = os.path.join(args.input_dir, "output")
if os.path.isdir(classdir):
    process_classes(classdir, outfile)

guidesdir = os.path.join(args.input_dir, "guides")
if os.path.isdir(guidesdir):
    process_guides(guidesdir, outfile)

outfile.close()
