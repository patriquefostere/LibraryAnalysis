import os
import json
import sys

def WriteFile(data):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    path = os.path.join(script_directory, "data.txt")
    with open(path, "w+") as outfile:
        outfile.write(json.dumps(data))
