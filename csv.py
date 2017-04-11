import csv
import json
from collections import OrderedDict

reduced_item_fun = OrderedDict()
processed_data = []


# Convert to string
def to_string(s):
    try:
        return str(s)
    except:
        # Change the encoding type if needed
        return s.encode('utf-8')


def reduce_item(key, value):
    """
    | **@author:** Thebzeera V
    |
    |
    :param key: Keys of dictionary
    :param value: Value of dictionary
    :return:
    """
    # Reduction  condition 1
    if type(value) is list:
        reduce_item(key + "_start", value[0])
        reduce_item(key + "_end", value[-1])

    # Reduction condition 2
    elif type(value) is OrderedDict:
        sub_keys = value.keys()

        for sub_key in sub_keys:
            reduce_item(key + "_" + to_string(sub_key), value[sub_key])

    # Reduction condition 3
    else:
        reduced_item_fun[to_string(key)] = to_string(value)

    return reduced_item_fun


def parser(meta_parsed, config_parsed):
    """
    | **@author:** Thebzeera V
    |
    |
    :param meta_parsed: Meta json
    :param config_parsed: rztdl config json
    :return: Header length
    """
    header = []
    header.append("ID")

    config_meta = config_parsed['metadata_config']
    sub_key = config_meta.keys()
    key_meta = meta_parsed.keys()

    try:
        keys = int(max(key_meta))
        for sub_key_meta in key_meta:
            for key in sub_key:

                if to_string(config_meta[key]) == "True":
                    reduced_item_fun = reduce_item(key, meta_parsed[sub_key_meta][key])

            reduced_item_fun["ID"] = to_string(sub_key_meta)
            processed_data.append(reduced_item_fun.copy())
    except:
        for key in sub_key:
            if to_string(config_meta[key]) == "True":
                reduced_item_fun = reduce_item(key, meta_parsed[key])

        reduced_item_fun["ID"] = "0"
        processed_data.append(reduced_item_fun.copy())

    for key in reduced_item_fun.keys():
        header.append(key)
    # header.remove(-1)
    header = header[:-1]
    with open(csv_file_path, 'w') as f:
        writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)

    return len(header)


if __name__ == "__main__":
    json_file_path = "/home/thebzeera/PycharmProjects/new/sample.json"
    csv_file_path = "/home/thebzeera/PycharmProjects/new/trueJsonToCsv.csv"
    true_json_path = "/home/thebzeera/PycharmProjects/new/truejson.json"

    # Open the file
    fp = open(json_file_path, 'r')
    json_value = fp.read()
    # Load json file
    inputJsonFile = json.loads(json_value, object_pairs_hook=OrderedDict)

    # Open the file
    tp = open(true_json_path, 'r')
    true_json_value = tp.read()
    # Load  json file
    json_config = json.loads(true_json_value, object_pairs_hook=OrderedDict)

    length = parser(inputJsonFile, json_config)
    print("Just completed writing csv file with %d columns" % length)