def num_unique_family(proteins):
    """Input: list of protein strings
    Output: Num of unique family numbers"""
    return len(set([x.split(".")[0] for x in proteins]))
  
def num_unique_members(proteins):
    family_dict = {}
    for p in proteins:
        family_name = p.split(".")[0]
        try:
            family_dict[family_name] += 1
        except:
            family_dict[family_name] = 1
    return family_dict
  
def combined_dict(dict1, dict2):
    final_dict = {}
    final_keys = set(dict1.keys() | dict2.keys())
    for key in final_keys:
        final_dict[key] = (dict1.get(key, 0), dict2.get(key, 0))
    return final_dict
