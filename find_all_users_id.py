from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messages: list[dict] = data['messages']
    user_ids = []
    for message in messages:
        if 'from_id' in message.keys():
            user_ids.append(message['from_id'])

    return user_ids

data = read_data('data/result.json')
# print(find_all_users_id(data))