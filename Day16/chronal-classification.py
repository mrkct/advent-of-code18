

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
    c =0
    opcodes = [
        addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
    ]
    while True:
        state = file.readline()
        if not state:
            break
        state = [int(x) for x in state[state.index('[')+1 : state.index(']')].split(',')]
        instructions = [int(x) for x in file.readline().split(' ')]
        result = file.readline()
        result = [int(x) for x in result[result.index('[')+1 : result.index(']')].split(',')]
        file.readline()
        like = 0
        for opcode in opcodes:
            if opcode(state, instructions) == result:
                like += 1
        if like >= 3:
            c += 1
    print('{} samples behave like 3 opcodes'.format(c))
