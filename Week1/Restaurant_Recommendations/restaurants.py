"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    rating_list = [[name_to_rating[name], name] for name in names_final]
    return rating_list

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    names_matching_cuisine = [name for name in names_matching_price
                                    for cuisine in cuisines_list
                                    if name in cuisine_to_names[cuisine]]
    return names_matching_cuisine

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    # Read data into a big list splitted by '\n'
    with open(file) as f:
        file_list = f.read().splitlines()
        # for line in f.readlines():


    # Extract all details in order; every 5 lines as a segment
    restaurant_names = file_list[::5]       # the first lines are always the names
    restaurant_ratings = file_list[1::5]    # the second lines are the ratings
    restaurant_prices = file_list[2::5]     # the third lines are the prices
    restaurant_cuisines = [item.split(',') for item in file_list[3::5]]
        # the fourth lines, different types of food offered

    # "name_to_rating" initialization
    name_to_rating = {}
    # map the names and the ratings to construct a dict
    name_to_rating = dict(zip(restaurant_names, restaurant_ratings))

    # "price_to_names" initialization
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    # adding names to ratings
    for i in range(len(restaurant_ratings)):
        price_to_names[restaurant_ratings[i]].append(restaurant_names[i])

    #
    cuisine_to_names = {}
    restaurant_cuisines_lists = list(zip(restaurant_names, restaurant_cuisines))

    #
    for restaurant in restaurant_cuisines_lists:
        # for each cuisine
        for cuisine in restaurant[1]:
            # if it already exists
            if cuisine in cuisine_to_names.keys():
                # adding the restaurant's name
                cuisine_to_names[cuisine].append(r[0])
            # if not
            else:
                #adding this cuisine and the restaurant's name
                cuisine_to_names[cuisine] = [r[0]]
    return (name_to_rating, price_to_names, cuisine_to_names)
