from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    messages: list[dict] = data['messages']
    message_count = 0
    for message in messages:
        if message['type']=='message':
            message_count+=1

    return message_count

data = read_data('data/result.json')
print(find_number_of_messages(data))