# Write a program to tell me the shared numbers/items within 2 lists.

# This code works fine.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # List a
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # List b
c = [] # C = empty list, I will use the .append function with the 'item' tag to..
# Stick all the overlapping numbers into, thus creating our new list of overlapping int's (items).
for item in a: # item is just the placeholder name (like for i in list etc)
    if item in b:
        if item not in c: # This line and the line under it are the more difficult parts to remember
            c.append(item)
print("this is list A ", a) # Printing these out on separate lines makes it easier to read on the output
print("this is list B ", b)
print("This is the new list containing all duplicates from lists a and b ", c) # This prints c, our new list
