import json


def read_offers(file="top/offers.json"):
    with open(file) as json_file:
        data = json.load(json_file)
        sorted_data = sorted(data['offers'].items(), key=lambda x: x[1]['priority'])
        sorted_data = dict(sorted_data)
        return sorted_data


if __name__ == '__main__':
    r = read_offers("offers.json")
    sorted_x = sorted(r['offers'].items(), key=lambda x: x[1]['priority'])
    sorted_dict = dict(sorted_x)
    print(type(sorted_x))
    print(type(sorted_dict))
    for k,v in sorted_dict.items():
        print(k,v)
