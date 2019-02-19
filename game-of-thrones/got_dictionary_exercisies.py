from characters import characters
print(len(characters))
import requests
import time
# # jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # # print out the key names individually
# # # for k in jon_snow:
# # #     print(k)

# # # print out just the values
# # # for k in jon_snow:
# # #     print(jon_snow[k])

# # # print both the key and the value
# # for k in jon_snow:
# #     print("%s: %s" % (k, jon_snow[k]))


# # print all characters whose name begins with an "A"

# # def a_names()
#     # names_with_a = []
#     # for i in characters:
#     #     if i ['name'][0] == 'A':
#     #         return 
#     #         print(i['name'])

# # print characters names that start with "Z"
# # same as above just change "A" to "Z"
# print('next question')
# # print how many characters are dead
# # define a function
# # def whos_dead():
#     # empty dictionary to add (append) results into

#     # 
# for j in characters:
#     dead_characters = []
#     if j['died'] != "":
#         dead_characters.append(j)
#     print (len(dead_characters(j)))

# # who has the most titles
# def most_titles:
#     titles = []
#     for k in characters:
#         if 

#     print(most_titles(titles))
# # hot pie
# # maybe??
# for i in characters:
#     if ['name'] == 'Hot Pie'
#     print(i)

print('histogram')
# GoT histogram
# count number of people that are part of a house

def make_house_histogram(character_list):
    histogram = {}
    # loop through all characters
    for person in character_list:
        # what do i check for each person?
        allegiances = person['allegiances'] 
        # allegiances is a list of URLs
        for house in allegiances:
            # do something with that house.
            # add data to histogram
            # checks to see if the key is already added to histogram
            if house in histogram:
                # if it is then add one the the counter of how many
                histogram[house] = histogram[house] + 1
                # if not already in dictionary add it.
            else:
                histogram[house] = 1
    return histogram
# function to use string interpolation to make dictionary look better when printed
def pretty_print_histogram(histogram):

    for house in histogram:
            
        print("%s has %d members" % (house, histogram[house]))
# change urls into the actual house names
def translate_url_to_house_name(URL):
    # empty string for house names.
    house_name = ''
    r = requests.get(URL)
    # converts to a readable format
    house_info = r.json()
    # pulls name of the house from the api dictionary
    house_name = house_info['name']
    return house_name
    # print function passing characters into it.


def convert_to_nice_names(histogram):
    nice_histogram = {}
    for URL in histogram:
        # create variable to pass urls
        house_name = translate_url_to_house_name(URL)
        nice_histogram[house_name] = histogram[URL]
        # delay to not overload api
        time.sleep(0.1)
    return nice_histogram

    # using each function to print what i want to be shown.
ugly_histogram = make_house_histogram(characters)
pretty_histogram = convert_to_nice_names(ugly_histogram)
pretty_print_histogram(pretty_histogram)
# print(make_house_histogram(characters))