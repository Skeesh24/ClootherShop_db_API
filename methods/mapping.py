from methods.logging import toDesktop


def keyvalue_map(keys: list, values_list: list) -> dict:
    key_dict = list(filter(lambda x: not "_" in x, keys))
    return dict(zip(key_dict, values_list))
