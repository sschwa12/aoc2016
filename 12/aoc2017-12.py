from typing import List, Dict, Tuple

from utils import read_file, timer

data = read_file('12')

test_data = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']


class Computer:
    def __init__(self, instruction: str, registers: dict, pc: int = 0):
        self.operation, *self.xy = instruction.split()
        self.registers = registers
        self.pc = pc

    def cpy(self):
        val, reg = self.xy
        val = self.registers.get(val, val)
        # these all need to do get(registers, default=reg)
        self.registers[reg] = int(val)
        self.pc += 1

    def inc(self):
        val = self.xy[0]
        self.registers[val] += 1
        self.pc += 1

    def dec(self):
        val = self.xy[0]
        self.registers[val] -= 1
        self.pc += 1

    def jnz(self):
        reg, val = self.xy
        if self.registers.get(reg, reg) != 0:
            self.pc += int(val)
        else:
            self.pc += 1

    def exec(self):
        eval(f'self.{self.operation}')()
        return self.pc, self.registers


def run_instruction(i: str, r: str, pc: int) -> Tuple[str, Dict[str, int]]:
    computer = Computer(i, r, pc)
    return computer.exec()


@timer
def run(puzzle_input: List[str], c: int = 0) -> int:
    inst = puzzle_input[0]
    reg = dict(zip('abcd', [0, 0, c, 0]))
    pc = 0
    while inst:
        pc, reg = run_instruction(inst, reg, pc)
        try:
            inst = puzzle_input[pc]
        except IndexError:
            return reg['a']


# p1 - 318083
print(run(data))
# p2 - 9227737
print(run(data, 1))

