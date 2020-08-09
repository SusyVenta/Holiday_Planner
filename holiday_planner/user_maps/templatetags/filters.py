from django.template.defaultfilters import register


@register.filter
def get_dict_item(dictionary, key):
    """
    Given a dictionary and a key variable,
    Returns the value for given key variable value from a dictionary.
    Necessary otherwise from the template it would look for a key with the name == key variable."""
    return dictionary[key]


