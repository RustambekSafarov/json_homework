import json

def getTitle(data:str):
    """Get the title name from the dictionary.

    Args:
        data (str): A string value

    Returns:
        str: Title in the dictionary
    """
    d = json.loads(data)
    return d['name']['title']

print(getTitle(open('data.json').read()))