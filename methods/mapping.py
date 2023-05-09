def keyvalue_map(key_type: type, values_list: list) -> dict:
    key_dict = key_type.__dict__.keys()
    return dict(zip(list(key_dict)[2:], list(values_list)))
