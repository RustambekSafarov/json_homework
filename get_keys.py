import json

def getKeys(data:str):
    """Get the all keys from the dictionary.

    Args:
        data (str): A string value

    Returns:
        list: A list of all keys in the dictionary
    """
    d = json.loads(data)
    return list(d.keys())
print(getKeys(open('data.json').read()))