FILE = open('../input.txt', "r")

sum = 0

for line in FILE.readlines():
    nums: list[int] = []

    for char in line:
        if char.isnumeric():
            nums.append(int(char))

    first = nums[0]
    last = nums[len(nums) - 1]
    val = (first * 10) + last

    sum += val

print(sum)