import json

rate_file = '/Users/fengtang/test/rate_limit.txt'
config_file = '/Users/fengtang/test/test_mitigation.json'

ENABLE_DYNAMIC_RATE_ALLOCATION = 'enable_dynamic_rate_allocation'

def update_rate_limit(mitigations, shaper_id, rate_limit):
    tokens = shaper_id.split("||")
    target_group = tokens[0].strip()
    target = tokens[1].strip()
    shaper = tokens[2].strip()

    print("rate_limit = {}".format(rate_limit))
    if shaper == "default":
        end = shaper
    else:
        end = "named"

    allocated_percentage = float(rate_limit[0].strip())
    timestamp = int(rate_limit[1][1].strip())
    #node = walk_config_tree(mitigations["target_groups"], target_group, target, end)
  
    node = _get_value_for_shaper(mitigations, shaper_id)

    print("node = {}".format(node))

    if node is None:
        return

    if shaper == "default":
        print("rate = {}, location_rate = {}, allocated_percentage = {}".format(node["per_dest_buckets_config"]["rate"], node["per_dest_buckets_config"]["location_rate"], allocated_percentage))
        node["per_dest_buckets_config"]["rate"] = int(node["per_dest_buckets_config"]["location_rate"] * allocated_percentage)
        print("rate = {}".format(node["per_dest_buckets_config"]["rate"]))
    else:
        for item in node:
            if item["name"] == shaper:
                print("rate = {}, location_rate = {}, allocated_percentage = {}".format(item["per_dest_buckets_config"]["rate"], item["per_dest_buckets_config"]["location_rate"], allocated_percentage))
                item["per_dest_buckets_config"]["rate"] = int(item["per_dest_buckets_config"]["location_rate"] * allocated_percentage)
                print("rate = {}".format(item["per_dest_buckets_config"]["rate"]))
                break

    num_of_hosts = get_active_host_count(mitigations["location_state"])
    print("num_of_hosts = ", num_of_hosts)
        
def walk_config_tree(root, target_group, target, shaper):
    print("target_group = {}, target = {}, shaper = {}".format(target_group, target, shaper))
    try:
        node = root[target_group]["targets"][target]["mitigation_config"]["ip_traffic_shaper"]["config"][shaper]
    except:
        node = None
    return node

def get_active_host_count(root):
    count = 0
    try:
        hosts = root["hosts"]
        for key, value in hosts.items():
            if value["current_status"] == "ACTIVE":
                count += 1
        return count;        
    except Exception as e:
        raise Exception("Failed to get host information") from e 

def parse_shaper_name(shaper_name):
    tokens = shaper_name.split("||")
    target_group = tokens[0].strip()
    target = tokens[1].strip()
    shaper = tokens[2].strip()
    return target_group, target, shaper

def _get_value_for_shaper(root, shaper_name):
    target_group, target, shaper = parse_shaper_name(shaper_name)

    if shaper == "default":
        end = shaper
    else:
        end = "named"

    print("target_group = {}, target = {}, shaper = {}".format(target_group, target, shaper))
    #print("_get_value_for_shaper: {}".format(json.dumps(root, indent=4)))

    #print(json.dumps(root, indent=4))

    value = root["target_groups"]["FOO"]["targets"]["DNS"]["mitigation_config"]["ip_traffic_shaper"]["config"]
    print("++++++ value = {}".format(value))

    if ENABLE_DYNAMIC_RATE_ALLOCATION in value:
        print(value[ENABLE_DYNAMIC_RATE_ALLOCATION])



    try:
        node = root["target_groups"][target_group]["targets"][target]["mitigation_config"]["ip_traffic_shaper"]["config"][end]
        print("root[\"target_groups\"][{}][\"targets\"][{}][\"mitigation_config\"][\"ip_traffic_shaper\"][\"config\"][{}] == {}".format(target_group, target, shaper, node))
    except:
        node = None
    
    return node


table = {}
with open(rate_file, 'r') as rate_limit_fp:
    line = rate_limit_fp.readline().strip()
    while line:
        tokens = []
        for token in line.split(','):
            tokens.append(token.strip())
        table[tokens[0]] = tokens[1:]
        line = rate_limit_fp.readline().strip()

with open(config_file, 'r') as config_file_fp:
    mitigations = json.load(config_file_fp)
    
for key, value in table.items():
    update_rate_limit(mitigations, key, value)

