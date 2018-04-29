import json
from queue import *

config_file = '/Users/fengtang/test/test_mitigation.json'

with open(config_file, 'r') as config_file_fp:
    mitigations = json.load(config_file_fp)
    #print(json.dumps(mitigations, indent=4))

def main():
    for shaper in retrieve_shapers(mitigations):
        print(json.dumps(shaper, indent=4))


# traverse the mitigation tree and fetch all shapers
def retrieve_shapers(mitigation):
    root = mitigation["target_groups"]
    queue = Queue(maxsize=0)
    queue.put(root)
    shapers = []
    while not queue.empty():
        node = queue.get()
        if not isinstance(node, dict):
            continue
        for key in node.keys():
            if key == "default":
                shapers.append(node[key])
            elif key == "named":
                for shaper in node[key]:
                    shapers.append(shaper)
            else:
                queue.put(node[key])
    return shapers

if __name__ == "__main__":
    main()
