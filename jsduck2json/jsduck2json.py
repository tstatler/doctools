import json, re, sys

since_pattern = "@since [0-9\.]+"

platform_pattern = ".*(@platform .+ [0-9\.]+).*"
pretty_platforms = {
	"android":"Android",
	"blackberry":"BlackBerry",
	"iphone":"iPhone",
	"ipad":"iPad",
	"mobileweb":"Mobile Web",
	"tizen":"Tizen"
}

example_pattern = ".*(<h3>Examples<\/h3>.*)"

# Helper function to convert unicode string to ASCII
def u2a(str):
	if isinstance(str, unicode):
		return str.encode('ascii', 'ignore')
	else:
		return str

def parse_doc(doc):
	parsed_doc = {}

	# Parse @since
	since_match = re.search(since_pattern, doc)
	if since_match:
		tokens = since_match.group().split()
		parsed_doc["since"] = u2a(tokens[1])

	# Parse @platform
	platform_match = re.findall(platform_pattern, doc, 0)
	if platform_match:
		platforms = []
		for item in platform_match:
			tokens = item.split()
			platform = {}
			platform["pretty_name"] = u2a(pretty_platforms[tokens[1]])
			platform["since"] = u2a(tokens[2])
			platform["name"] = u2a(tokens[1])
			platforms.append(platform)
		parsed_doc["platforms"] = platforms

	# Parse examples
	example_match = re.search(example_pattern, doc, re.M | re.S)
	if example_match:
		examples = []
		tokens = re.split(r'<\/?h4>', example_match.group())
		x = 1
		while True:
			example = {
				"code":u2a(tokens[x + 1]),
				"description":u2a(tokens[x])
			}
			examples.append(example)
			x = x + 2
			if x + 1 > len(tokens):
				break
		parsed_doc["examples"] = examples

	# Anything else is the description
	stripped = re.sub(platform_pattern, '', doc, 0)
	stripped = re.sub(since_pattern, '', stripped, 0)
	stripped = re.sub(example_pattern, '', stripped, re.M | re.S)
	stripped = re.sub(r'@description', '', stripped, 0)
	stripped = re.sub(r'^<p>@typestr.*$', '', stripped, 0)
	parsed_doc["description"] = u2a(stripped)

	return parsed_doc



def parse_params(params, api_name, tagname):
	suffix = ""
	if tagname == "method":
		suffix = "-param"
	if tagname == "event":
		suffix = "-callback-property"

	new_params = []
	for elem in params:
		new_elem = {}
		new_elem["deprecated"] = u2a(elem["deprecated"])
		new_elem["filename"] = u2a(api_name + "." + elem["name"] + suffix)

		parse_dict = parse_doc(elem["doc"])
		if parse_dict is not None:
			for key in parse_dict.keys():
				new_elem[key] = parse_dict[key] 

		if tagname == "method":
			new_elem["optional"] = elem["optional"]

		new_elem["type"] = u2a(elem["type"])
		new_elem["name"] = u2a(elem["name"])
		new_params.append(new_elem)
	return new_params


def parse_members(members):
	new_members = []
	for api in members:
		new_api = {}
		new_api["filename"] = u2a(api["owner"] + "." + api["name"] + "-" + api["tagname"])
		new_api["filename"] = u2a(new_api["filename"])

		parse_dict = parse_doc(api["doc"])
		if parse_dict is not None:
			for key in parse_dict.keys():
				new_api[key] = parse_dict[key] 

		if api["tagname"] == "property":
			new_api["type"] = u2a(api["type"])
			new_api["default"] = u2a(api["default"])

		if api["tagname"] == "method":
			new_api["parameters"] = parse_params(api["params"], new_api["filename"], api["tagname"])
			if api["return"] is not None:
				returnz = {}
				returnz["type"] = u2a(api["return"]["type"])
				if returnz["type"] == "undefined":
					returnz["type"] = "void"
				else:
					parse_dict = parse_doc(api["return"]["doc"])
					if re.sub(r'[^\s]', '', parse_dict["description"]) is not None:
						returnz["summary"] = parse_dict["description"]
				new_api["returns"] = returnz

		if api["tagname"] == "event":
			new_api["properties"] = parse_params(api["params"], api["owner"] + "." + api["name"], api["tagname"])

		new_api["name"] = u2a(api["name"])

		new_members.append(new_api)
	return new_members


if len(sys.argv) < 3 or re.search("help", sys.argv[1]):
	print "jsduck2json.py <input_file.json> <output_file.json>"
	sys.exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

json_data=open(input_file)
data = json.load(json_data)
export_data = {}
for obj in data:
	if obj["tagname"] == "class":
		new_obj = {}
		new_obj["name"] = u2a(obj["name"])

		new_obj["filename"] = u2a(obj["name"] + "-object")

		parse_dict = parse_doc(obj["doc"])
		if parse_dict is not None:
			for key in parse_dict.keys():
				new_obj[key] = parse_dict[key] 

		new_obj["extends"] = u2a(obj["extends"])
		new_obj["properties"] = parse_members(obj["members"]["property"])
		new_obj["method"] = parse_members(obj["members"]["method"])
		new_obj["events"] = parse_members(obj["members"]["event"])
		export_data[new_obj["name"]] = new_obj
		
json_data.close()

file=open(output_file, 'w')
json.dump(export_data, file, indent=4, separators=(',', ': '))
file.close()
