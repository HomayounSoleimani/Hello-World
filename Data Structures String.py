#################################### String ###############################
#	                                Comparison Table	
#	*************************************************************************
#	*                * Ordered * Iterable * Immutable * Multiple Data Types *
#	*************************************************************************
#	*  Lists         *   yes   *    yes   *	   no	    *         yes         *
#	*************************************************************************
#	*  Tuples        *   yes   *	  yes   *    yes    *         yes         *
#	*************************************************************************
#	*  Strings       *   no    *    yes   *    yes    *         no          *
#	*************************************************************************
#	*  Dictionaries  *   no    *    yes   *    no     *         yes         *
#	*************************************************************************


s = str('9876543210')
len(s) # return length of string object
s[i] # return ith elements of string object

s[:3] # slice string object from begining to 3th element 
s[5:] # slice string object from 5+1th to the end
s[-1] # return the last element of the string

# Some string methods
s = str('I Love NY.')
s.lower() # return lowercase
s.upper() # return CAPITAL

# examin string methods
s.startswith('I') # check if string obj starts with 'I', return True
s.endswith('NY') # check if string obj ends with 'NY', returns True
s.isdigit() # check if str obj is digit

s.find('NY') # returns index of first occurrence (2), but dose not support regex
# this method returns -1 if str obj dose not contain given string. 
s.replace('Love','Like') # replaces all instances of 'like' with 'love'
# this method is not case-sensitive

# split a string into a list of substrings separated by a delimiter
s.split(' ') # default separator is any whitespace.

# Join all items in a tuple into a string, using a delimiter
a = ['She','loves','Berlin']
' '.join(a) # returns 'She loves Berlin'

# concatenate strings
new_str = s + ' '.join(a) + str(' too much.')
print(new_str)

# removes characters from both left and right based on the argument.
# if argument is not provided, all leading and trailing whitespaces are removed from the str obj.
new_str.strip('.')

# string substitutions:

import datetime
import time

import datetime

day = datetime.date.today().day
month = datetime.date.today().month

print('Today is {} of month.'.format(day)) # new way
# second way
print('Today is {arg} of month.'.format(arg=day)) # named arguments

# string formatting
print('pi is {:.2f}'.format(3.14159)) # returns 'pi is 3.14'
