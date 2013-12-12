#!/usr/bin/env python
#
# Copyright (c) 2013 Appcelerator, Inc. All Rights Reserved.
# Licensed under the Apache Public License (version 2)

import os, shutil, sys, optparse 
from xml.dom import minidom, getDOMImplementation

def copy_node_html(node, basedir, destdir):
	if node.getAttribute('href').find('#') !=-1:
		return
	filename = node.getAttribute('href')
	outpath = os.path.join(destdir, filename)
	if os.path.exists(outpath):
		print "Warning: copy_node_html: Overwriting file: %s" % filename
		return
	shutil.copyfile(os.path.join(basedir, filename), outpath)
	for child_node in node.childNodes:
		if child_node.nodeType == 1 and child_node.hasAttribute('href'): 
			copy_node_html(child_node, basedir, destdir)

# Recursively copy image (and css) directories, throwing an error if we encounter
# any duplicate paths.
def copy_resources(src, dst):
	if not os.path.isdir(src):
		return
	names = os.listdir(src)
	if not os.path.exists(dst):
		os.makedirs(dst)
	errors = []
	for name in names:
		srcname = os.path.join(src, name)
		dstname = os.path.join(dst, name)
		try:
			if os.path.isdir(srcname):
				copy_resources(srcname, dstname)
			elif os.path.exists(dstname):
				print "ERROR: copy_resources: duplicate path: %s" % dstname
			else:
				shutil.copyfile(srcname, dstname)
		except Exception as err:
			print str(err)
			exit(1)

parser = optparse.OptionParser()
parser.add_option("-i", "--input", dest="input",
	help="input dir -- base guides ", metavar="FILE")
parser.add_option("-a", "--addon", dest="addon",
	help="input dir -- enterprise addon guides", metavar="FILE")
parser.add_option("-o", "--output", dest="output",
	help="output", metavar="FILE")
(options, args) = parser.parse_args()
if options.output is None or options.input is None or options.addon is None:
	print "please provide --input and --output and --addon "
	exit(1)

main_guides = minidom.parse(options.input) # parse an XML file by name
addon_guides = minidom.parse(options.addon)
impl = getDOMImplementation()
output_guides = impl.createDocument(None, "toc", None)

dest = os.path.join(options.output)

try:
	shutil.rmtree(dest)
except:
	print "Error removing output directory %s." % dest

try:
	os.makedirs(dest)
except:
	print "Error creating output directory %s." % dest

top_level_nodes = [] 
studio_nodes = []

for node in addon_guides.documentElement.childNodes:
	if node.nodeType != 1:
		continue
	if node.getAttribute('label') == 'Enterprise Features':
		studio_nodes.append(node)
	elif node.getAttribute('label') != 'Quick Start':
		top_level_nodes.append(node)
	copy_node_html(node, os.path.dirname(options.addon), dest)

for node in main_guides.documentElement.childNodes:
	if node.nodeType != 1:
		continue
	# Copy HTML before manipulating the DOM -- addon guides are 
	# already copied
	copy_node_html(node, os.path.dirname(options.input), dest)
	if node.getAttribute('label') == 'Studio':
		for new_node in top_level_nodes:
			output_guides.documentElement.appendChild(new_node)
		for child_node in node.childNodes:
			if child_node.nodeType != 1:
				continue
			if child_node.getAttribute('label') == 'Titanium Development':
				for new_node in studio_nodes:
					if child_node.nextSibling:
						node.insertBefore(new_node, child_node.nextSibling)
					else:
						node.appendChild(new_node)
				break
		output_guides.documentElement.appendChild(node)
	else:
		output_guides.documentElement.appendChild(node)

for dir in [ os.path.dirname(options.input), os.path.dirname(options.addon) ]:
	for subdir in [ "images", "attachments", "css" ]:
		copy_resources(os.path.join(dir, subdir), os.path.join(dest, subdir))

# Write merged toc.xml
f = open(os.path.join(dest, 'toc.xml'), 'w')
f.write(output_guides.toxml().encode('ascii', 'xmlcharrefreplace'))
f.close()
