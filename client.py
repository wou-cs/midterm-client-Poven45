import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    base_url = "http://chrisbrooks.pythonanywhere.com/"
    r = requests.get(base_url + 'api/programmers')
    programmers_data = r.json()
    return len(programmers_data['programmers'])


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    return ""
