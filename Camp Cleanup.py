sections = [2, 3, 4, 6, 7, 8] #first pair 2-4 and second pair 6-8

# find the length of the list
print(len(sections))

# create a set from the list
myset = set(sections)

# find the length of the Python set variable myset
print(len(myset))

# compare the length and print if the list contains duplicates
if len(sections) != len(myset):
    print("section repeats")
else:
    print("sections do not repeat")