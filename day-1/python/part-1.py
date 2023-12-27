def calculate_sum_from_file(file_path: str) -> int:
    """
    Parses a file for numbers (only digits) and returns their sum.
    Each line in the file is expected to contain at least one numeric character.
    Lines can contain other characters.
    
    Args:
    file_path (str): The path to the file to be read.
    
    Returns:
    int: The sum of the processed numbers.
    """

    total_sum = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                nums = [int(char) for char in line if char.isnumeric()]
                if nums:
                    first, last = nums[0], nums[-1]
                    val = (first * 10) + last
                    total_sum += val
                else:
                    print(f"No numeric characters found in line: {line}")

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
