################################## Tuple ####################################
#	                            Comparison Table	
#	*************************************************************************
#	*				         * Ordered * Iterable * Immutable * Multiple Data Types *
#	*************************************************************************
#	*  Lists	    	 *	 yes   *    yes   *	   no	    *	    		yes         *
#	*************************************************************************
#	*  Tuples	    	 *   yes   *	  yes   *    yes    *         yes         *
#	*************************************************************************
#	*  Strings   		 *   no    *    yes   *    yes    *         no          *
#	*************************************************************************
#	*  Dictionaries  *   no    *    yes   *    no     *         yes         *
#	*************************************************************************


tuple1 = ('USA', '001', '$') # Create a tuple
city_tuples = tuple(['Europ', 'Asia']) # Convert a list to a tuple

# discriminate between character variable and a tuple

char_var = ("USA") # or "USA"
print(type(char_var)) # <class 'str'>
char_tuple = ("USA",)
print(type(char_tuple)) # <class 'tuple'>

len(tuple1) # return length of tuple.

tuple1.count(0) # counts the number of instances of that value ("USA")
tuple1.index("$") # returns the index of the first instance of that value (1)

# concatenate tuples
tuple1 = tuple1 + ('Washington, D.C.', 'Donald Trump')
print(tuple1)
