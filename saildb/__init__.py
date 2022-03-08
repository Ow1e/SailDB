from types import NoneType
import logging

def return_none(*args, **kwargs):
    return None

def run_type(objtype):
    return {"i": int, "f": float, "s": str, "d": dict, "b": "BOOL", "n": "NONE"}[objtype]

def find_type(object):
    return {int: "i", float: "f", str: "s", dict: "d", bool: "b", NoneType: "n"}[object]

def advance(string):
    passings = 0
    product = ""
    for i in string:
        if i == ":" and product == "":
            passings += 1
        
        if passings >= 3:
            product += i
    return product.removesuffix(";")[1:]

def parse(string : str):
    contents = string.split(":")
    mapping = int(contents[0])
    directive = str(contents[1])
    objtype = str(contents[2])
    result = advance(string)
    pass_through = run_type(objtype)
    return mapping, directive, pass_through, result

def load(data : str):
    """
    Loads SAIL into Python Objects
    ```
    with open("mything.sail") as f:
        data = saildb.load(f.read())
    ```
    """
    export = {} # Exported Content
    mappings = {1: []}
    line = -1
    for i in data.splitlines():
        parsed = False
        try:
            line+=1
            mapping, directive, pass_through, result = parse(i)
            parsed = True

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
            elif pass_through == "NONE":
                level[directive] = None
            else:
                level[directive] = pass_through(result)
        except Exception as e:
            if i == "":
                logging.warning(f"Skipped line #{line} because it was empty and gave a error")
            elif not parsed:
                logging.critical(f"Error parsing line {line}, elements may be missing from export")
            else:
                logging.critical(f"Error computing line #{line}, elements may be missing from export: {e.args}")

    return export

def dump(data, deep = 1):
    """
    Dumps data into SAIL, use deep to specify how deep the database is (dont change it unless you know what you are doing)
    """
    product = ""
    # Check to see if its array switchable
    if type(data) == list:
        c = 0
        new = {}
        for i in data:
            new[c] = i
            c+=1
        data = new

    for i in data:
        current = data[i]
        if type(current) == list:
            new = {}
            for l, d in enumerate(current):
                new[l] = d
            current = new
        if type(current) == dict:
            product += f"{deep}:{i}:{find_type(type(current))}:{str(deep+1)};\n"
            product += dump(current, deep=deep+1)
        else:
            product += f"{deep}:{i}:{find_type(type(current))}:{str(current)};\n"
    if deep!=1:
        return product
    else:
        return product.removesuffix("\n")