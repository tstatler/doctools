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

pseudo_pattern = ".*(@pseudo).*"

# Helper function to convert unicode string to ASCII
def u2a(str):
	if isinstance(str, unicode):
		return str.encode('ascii', 'ignore')
	else:
		return str

def dict_has_non_empty_member(d, member_name):
	return member_name in d and d[member_name] is not None and len(d[member_name]) > 0

def strip_desc(str):
	str_sub = re.sub("\.\.\.$", "", str)
	str_match = re.search("<p>", str_sub)
	if str_match:
		tokens = re.split("<\/p>", str_sub)
		str_sub = tokens[0] + "</p>"
	return str_sub

def to_jsca_type_name(type_test):

	if type_test.startswith("Array"):
		type_test = "Array"
	elif type_test.startswith("Dictionary"):
		type_test = "Object"
	elif type_test.startswith("Titanium"):
		type_test = "Object"
	elif type_test.startswith("Alloy"):
		type_test = "Object"
	return type_test


def parse_doc(doc):
	parsed_doc = {}

	# Parse @since
	since_match = re.search(since_pattern, doc)
	if since_match:
		tokens = since_match.group().split()
		parsed_doc["since"] = { "since": u2a(tokens[1]), "version": "Titanium Mobile SDK"}

	# Parse @platform
	platform_match = re.findall(platform_pattern, doc, 0)
	if platform_match:
		platforms = []
		since_dict = []
		for item in platform_match:
			tokens = item.split()
			platform = {}
			platform["platform"] = u2a(tokens[1])
			platforms.append(platform)
			since_dict.append({
				"since":u2a(tokens[2]),
				"version": "Titanium Mobile SDK - " + pretty_platforms[tokens[1]]
			})
		parsed_doc["userAgents"] = platforms
		parsed_doc["since"] = since_dict

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


	# Parse @pseudo
	pseudo_match = re.search(pseudo_pattern, doc)
	if pseudo_match:
		parsed_doc["pseudo"] = True

	# Anything else is the description
	stripped = re.sub(platform_pattern, '', doc, 0)
	stripped = re.sub(since_pattern, '', stripped, 0)
	stripped = re.sub(pseudo_pattern, '', stripped, 0)
	stripped = re.sub(example_pattern, '', stripped, re.M | re.S)
	stripped = re.sub(r'@description', '', stripped, 0)
	stripped = re.sub(r'^<p>@typestr.*$', '', stripped, 0)
	parsed_doc["description"] = strip_desc(u2a(stripped))

	return parsed_doc



def parse_params(params, tagname):

	new_params = []
	for elem in params:
		new_elem = {}

		if tagname == "event":
			parse_dict = parse_doc(elem["doc"])
			if parse_dict is not None:
				new_elem["description"] = parse_dict["description"] 

		if tagname == "method":
			new_elem["usage"] = "optional" if elem["optional"] else "required"

		new_elem["type"] = to_jsca_type_name(u2a(elem["type"]))
		new_elem["name"] = u2a(elem["name"])
		new_params.append(new_elem)
	return new_params


def parse_members(members):
	new_members = []
	for api in members:
		new_api = {}

		new_api["name"] = u2a(api["name"])

		parse_dict = parse_doc(api["doc"])
		if parse_dict is not None:
			for key in parse_dict.keys():
				new_api[key] = parse_dict[key] 

		if dict_has_non_empty_member(api, "shortDoc"):
			parse_dict = parse_doc(api["shortDoc"])
			new_api["description"] = strip_desc(u2a(parse_dict["description"]))

		if dict_has_non_empty_member(api, "meta"):
			meta = api["meta"]
			if dict_has_non_empty_member(meta, "since"):
				new_api["since"] = { "since": u2a(meta["since"]), "version": "Titanium Mobile SDK"}

		if api["tagname"] == "property":
			new_api["type"] = to_jsca_type_name(u2a(api["type"]))
			new_api["isInternal"] = False
			new_api["isClassProperty"] = True
			new_api["isInstanceProperty"] = False

		if api["tagname"] == "method":
			new_api["isMethod"] = True
			new_api["isConstruction"] = False
			new_api["isInternal"] = False
			new_api["isInstanceProperty"] = True
			new_api["isClassProperty"] = False
			new_api["parameters"] = parse_params(api["params"], api["tagname"])
			if api["return"] is not None:
				returnz = {}
				returnz["type"] = to_jsca_type_name(u2a(api["return"]["type"]))
				if returnz["type"] == "undefined":
					returnz["type"] = "void"
				else:
					parse_dict = parse_doc(api["return"]["doc"])
					if re.sub(r'[^\s]', '', parse_dict["description"]) is not None:
						returnz["description"] = parse_dict["description"]
				new_api["returns"] = returnz

		if api["tagname"] == "event":
			new_api["properties"] = parse_params(api["params"], api["tagname"])

		new_members.append(new_api)
	return new_members


if len(sys.argv) < 3 or re.search("help", sys.argv[1]):
	print "jsduck2json.py <input_file.json> <output_file.json>"
	sys.exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

json_data=open(input_file)
data = json.load(json_data)
import pprint
pprint.pprint(data)
export_types = []
for obj in data:
	if obj["tagname"] == "class":

		new_obj = {}
		new_obj["name"] = u2a(obj["name"])
		if new_obj["name"] == "Alloy.Widget":
			new_obj["name"] = "Widget"
		elif new_obj["name"] == "Alloy.widgets":
			continue

		if re.search("Alloy\.builtins.+", new_obj["name"]):
		#	new_obj["name"] = re.sub("^Alloy\.builtins\.", "", new_obj["name"])
		#elif new_obj["name"] == "Alloy.builtins":
			continue

		parse_dict = parse_doc(obj["doc"])
		if parse_dict is not None:
			for key in parse_dict.keys():
				new_obj[key] = parse_dict[key] 

		if "pseudo" in new_obj and new_obj["pseudo"] is True:
			continue

		if dict_has_non_empty_member(obj, "shortDoc"):
			parse_dict = parse_doc(obj["shortDoc"])
			new_obj["description"] = u2a(parse_dict["description"])

		#new_obj["inherits"] = u2a(obj["extends"]) if obj["extends"] is not None else "Object"
		new_obj["isInternal"] = False
		new_obj["properties"] = parse_members(obj["members"]["property"])
		new_obj["functions"] = parse_members(obj["members"]["method"])
		new_obj["events"] = parse_members(obj["members"]["event"])
		export_types.append(new_obj)
		
json_data.close()

export_data = {}
export_data["types"] = export_types
export_data["version"] = "1.0"

file=open(output_file, 'w')
json.dump(export_data, file, indent=4, separators=(',', ': '))
file.close()
