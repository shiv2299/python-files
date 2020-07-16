dictionary1 = dict()
dictionary1["Name"] = "Yagnesh"
dictionary1["Age"] = 20
dictionary1["gender"] = "Male"
print(dictionary1)

dictionary1["Age"] + 3

dict2 = {"Yagnesh": 1, "Age": 21}
for key in dict2:
    print(key, dict2[key])

# counting the number of time key occurs as an input- approach 1
dict1 = {"Yagnesh": 1, "siddhi": 1, "Patil":1}

while True:
    inp = input("Enter a key:")
    if inp == "done": break
    if inp in dict1:
        dict1[inp] = dict1[inp] + 1
    else: dict1[inp] = 1

print(dict1)

# Approach -2 using get method of dictionary which accepts 2 args:
# 1. key name, 2. default value, if key is found in dict then it returns value related to given key else returns default value.
dict1 = {"yagnesh":1, "yagnesh2":1, "siddhi":1, "patil":1}

while True:
    inp = input("Enter a key:")
    if inp == "done": break
    dict1[inp] = dict1.get(inp,0) + 1

print(dict1)

# working with list and dictionaries

    # converting dictionary into list
print(list(dictionary1))
print(dictionary1.keys())  #gives list of keys from dict
print(dictionary1.values()) #gives list of values from dict
print(dictionary1.items()) #gives list of keys, values from dict that is list of tuples

#putting 2 iteration variables in for loop to loop through tuples list
for i,j in dictionary1.items():
    print(i,j)


line = input("enter whole sentence:")
list_dict = dict()
lst = line.split()

for word in lst:
    list_dict[word] = list_dict.get(word,0) + 1

print(list_dict)

# working with dictionaries & files

word_count_dict = dict()
file_handle = open("romeo.txt")
for line in file_handle:
    words_in_line = line.split()
    for word in words_in_line:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

big_count = None
big_word = None
for word, count in word_count_dict.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word,big_count)