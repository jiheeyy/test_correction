"""Jihee You Test1 Corrections"""


def num_unique_family(proteins):
    """Input: list of protein strings
    Output: Num of unique family numbers"""
    return len({x.split(".")[0] for x in proteins})


def num_unique_members(proteins):
    """Input: list of protein strings
    Output: Dictionary with key: family name, value: # members"""
    family_dict = {}
    for protein in proteins:
        family_name = protein.split(".")[0]
        try:
            family_dict[family_name] += 1
        except KeyError:
            family_dict[family_name] = 1
    return family_dict


def combined_dict(dict1, dict2):
    """Combine 2 outputs from num_unique_members"""
    final_dict = {}
    final_keys = set(dict1.keys() | dict2.keys())
    for key in final_keys:
        final_dict[key] = (dict1.get(key, 0), dict2.get(key, 0))
    return final_dict
