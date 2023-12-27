def calculate_sum_from_file(file_path: str) -> int:
    """
    Parses a file for numbers (both digits and spelled out) and returns their sum.
    Each line in the file is expected to contain at least one number in either format.
    Lines can contain other characters.
    
    Args:
    file_path (str): The path to the file to be read.
    
    Returns:
    int: The sum of the processed numbers.
    """
        
    SPELLED_TO_NUM = {word: i + 1 for i, word in enumerate([
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ])}
    total_sum = 0

    try:
        with open(file_path, 'r') as FILE:
            for line in FILE:
                nums: list[int] = []

                for i, char in enumerate(line):
                    if char.isnumeric():
                        nums.append(int(char))
                    else:
                        for spelled_num, num in SPELLED_TO_NUM.items():
                            if char == spelled_num[0] and line.startswith(spelled_num, i):
                                nums.append(num)
                                break
                
                if len(nums) >= 1:
                    first, last = nums[0], nums[-1]
                    val = (first * 10) + last
                    total_sum += val
                else:
                    print(f"No numeric characters and no spelled out words found in line: {line}")
                
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
    return total_sum


# Solution
file_path = '../input.txt'
result = calculate_sum_from_file(file_path)
print(result)
