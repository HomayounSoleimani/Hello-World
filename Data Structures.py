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

country_list[0] = 'Madrid' # replace Madrid with Los angles as element 0 from city_list
print(city_list)


# find elements in a list
print(city_list.index('Ankara')) # returns index of first matched instance

print(city_list.count('Paris')) # counts the number of instances

# concatenate lists
country_list = country_list + ['Algeria','Canada','Russia']
print(country_list)

# slicing a list [start:end:stride]
Cars = ['mpg','cylinders','displacement','horsepower','weight', 'acceleration', 'model_year', 'origin', 'car_name']
print(Cars[0]) # print first feature(element 0) : mpg
print(Cars[0:3]) # print first three features(elements 0, 1, 2) : ['mpg', 'cylinders', 'displacement']
print(Cars[:3]) # print first three features(elements 0, 1, 2) : ['mpg', 'cylinders', 'displacement']
print(Cars[3:]) # print features from 3rd position (elements 3, 4, 5, 6, 7, 8) : ['horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
print(Cars[-1]) # print last feature(last element (element 8)) : car_name 
print(Cars[::2]) # print every 2nd features(elements (0, 2, 4)) : ['mpg', 'displacement', 'weight', 'model_year', 'car_name']
print(Cars[::-1]) # print backwards (4, 3, 2, 1, 0) : ['car_name', 'origin', 'model_year', 'acceleration', 'weight', 'horsepower', 'displacement', 'cylinders', 'mpg']

# alternative method for returning the list backwards
list(reversed(Cars)) # : ['car_name', 'origin', 'model_year', 'acceleration', 'weight', 'horsepower', 'displacement', 'cylinders', 'mpg']

# sort a list in place (modifies but does not return the list)
city_list.sort() # : ['Ankara', 'Los angles', 'Paris', 'Rome', 'Zurich']
city_list.sort(reverse=True) # sort in reverse : ['Zurich', 'Rome', 'Paris', 'Los angles', 'Ankara']
city_list.sort(key=len) # sort by a key : ['Rome', 'Paris', 'Zurich', 'Ankara', 'Los angles']

# return a sorted list (but does not modify the original list)
sorted(city_list)
sorted(city_list, reverse=True)
sorted(city_list, key=len)

# three way of copying list
new_list = Cars.copy()
new_list = Cars[:]
new_list = list(Cars)

# examine objects of a list
print(Cars == new_list) # returns True (their contents are equivalent)
