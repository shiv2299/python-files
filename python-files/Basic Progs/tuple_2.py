# exercise for tuples

file_handle = open("Basic Progs/mbox-short.txt")

hour_count_dict = dict()

for line in file_handle:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(':')[0]
        hour_count_dict[hour] = hour_count_dict.get(hour, 0) + 1

sorted_hours_list = sorted([ (k,v) for k,v in hour_count_dict.items() ])

for hour,count in sorted_hours_list:
    print(hour, count)