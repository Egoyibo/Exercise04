
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]
    #pass

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list [1:]

def last(input_list):
    """Return the last element of the input list."""
    return input_list [-1]

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list [:-1]

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list [0:3]

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list [-5:]

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list [2:-2]

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list [2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list [-6:-2]

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0]=42
    return input_list

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list [2] = 37
    input_list [-1] = 37
    return input_list

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """

    """mylist = input_list[0:2]
    mylist.append(42)
    mylist.append(37)
    mylist.insert (len(mylist),input_list[:-2])

    mylist.insert(len(mylist),input_list[:-1])
    return mylist"""

    input_list[2] = 42
    input_list[3] = 37
    del input_list[4:-2]

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6]
    del input_list[2]
    #1) If you remove the 7th before the 3rd then you don't screw up the index of the lower number
    #2) [6] didn't work because we screwd up the index by removing 3rd element first

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """

    del input_list[2:-2]    
    
"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    count = 0
    
    for x in input_list:
        count = count + 1

    return count

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
#    mylist = [value]
 #   input_list = input_list + mylist
  #  input_list = input_list + [value]

    input_list[custom_len(input_list):] = [value]
#    input_list += [value]
    #the_list = []
    #the_list = input_list + mylist
    #the_list [-1] = value
#    return input_list
    

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    input_list += values
    

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    input_list[custom_len(input_list):] = [" "]

    input_list[index+1:] = input_list[index:-1]

    input_list[index] = value
    #custom_append(input_list[:index], value)
    #custom_append(input_list, input_list [(index+1):])
    #newlist1 = input_list[:index]
    #custom_append (newlist1, value)
    #custom_append (newlist1, input_list [index+1:])
    #newlist2 = input_list [index:]
    #input_list += newlist1
    #input_list += newlist2
    #return newlist1


    #newlist1 = input_list[:index]
    #custom_extend(newlist1, [value])
    #custom_extend(newlist1, input_list [index+1:])

    #custom_extend (input_list [:index], custom_extend ([value], input_list[index:]))

    #custom_append (input_list [:index], value)

    #for i in input_list:
    #    custom_append(input_list, i)     
    #return
    #append(input_list[index:])

# #'''>>> list[6:] = [None]
# #>>> list
# #[1, 2, 37, 42, 6, 7, None]
# #>>> list[3:]
# [42, 6, 7, None]
# >>> list[2:-1]
# [37, 42, 6, 7]
# >>> list[3:] = list[2:-1]
# >>> list
# [1, 2, 37, 37, 42, 6, 7]
# >>> list [2] = 47
# >>> list
# [1, 2, 47, 37, 42, 6, 7]
# >>>''' 

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
   
    count = 0
    for i in input_list:
        if (i != value):
            count = count + 1
        else: 
            del input_list[count]
            return  # initially, we did not have this return, so it kept looking for the value, and on the second list, after it already deleted one, it also deleted "Ti"

    #count = 0
    #for i in input_list:
    #    if (input_list[count] == value):
    #        del input_list[count] 
     #       return 
      #  else: 
       #     count = count + 1   

# loop through a list
# compare each list element to a value
# if it matches, delete the element from the list
# to delete element from list, we need list index

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    out = input_list[-1]
    del input_list[-1]

    return out

def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    count = 0
    for num in input_list:
        if num == value:
            return count
        else:
            count = count + 1

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    item_count = 0

    for item in input_list:
        if item == value:
            item_count = item_count + 1
        else:
            ()

    return item_count

def custom_reverse(input_list):  
    """custom_reverse(input_list) imitates input_list.reverse()"""

    #create a variable for holding the first swap index[i]
    # i = 0
    # while (i < (( custom_len(input_list))/2)):
    #     swap_box = input_list[i]
    #     # print input_list
    #     input_list[i] = input_list[-1-i]
    #     # print input_list
    #     input_list[-1-i] = swap_box
    #     i = i + 1
    # return input_list 
    i = 0
    for item in input_list:
        swap_box = input_list[i]
        input_list[i] = input_list[-1-i]
        input_list[-1-i] = swap_box
        i = i + 1
        if i == ((custom_len(input_list))/2):
            break
    return input_list 


    # Later, we will make this into a for loop 
    # for item in input_list 
    #     swap_box = input_list[i]
    #     # print input_list
    #     input_list[i] = input_list[-1-i]
    #     # print input_list
    #     input_list[-1-i] = swap_box
    #     i = i + 1
    # return input_list 

    # for i in range ((custom_len(input_list)-1):
    #     input_list[custom_len(input_list):] = [" "]
    #     input_list[-1] = input_list[i]
    #     del input_list[0]
    # return input_list

    # for i in range (1, (custom_len(input_list)-1) , 1):
    #     input_list[custom_len(input_list):] = [" "]
    #     input_list[-1] = input_list[0]
    #     del input_list[0]
    # return input_list

    # for i in range (1, (custom_len(input_list)-1) , 1):
    #     input_list[custom_len(input_list):] = [" "]
    #     input_list[-1] = input_list[i]
    #     del input_list[0]

    # return input_list



    # output_list = []

    # # for 
    # # custom_pop (input_list)
    # for i in input_list:
    #     output_list = custom_append(output_list, custom_pop(input_list[i]))
    #     i = i +
    # return output_list    



    # for i in input_list:
    #     custom_insert(input_list, )

    # out = []

    # for index in range((custom_len(input_list)-1), -1, -1):
    #     out = out + [input_list[index]]

    # return out 


    # for index in input_list[cus]

    #     custom_append ()
    
    # # out = []
    # # for letter in input_list[-1:
    #     custom_append(input_list, letter)


def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""

    # for item in input_list:
    #     if item == value
    #         return true
    #     # else:
    #     #     return false

    count = 0
    for i in input_list:
        if count == custom_len(input_list):
            return False  
        elif i == value:
            return True 
        else:
            count = count + 1 

    # while (item != value):
    #     if item == value:
    #         return True
    #     elif count == custom_len(input_list):
    #         return False
    #     else:
    #         count = count + 1


def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    
    if custom_len(some_list) != custom_len(another_list):
        return False
    else:
        count = 0
        for item in some_list:
            if item == another_list[count]:
                count = count + 1
            else:
                return False
        return True



    #     if count == custom_len(another_list):
    #         return True 
    #     elif item == another_list[count]:
    #         count = count + 1
    #     # elif some_list[custom_len(some_list)] == another_list[custom_len(another_list)]:
    #     #     return True
    #     elif item != another_list[count]:
    #         print some_list[count], another_list[count], False
            #return False
    #     for index in custom_len(some_list):
    #         if some_list[index] == another_list[index]:
    #             index = index + 1
    # elif some_list[custom_len(some_list)] == another_list[custom_len(another_list)]
    #         #     return True 
    #         else: 
    #             return False
    #         return true