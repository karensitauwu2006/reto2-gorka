import os
import json


users_cvs_route_str = "./users.json"

def fn_read_json(route_str):
    data_list = []

    if not os.path.exists(route_str):
        return data_list

    with open(route_str, "r", encoding="utf-8") as f:
        data_list = json.load(f)

    return data_list


def fn_write_json(route_str, data_list):
    with open(route_str, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)

