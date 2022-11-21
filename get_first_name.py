import json

def getFirstName(data:str):
    """Get the first name from the dictionary.

    Args:
        data (str): A string value

    Returns:
        str: First name in the dictionary
    """
    d = json.loads(data)
    
    return d['name']['first']

print(getFirstName(open('data.json').read()))