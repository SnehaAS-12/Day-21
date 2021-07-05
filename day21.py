#Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

chocolate=("5 star","cadbury","kitkat","perk","dark chocolate")
icecream=("chocolate","vanilla","mango","Strawberry")
s=zip(chocolate,icecream)
print(s)
print(list(s))


#First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
a=range(1,8)
b=[2,6,5,9,8,1,7,3,0,4]
c=zip(a,b)
print(tuple(c))


#Using sorted() function, sort the list in ascending order.
v=[2,6,5,9,8,1,7,3,0,4]
v=sorted(v)
print(v)


#Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list1 = [1,2,3,4,5] 
even = lambda x: x % 2 == 0
list2 = list(filter(even, list1)) 
print(list2) 