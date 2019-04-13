#Python has quite a few builtins data structures which are lists, tuples, dictionaries, strings and sets.


###########List###################

# Create a New List
# List index start from 0

city_list = ['Los angles', 'Paris', 'Istanbul', 'Zurich']
country_list = list(['United State', 'France', 'Turkey', 'switzerland'])
print(city_list) # : ['Los angles', 'Paris', 'Istanbul', 'Zurich']
print(country_list) # : ['United State', 'France', 'Turkey', 'switzerland']

# List length

print(len(city_list)) # 4

# modify a list

city_list.append('Rome') # append Rome to end of city_list
print(city_list) # : ['Los angles', 'Paris', 'Istanbul', 'Zurich', 'Rome']

country_list.extend(['Italy', 'Greek']) # append 'Italy' and 'Greek" to end of country_list
print(country_list) # : ['United State', 'France', 'Turkey', 'switzerland', 'Italy', 'Greek']

city_list.insert(0, 'Tehran') # add Tehran to index 0 of city_list
print(city_list) # : ['Tehran', 'Los angles', 'Paris', 'Istanbul', 'Zurich', 'Rome']

country_list.remove('Greek') # searches for first element(city) in city_list and removes it
print(country_list) # : ['United State', 'France', 'Turkey', 'switzerland', 'Italy']

city_list.pop(0) # removes Tehran as element with 0 index in city_list and returns it
print(city_list) # : ['Los angles', 'Paris', 'Istanbul', 'Zurich', 'Rome']

del country_list[0] # removes United State as  element 0 from country_list
print(country_list) # : ['France', 'Turkey', 'switzerland', 'Italy']

city_list[2] = 'Ankara' # replace Ankara to Istanbul with index 2
print(city_list) # : ['Los angles', 'Paris', 'Ankara', 'Zurich', 'Rome']
