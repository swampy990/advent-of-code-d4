infile = open("input.txt")
Lines = infile.readlines()
left_range = []
right_range = []
match = 0
line_num = 1

for line in Lines:
    #print(line_num)
    #line_num = line_num + 1
    field1 = (line.strip().split(',')[0])
    field2 = (line.strip().split(',')[1])

    field1_start = int(field1.split('-')[0])
    field1_end = int(field1.split('-')[1])

    field2_start = int(field2.split('-')[0])
    field2_end = int(field2.split('-')[1])

    field1_range = int(field1.split('-')[1]) - int(field1.split('-')[0])
    field2_range = int(field2.split('-')[1]) - int(field2.split('-')[0])

    if field1_range == 0:
        field1_range = 1

    if field2_range == 0:
        field2_range = 1

    n = field1_start
    field1_end = field1_end + 1
    while n < field1_end:
        left_range.append(n)
        n = n + 1

    n = field2_start
    field2_end = field2_end + 1
    while n < field2_end:
        right_range.append(n)
        n = n + 1

    if set(right_range).intersection(left_range) == set(right_range):
        match = match + 1
        print(line)
    elif set(left_range).intersection(right_range) == set(left_range):
        match = match + 1
        print(line)
    left_range.clear()
    right_range.clear()

print(match)





