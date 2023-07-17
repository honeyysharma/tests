import os
import re


def strip(value):
    return re.sub(r'\s', '', value)

def parse_config(config_file):
    data = {}
    with open(config_file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            content = line.split("=", 1)
            if len(content) < 2:
                continue
            key, value = strip(content[0]), strip(content[1])
            data[key] = value
    return data


if __name__ == "__main__":
    import os
    config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_files.txt")
    d = parse_config(config)
    print(d)
