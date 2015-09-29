"""
Prints out all the melons in our inventory
"""

from melons import melon_names


def print_all_melons(melon_data):

    for melon, attributes in melon_data.items():
        print melon.upper()
        for attributes, value in attributes.items():
            print "{}:, {}".format(attributes, value)

        print


print_all_melons(melon_names)