ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def main():
    f = open('input2.txt', 'r')
    instructions = f.read().split('\n')[:-1]
    op_arg_pairs = structure_instructions(instructions)
    print(run_instructions(op_arg_pairs))

def run_instructions(op_arg_pairs):
    """
    Runs the given instructions, keeping track of
    the accumulator. Stops when it enters the second loop.
    Returns the accumulator.
    """
    i = 0
    accumulator = 0
    ran = []
    while True:
        if i in ran:
            break
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
