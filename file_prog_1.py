# file_handle = open('temp.txt','r')
# for line in file_handle:
#     for ch in line:
#         print(ch , end='')


# file2 = open('temp.txt')
# file_content = file2.read()
# print(file_content)


# fh = open(fname,'r')
# sum = count = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence: 0.") : continue
#     val = float(line[-7:])
#     count = count + 1
#     sum = sum + val
# ans = sum/count
# print("Average spam confidence:",ans)