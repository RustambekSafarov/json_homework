import json

def getStreet(data:str):
    """Get the street name from the dictionary.

    Args:
        data (str): A string value

    Returns:
        str: A name of the street in the dictionary
    """
    d = json.loads(data)
    
    return d['location']['street']['name']

print(getStreet(open('data.json').read()))