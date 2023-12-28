import functools

FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]
HISTORIES = [[int(num) for num in line.split()] for line in LINES]

def get_differences(nums: list[int]) -> list[int]:
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]

def get_all_differences(nums: list[int]) -> list[list[int]]:
    if all(num == 0 for num in nums):
        return [nums]
    differences = get_differences(nums)
    return get_all_differences(differences) + [nums]

def predict_next_value(nums: list[int]) -> int:
    sequences: list[list[int]] = get_all_differences(nums)
    next_increment = functools.reduce(lambda a, b: a + b[-1], sequences, 0)
    return next_increment

def predict_prev_value(nums: list[int]) -> int:
    sequences: list[list[int]] = get_all_differences(nums)
    prev_increment = functools.reduce(lambda a, b: b[0] - a, sequences, 0)
    return prev_increment


# Part 1
predictions = [predict_next_value(history) for history in HISTORIES]
sum_of_predictions = sum(predictions)
print('Part 1:', sum_of_predictions)

# Part 2
predictions = [predict_prev_value(history) for history in HISTORIES]
sum_of_predictions = sum(predictions)
print('Part 2:', sum_of_predictions)
