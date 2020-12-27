import copy
ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def main():
    f = open('input.txt', 'r')
    instructions = f.read().split('\n')[:-1]
    op_arg_pairs = structure_instructions(instructions)
    print(find_fix(op_arg_pairs))

def run_instructions(op_arg_pairs):
    """
    Runs the given instructions, keeping track of
    the accumulator. Stops when it enters the second loop,
    or when the instructions have terminated.
    Returns the accumulator.
    """
    i = 0
    accumulator = 0
    ran = []
    while True:
        if i == len(op_arg_pairs) - 1 or i in ran:
        else:
            op_arg = op_arg_pairs[i]
            if op_arg[0] == ACC:
                ran.append(i)
                accumulator += int(op_arg[1])
                i += 1
            elif op_arg[0] == JMP:
                ran.append(i)
                i += int(op_arg[1])
            else:
                ran.append(i)
                i += 1
    return accumulator

def check_termination(op_arg_pairs):
    i = 0
    ran = []
    terminates = True
    while terminates:
        if i == len(op_arg_pairs) - 1:
            break
        if i in ran:
            terminates = False
            break
        else:
            op_arg = op_arg_pairs[i]
            if op_arg[0] == ACC:
                ran.append(i)
                i += 1
            elif op_arg[0] == JMP:
                ran.append(i)
                i += int(op_arg[1])
            else:
                ran.append(i)
                i += 1
    return terminates

def find_fix(op_arg_pairs):
    """
    Finds the accumulator value when a NOP<->JMP swap is done
    that makes the instructions not loop.
    """
    for i in range(len(op_arg_pairs)):
        if op_arg_pairs[i][0] == JMP:
            pairs_copy = copy.deepcopy(op_arg_pairs)
            pairs_copy[i] = (NOP, pairs_copy[i][1])
            if check_termination(pairs_copy):
                return run_instructions(pairs_copy)
        elif op_arg_pairs[i][0] == NOP:
            pairs_copy = copy.deepcopy(op_arg_pairs)
            pairs_copy[i] = (JMP, pairs_copy[i][1])
            if check_termination(pairs_copy):
                return run_instructions(pairs_copy)
    
def structure_instructions(instructions):
    """
    Takes in lines from file and structures into a list
    of (operation, argument) tuples 
    """
    structured_instructions = []
    for instruction in instructions:
        instr = instruction.split(' ')
        structured_instructions.append((instr[0], instr[1]))
    return structured_instructions
    
if __name__ == '__main__':
    main()
