from typing import TypeAlias
from math import sqrt
import functools

Node: TypeAlias = tuple[str, str]

FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]

DIRECTIONS = {'L': 0, 'R': 1}
INSTRUCTIONS = [DIRECTIONS[char] for char in LINES[0]]

def get_node_name(line: str) -> str:
    name, _ = line.split(' = ')
    return name

def get_dirs(line: str) -> Node:
    _, dirs = line.split(' = ')
    dirL, dirR = dirs[1:-1].split(', ')
    return (dirL, dirR)

NODES: dict[str, Node] = {get_node_name(line):get_dirs(line) for line in LINES[1:]}

def get_distance_to_end_node(start_node_name: str, end_node_name: str) -> int:
    steps = 0
    current_node = start_node_name
    while True:
        instruction = INSTRUCTIONS[steps % len(INSTRUCTIONS)]
        current_node = NODES[current_node][instruction]
        steps += 1
        match len(end_node_name):
            case 1:
                if current_node[-1] == end_node_name:
                    break
            case 3:
                if current_node == end_node_name:
                    break
    return steps


# Part 1
start_node = 'AAA'
end_node = 'ZZZ'
steps = get_distance_to_end_node(start_node, end_node)

print('Part 1:', steps)


# Part 2
def get_prime_factors(num: int) -> list[int]:
    prime_factors: list[int] = []
    
    while num % 2 == 0:
        prime_factors.append(2)
        num /= 2

    for i in range(3, int(sqrt(num) + 1), 2):
        while num % i == 0:
            prime_factors.append(i)
            num /= i

    if num > 2:
        prime_factors.append(int(num))

    return prime_factors

def find_lowest_common_multiple(nums: list[int]) -> int:
    prime_factors = [get_prime_factors(num) for num in nums]
    frequencies: list[dict[int, int]] = []

    for primes in prime_factors:
        frequency: dict[int, int] = {}

        for num in primes:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        frequencies.append(frequency)

    max_frequency: dict[int, int] = {}

    for freq in frequencies:
        for num in freq:
            if num in max_frequency and freq[num] > max_frequency[num]:
                max_frequency[num] += freq[num]
            else:
                max_frequency[num] = freq[num]

    lcm = functools.reduce(lambda a, b: a * b * max_frequency[b], max_frequency, 1)
    return lcm


start_nodes_last_char = 'A'
end_nodes_last_char = 'Z'
starting_nodes = [node for node in NODES if node[-1] == start_nodes_last_char]
distances_to_end_node = [get_distance_to_end_node(node, end_nodes_last_char) for node in starting_nodes]
steps = find_lowest_common_multiple(distances_to_end_node)

print('Part 2:', steps)