import re
import os 

EXAMPLE_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
EXAMPLE_INPUT2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
def main():
    filename = "input_day3.txt"
    if not os.path.isfile(filename):
        print("Input file does not exist")
    else :
        with open(filename) as f:
            input = f.read()
            regex_pattern_for_mul_instructions = r"mul\(\d{1,3},\d{1,3}\)"
            mul_instructions = re.findall(regex_pattern_for_mul_instructions, input)
            regex_pattern_for_mul_terms = r"mul\((\d+),(\d+)\)"
            mul_instructions = [list(map(int, *re.findall(regex_pattern_for_mul_terms, instruction))) for instruction in mul_instructions]
            result = sum([instruction[0] * instruction[1] for instruction in mul_instructions])
            print(f"Result for part 1: {result}")
            # part 2
            
            regex_pattern_for_all_instructions = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
            instructions = re.findall(regex_pattern_for_all_instructions, input)
            enabled = True
            result = 0
            for instruction in instructions:
                if enabled and instruction.startswith("mul"):
                    operation = list(map(int, *re.findall(regex_pattern_for_mul_terms, instruction))) 
                    result += operation[0] * operation[1]
                else :
                    enabled = (instruction == "do()")
            print(f"Result for part 2: {result}")

            


if __name__ == "__main__":
    main()