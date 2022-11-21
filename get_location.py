import json

def getLocation(data:str):
    """Get the location keys from the dictionary.

    Args:
        data (str): A string value

    Returns:
        str: location in the dictionary
    """
    d = json.loads(data)
    
    return d['location']

print(getLocation(open('data.json').read()))