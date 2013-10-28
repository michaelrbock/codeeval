import sys

input = open(sys.argv[1], 'r')

nums = []

for line in input:
    nums.append(int(line))

input.close()

for i, num in enumerate(nums):
    count = 1
    sum = num + int(str(num)[::-1])
    if str(sum) == str(sum)[::-1]:
        sys.stdout.write(str(count) + ' ' + str(sum))
    else:
        while str(sum) != str(sum)[::-1]:
            count += 1
            sum = sum + int(str(sum)[::-1])
        sys.stdout.write(str(count) + ' ' + str(sum))
    if i != len(nums) - 1:
        sys.stdout.write('\n')
