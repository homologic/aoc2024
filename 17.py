#!/usr/bin/python3

reg = []

for i in range(3) :
    reg.append(int(input().split()[-1]))


def combo_operand(reg, n) :
    if n < 4 :
        return n
    elif n < 7 :
        return reg[n-4]


def execute_instruction(reg, opcode, operand) :

    if opcode == 0 :
        reg[0] = reg[0] // (2**combo_operand(reg,operand))
    elif opcode == 1 :
        reg[1] = reg[1] ^ operand
    elif opcode == 2 :
        reg[1] = combo_operand(reg,operand) % 8
    elif opcode == 3 :
        if reg[0] != 0 :
            reg[3] = operand
            return
    elif opcode == 4 :
        reg[1] = reg[1] ^ reg[2]
    elif opcode == 5 :
        reg[4].append(combo_operand(reg,operand)%8)
    elif opcode == 6 :
        reg[1] = reg[0] // (2**combo_operand(reg,operand))
    elif opcode == 7 :
        reg[2] = reg[0] // (2**combo_operand(reg,operand))
    reg[3] += 2

input()

program = list(map(int,input().split()[-1].split(",")))
print(program, reg)

reg.append(0)
reg.append([])

def run_machine(reg,program) :
    while reg[3] < len(program) - 1 and len(reg[4]) <= len(program) :
        execute_instruction(reg,program[reg[3]], program[reg[3]+1])
    return reg[4] == program

run_machine(reg,program)
print(",".join(map(str, reg[4])))

i = 0o2415751603465540
reg = [i,0,0,0,[]]
if run_machine(reg,program) :
    print(i)
#print(",".join(map(str, reg[4])))
print(reg[4])
