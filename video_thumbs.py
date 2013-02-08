#!/usr/bin/env python
#
# Copyright (c) 2012 Appcelerator, Inc. All Rights Reserved.
# Licensed under the Apache Public License (version 2)

import json
import pycurl
import StringIO
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="verbose output")
parser.add_option("-i", "--input", dest="input_file", default='videos.json', help="Input file")
parser.add_option("-o", "--output", dest="output_file", default='video_thumbs.json', help="Output file")

(options, args) = parser.parse_args()

try: 
	video_list_file = open(options.input_file, 'r')
except:
	print ('Failed to open input file: %s' % options.input_file)
	exit(1)

try: 
	result_file = open(options.output_file, 'w')
except:
	print ('Failed to open output file: %s' % options.output_file)
	exit(1)

try:
	video_list_json = video_list_file.read()
except:
	print ('Failed to read source file')
	exit(1)
finally:
	video_list_file.close()
	
video_list = json.loads(video_list_json)

for ii in range(len(video_list)):
	chapter = video_list[ii]
	if (options.verbose):
		print ('Processing chapter ' + chapter['title'] + '...')
	
	for jj in range(len(chapter['items'])):
		video = chapter['items'][jj]
		if (options.verbose):
			print ('\tFetching '+video['title'] + '...'),
		url = str("http://vimeo.com/api/v2/video/" + video['id'] + ".json")
		try:
			request = pycurl.Curl()
			request.setopt(pycurl.URL, str(url))
			response = StringIO.StringIO()
			request.setopt(pycurl.WRITEFUNCTION, response.write)
			request.perform()
			video_info = json.loads(response.getvalue())
			if (options.verbose):
				print (video_info[0]['thumbnail_small']),
			video_list[ii]['items'][jj]['thumb'] = video_info[0]['thumbnail_small']
			if (options.verbose):
				print ('OK')
		except pycurl.error as e:
			if (options.verbose):
				print (e[1])
			exit(1)
		finally:
			request.close()

try:
	result_file.write(json.dumps(video_list, indent=2))
except:
	print ('Failed to write results to %s' % options.output_file)
	exit(1)
finally:
	result_file.close()
