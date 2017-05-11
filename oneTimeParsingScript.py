# coding=utf-8

import re
import json

sample_string = '''
01/01/17
-thing one
-thing two
-thing three
-thing four
-thing five


01/02/17
-thing 1
-thing 2
-thing 3
-thing 4
-thing 5


01/04/17
-thing i
-thing ii
-thing iii
-thing iv
-thing v


01/06/17
-thing 9
-thing 8
-thing 7
-thing 6
-thing 5




01/08/17
-thing 
-thing 
-thing 
-thing 
-thing 


01/09/17
'''


output_json = {}

p1 = re.compile('\d{2}\/\d{2}\/\d{2}', flags=re.DOTALL)
results = p1.findall(sample_string)

for i in range(0, len(results)-1):
    things_pattern = "%s(.*?)%s" % (results[i].replace("/", "\/"), results[i+1].replace("/", "\/"))
    output_json[results[i]] = []
    notes = re.findall(things_pattern, sample_string, re.DOTALL)[0]
    for note in notes.split("\n"):
        output_json[results[i]].append(note[1:].capitalize())
    while "" in output_json[results[i]]:
        output_json[results[i]].remove("");

print json.dumps(output_json, indent=4, sort_keys=True)

text_file = open("Output.txt", "w")
text_file.write(json.dumps(output_json, indent=4, sort_keys=True))
text_file.close()