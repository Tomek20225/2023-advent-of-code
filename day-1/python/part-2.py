FILE = open('../input.txt', "r")
SPELLED_NUMS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0

for line in FILE.readlines():
    nums: list[int] = []

    for i, char in enumerate(line):
        if char.isnumeric():
            nums.append(int(char))
            continue

        for num, spelled_num in enumerate(SPELLED_NUMS):
            if char == spelled_num[0]:
                substr = line[i: i + len(spelled_num)]
                if substr == spelled_num:
                    nums.append(num + 1)
                    break

    first = nums[0]
    last = nums[len(nums) - 1]
    val = (first * 10) + last

    sum += val

print(sum)