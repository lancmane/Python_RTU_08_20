# # # Python Tuples (a,b)
# # # Immutable
# # # Use - passing data that does not need changing
# # # Faster than list
# # # "safer" than list
# # # Can be key in dict unlike list
# # # For Heterogeneous data - meaning mixing different data types(int,str,list et al) inside
# # # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# # # https://realpython.com/python-lists-tuples/

my_tuple = ("Valdis", "programmer", 45, 200.8, [10, 20, 30], True, None, {'food':'potatoes', 'drink':'kefir'})
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(len(my_tuple))
print(my_tuple[-1]) 
print(my_tuple[-1]['drink']) # get also would work
print(my_tuple[4][1])

mykey = "Valdis", 180 # i can make tuple without parenthesis when there is no confusion
print(mykey)
# # to use tuple as key tuple must only have immutables inside as well
newdict = {mykey:9000, "secondkey":9050}
print(newdict)
print(newdict[mykey])

# # tuples are immutable but you can mutate those data structures inside which are mutable
my_tuple[-1].setdefault(mykey, 500)
print(my_tuple)
my_tuple[-1][mykey] = 9000
print(my_tuple)

# my_tuple[4] += [1,2,3] # i can not write a new list in place of old list, OUT OF PLACE will not work
my_tuple[4].extend([1,2,3]) # BUT i can can mutate the old list IN PLACE
my_pop = my_tuple[4].pop()
my_tuple[4].append(5000) # BUT i can can mutate the old list
print(my_tuple)
# # print(my_tuple[-1])
# # print(my_tuple)
print(my_tuple[-1].get(mykey))

# regular slicing works
mini_3 = my_tuple[:3] # i can extract sub tuple
print(mini_3, type(mini_3))
# my_tuple[1] = "teacher" # will not work because tuples are immutable
my_list = list(my_tuple)
my_list[1] = "teacher"
print(my_list)
print(my_tuple)
my_tuple = tuple(my_list)
print(my_tuple)

print(my_tuple[::2])
print(my_tuple[::-1])
print((4,5,"Valdis")) # so i create tuple on the fly - hot tuple

mult_tuple = tuple(el * 2 for el in my_tuple[:5])
print(mult_tuple)
int_tuple = tuple(el**2 for el in range(1,10)) # this is not tuple but generator meaning it is made on demand not ready
print(int_tuple)

my_list = []
# for el in mini_3:
for el in my_tuple[:5]:
    if type(el) == int or type(el) == float:
        my_list.append(1/el) # could also check for zero
    else:
        my_list.append(el[::-1]) # might want to check also Booleans and None types and dictionaries
my_rev_tuple = tuple(my_list)
print(my_rev_tuple)

# # # print(my_tuple)
# # # my_tuple[1] = "scientist"
# # my_list = list(my_tuple)
# # print(my_list)
# # my_list[1] = "scientist"
# # new_tuple = tuple(my_list)
# # print(new_tuple)


t = ()  # empty tuple only question where would you use it? One use to functions which need some sequence
print(t, type(t))
t = (1, 2, 55)  # 2 or more elements
print(t, type(t))
t = (5,)  # if you really need a tuple of one element
print(t, type(t))
# my_tuple. # i can use . for Intellisense to suggest methods, we only have 2
print(my_tuple.count("programmer"))
print(my_tuple.index("teacher"))
print(my_tuple.index(45))
if "programmer" in my_tuple:
    print(my_tuple.index("programmer"))
else:
    print("Not found the key")
# # # print(my_tuple.index("notprogrammer"))
# print("somevalue" in my_tuple)

# # print(new_tuple.count("programmer"))
# # print(new_tuple.index("scientist"))
# # print(my_tuple.index(45))

# Trick on swapping values
a = 10
b = 20
print(a, b)
# how to change them
temp = a
a = b
b = temp
print(a, b)
# # # # in Python the above is simpler!
# # print(a, b)
a, b = b, a  # we can even change a,b,c,d = d,c,b,a and more
print(a, b)

a, b, c = 5, 10, "Booo" # example of tuple packing and unpacking
print(a,b,c)
my_num_tuple = 5, 6, 8
print(my_num_tuple, type(my_num_tuple))
my_num_tuple = (5, 6, 8)
print(my_num_tuple, type(my_num_tuple))

print(len(my_tuple))
name, job, age, top_speed, favorite_list, _ , _ , favorite_dict = my_tuple  # tuple unpacking
# _ symbolizes variables we do not care about
print(name, job, age, top_speed, favorite_list)
# # name is my_tuple[0]
# # tuple unpacking and using _ for values that we do need
(name, job, _, top_speed, _) = my_tuple[:5]
print(name, _)  # so _ will have value of last unpacking
(name, job, _, top_speed) = my_tuple[:4]
print(name, _)  # so _ will have value of last unpacking


def getMinMax(my_num_list):
    # so tuple will be created when returning multiple values
    return min(my_num_list), max(my_num_list)


res = getMinMax([3, 6, 1, 2])
print(res, type(res))

my_min, my_max = getMinMax([3, 6, 1, 2])
print(my_min,my_max)