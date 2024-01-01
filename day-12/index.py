from typing import TypeAlias

WORKING_CHAR = '.'
DAMAGED_CHAR = '#'
UNKNOWN_CHAR = '?'

Spring_Row: TypeAlias = tuple[str, list[int]]

def process_springs(line: str) -> Spring_Row:
    springs, groups_str = line.split(' ')
    groups = [int(group) for group in groups_str.split(',')]
    return (springs, groups)

def solve_spring_row(spring_row: Spring_Row) -> str:
    _, groups = spring_row
    solution = ".".join([DAMAGED_CHAR * group for group in groups])
    return solution


FILE = open('./input.txt')
LINES = [line.strip() for line in FILE if line.strip()]
SPRINGS = [process_springs(line) for line in LINES]

solutions = [solve_spring_row(spring_row) for spring_row in SPRINGS]
print(solutions)