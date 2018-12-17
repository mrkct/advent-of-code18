

def addr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] + new[B]

    return new

def addi(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] + B

    return new

def mulr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] * new[B]

    return new

def muli(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] * B

    return new

def banr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] & new[B]

    return new

def bani(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] & B

    return new

def borr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] | new[B]

    return new

def bori(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A] | B

    return new

def setr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = new[A]

    return new

def seti(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    new[C] = A

    return new

def gtir(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if A > new[B]:
        new[C] = 1
    else:
        new[C] = 0
    
    return new

def gtri(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if new[A] > B:
        new[C] = 1
    else:
        new[C] = 0
    
    return new

def gtrr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if new[A] > new[B]:
        new[C] = 1
    else:
        new[C] = 0
    
    return new

def eqir(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if A == new[B]:
        new[C] = 1
    else:
        new[C] = 0
    
    return new

def eqri(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if new[A] == B:
        new[C] = 1
    else:
        new[C] = 0
    
    return new

def eqrr(state, instruction):
    new = list(state)
    _, A, B, C = instruction
    if new[A] == new[B]:
        new[C] = 1
    else:
        new[C] = 0
    
    return new


with open('chronal-classification-input1.txt', 'r') as file:
    opcodes = [
        addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
    ]
    similar = {}
    for opcode in range(0, 16):
        similar[opcode] = list(opcodes)
    
    while True:
        state = file.readline()
        if not state:
            break
        state = [int(x) for x in state[state.index('[')+1 : state.index(']')].split(',')]
        instructions = [int(x) for x in file.readline().split(' ')]
        result = file.readline()
        result = [int(x) for x in result[result.index('[')+1 : result.index(']')].split(',')]
        file.readline()
        for opcode in opcodes:
            if opcode(state, instructions) != result and opcode in similar[instructions[0]]:
                similar[instructions[0]].remove(opcode)
    
    opcode_dict = {}
    for _ in range(30):
        for s in similar:
            if len(similar[s]) == 1:
                function = similar[s][0]
                opcode_dict[s] = function
                for k in similar:
                    if function in similar[k]:
                        similar[k].remove(function)
    for f in opcode_dict:
        print('{} : {}'.format(f, opcode_dict[f].__name__))

    # Execute program
    
    registers = [0, 0, 0, 0]
    for line in open('p.txt', 'r'):
        instructions = [int(x) for x in line.split(' ')]
        opcode = instructions[0]
        registers = opcode_dict[opcode](registers, instructions)
    
    print(registers)
    print("Value in register 0: {}".format(registers[0]))
    
