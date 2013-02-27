#!/usr/bin/env python
import subprocess
import html2text
baseurl="http://cloud.appcelerator.com/docs/api/v1/acls/"
for method in [ "create", "update", "delete", "show", "add", "remove", "check" ]:
    html2text_args =  "html2text.py " +baseurl+method +  " > " + method+".md"
    print html2text_args
    subprocess.call(html2text_args, shell=True)
    subprocess.call([ "./hack.py", method+".md", method+".yml" ])
