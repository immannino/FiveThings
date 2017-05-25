# A script to read specially formatted text and convert it to json. 
# Written to convert my text files to json to add to my firebase DB.

import re
import json

sample_string = '''
'''


output_json = {}

p1 = re.compile('\d{2}\/\d{2}\/\d{2}', flags=re.DOTALL)
results = p1.findall(sample_string)

for i in range(0, len(results)-1):
    things_pattern = "%s(.*?)%s" % (results[i].replace("/", "\/"), results[i+1].replace("/", "\/"))
    output_json[results[i]] = []
    notes = re.findall(things_pattern, sample_string, re.DOTALL)[0]
    for note in notes.split("\n"):
        output_json[results[i]].append(note[1:])
    while "" in output_json[results[i]]:
        output_json[results[i]].remove("");

print json.dumps(output_json, indent=4, sort_keys=True)

text_file = open("Output.txt", "w")
text_file.write(json.dumps(output_json, indent=4, sort_keys=True))
text_file.close()