file_handle = open("Basic Progs/mbox-short.txt")
max_count_dict = dict()

for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        max_count_dict[words[1]] = max_count_dict.get(words[1], 0) + 1


big_count = None
big_word = None
for word, count in max_count_dict.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)