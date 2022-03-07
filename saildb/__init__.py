def run_type(objtype):
    return {"i": int, "f": float, "s": str, "d": dict, "b": "BOOL"}[objtype]

def find_type(object):
    return {int: "i", float: "f", str: "s", dict: "d", bool: "b"}[object]

def parse(string : str):
    contents = string.split(":")
    mapping = int(contents[0])
    directive = str(contents[1])
    objtype = str(contents[2])
    result = contents[3]
    pass_through = run_type(objtype)
    return mapping, directive, pass_through, result

def load(data : str):
    export = {} # Exported Content
    mappings = {1: []}
    for i in data.splitlines():
        mapping, directive, pass_through, result = parse(i)

        level = export
        if mapping != 1:
            for i in mappings[mapping]:
                level = level[i]

        if pass_through == dict:
            level[directive] = {}
            mappings[int(result)] = mappings[mapping][:] # Creates a unlinked object
            mappings[int(result)].append(directive)
        elif pass_through == "BOOL":
            if result == "True":
                level[directive] = True
            else:
                level[directive] = False
        else:
            level[directive] = pass_through(result)

    return export

def dump(data, deep = 1):
    product = ""
    for i in data:
        current = data[i]
        if type(current) == list:
            new = {}
            for l, d in enumerate(current):
                new[l] = d
            current = new
        if type(current) == dict:
            product += f"{deep}:{i}:{find_type(type(current))}:{str(deep+1)}\n"
            product += dump(current, deep=deep+1)
        else:
            product += f"{deep}:{i}:{find_type(type(current))}:{str(current)}\n"
    if deep!=1:
        return product
    else:
        return product.removesuffix("\n")