input_list = [int(x) for x in input().split(' ')]
target = int(input())

elements = {}
output_list = [0, 0]
for i in input_list:
    difference = target-i
    if difference in elements:
        output_list[0] = elements[difference]
        output_list[1] = input_list.index(i)
    else: 
        elements[i] = input_list.index(i)

print(output_list)