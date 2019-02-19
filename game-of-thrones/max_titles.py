from characters import characters
# who has the most titles

# lets assume that we have seen no titles yet
most_titles = 0
person_with_most_titles = ''
# visit each character and see if they have more than 'most_titles'
for person in characters:
    num_titles = len(person['titles'])
    if num_titles > most_titles:
        most_titles = num_titles
        person_with_most_titles = person['name']
# print names of each person with the same number of titles as 'most_titles'
for person in characters:
    num_titles =  len(person['titles'])
    if num_titles == most_titles:
        # print("%s has %d titles" %(person_with_most_titles, most_titles))
# if so save new value to 'most_titles
# if not, ignore them

# print person['name] has (this many titles)
        print("%s has %d titles" % (person['name'], most_titles))