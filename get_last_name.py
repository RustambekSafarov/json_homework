import json

def getLastName(data:str):
    """Get the last name from the dictionary.

    Args:
        data (str): A string value

    Returns:
        str: Last name in the dictionary
    """
    d = json.loads(data)
    
    return d['name']['last']

print(getLastName(open('data.json').read()))