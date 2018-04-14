import difflib as diff
from nicknames import nicknames

MAX_NUM_OF_TYPOS = 1


def set_new_max_num_of_typos(num):
    """

    :param num: int, num of typos to allow
    :return: None
             Note: Even though MAX_NUM_OF_TYPOS is
                   generally supposed to be a constant,
                   it can be changed for unit test purposes.
                    * not recommended
    """
    global MAX_NUM_OF_TYPOS
    MAX_NUM_OF_TYPOS = num


def get_max_num_of_typos():
    return MAX_NUM_OF_TYPOS


def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    """

    :param billFirstName: string, the first name in the billing address form (could include middle names)
    :param billLastName: string, the last name in the billing address form
    :param shipFirstName: string, the first name in the shipping address form (could include middle names)
    :param shipLastName: string, the last name in the shipping address form
    :param billNameOnCard: string, the full name as it appears on the credit card
    :return: int, the number of unique names in a transaction
    """

    # Parse each name group independently and then compare between them
    names = [
        get_parsed_name(billFirstName + " " + billLastName),
        get_parsed_name(shipFirstName + " " + shipLastName),
        get_parsed_name(billNameOnCard)
    ]

    # If only one of the name groups has a middle name apply it to all groups
    add_middle_name(names)

    # Get the number of unique names with current names list
    num_unique_names = unique_names(names)

    # If there is only one unique name function is done.
    if num_unique_names == 1:
        return 1

    # If not, billNameOnCard might have been given in the form of 'lastName, firstName'
    # as it is the only parameter not explicitly parted by first name and last name.
    # We'll swap the first and last name in the billNameOnCard group,
    # and count the unique names again:
    names[2]["first name"], names[2]["last name"] = \
        replace_nickname(names[2]["last name"]), names[2]["first name"]
    # Return the minimum count between the former and current count
    return min(num_unique_names, unique_names(names))


def get_parsed_name(name):
    """

    :param name: string, name group string in the form of "first name (middle name) last name"
    :return: dictionary, first, middle and last name details
    """

    # space is what defines the difference between first, middle and last name
    name = name.lower().split(" ")  # all comparisons on name groups are done in lowercase
    first_name = replace_nickname(name.pop(0)) if name else ""  # make sure the first name is not a nickname
    last_name = name.pop(-1) if name else ""
    return {"first name": first_name, "last name": last_name, "middle name": " ".join(name)}


def replace_nickname(name):
    """

    :param name: string, first name / nickname
    :return: string, the corresponding name if exists in the nickname dictionary, otherwise returns the name itself
    """
    return nicknames.get(name) if nicknames.get(name) is not None else name


def add_middle_name(names):
    """

    :param names: list, name groups list with their dictionaries
    :return: None, updates each name group with a middle name if existent in one of the other groups
    """

    middle_names = set()
    for name in names:
        middle_names.add(name["middle name"])  # add every middle name to the set
    middle_names.remove('') if middle_names.__contains__('') else None  # remove middle name if it is blank
    # If there is only one middle name in the set,
    # it is most likely that it applies to all names.
    if len(middle_names) == 1:
        # Give all the name groups in the list the same middle name found
        middle_name = middle_names.pop()
        for name in names:
            name["middle name"] = middle_name

    # Otherwise, if there is more than one middle name, keep the name groups as they were.


def unique_names(names):
    """

    :param names: list, name groups list with their dictionaries
    :return: int, the number of unique names found
    """
    # Return name groups back into strings for comparison
    check_names = [[], [], []]  # list of strings
    for i in range(len(names)):
        check_names[0].append(names[i]["first name"])
        check_names[1].append(names[i]["middle name"])
        check_names[2].append(names[i]["last name"])

    sum_unique_names = 1  # there is at least 1 unique name in transaction
    # compare first names, middle names, and last names separately
    for i in range(len(check_names)):
        # Check first of all if second group string and last group string match
        if equal_or_typo_equal(check_names[i][1], check_names[i][2]) == 0:
            # If so, return the check between the other groups (first and second)
            # Add 1 because there is at least one unique name in all groups.
            sum_unique_names += equal_or_typo_equal(check_names[i][0], check_names[i][1])
        # Else, return the check between first and second groups + first and last groups
        else:
            sum_unique_names += equal_or_typo_equal(check_names[i][0], check_names[i][1]) + \
                             equal_or_typo_equal(check_names[i][0], check_names[i][2])
    return sum_unique_names


def equal_or_typo_equal(string1, string2):
    """

    :param string1: string, first full name string to compare
    :param string2: string, second full name string to compare
    :return: int, function returns 1 if strings are unique and 0 otherwise.
             Note: Function compares unique people, not unique strings.
                  Therefore, the function calculates the similarities between
                  the two strings and uses NUM_OF_TYPOS to decide of the number
                  of errors in string is due to a typing error or not.
    """

    # Technically, we can exit early here if(str1 === str2),
    # but there's little reason to believe it's a significant optimization

    # Choose string1 to be the shorter string between the two
    if len(string1) > len(string2):
        string1, string2 = string2, string1  # swap the stings to check them correctly later on
    # If string1 is shorter than the MAX_NUM_OF_TYPOS the max difference must be changed to be smaller.
    # Otherwise, strings 'a' and 'b' for example, will match for MAX_NUM_OF_TYPOS set to 1.
    max_difference = min(len(string1)-1, MAX_NUM_OF_TYPOS)
    # The difference also accounts for the difference in the length of the two strings.
    # Strictness is calculated as (2 x num of matches)/num of characters in both strings
    if max_difference == len(string1)-1 == len(string2)-1:
        # set the strictness to 1 in order to check that the strings match completely
        strictness = 1
    else:
        if max_difference == len(string1)-1:
            max_difference -= 1  # make sure the strictness isn't 0
        strictness = 2 * float((len(string1) - max_difference)) / float((len(string1) + len(string2)))
    similarity = diff.SequenceMatcher(None, string1, string2)  # calculate the similarity of the two strings
    if similarity.ratio() >= strictness:
        return 0  # strings are similar, typo was found.
    return 1  # strings are not similar enough, return +1 to the number of unique names found.
