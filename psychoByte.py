import sys

def run(prog_, gs):
    print("Program: ", prog_)
    print("Gridsize: ", gs)
    prog = list(prog_)
    grid = [[0 for _ in range(gs)] for _ in range(gs)]
    fe, fg, fl = False, False, False  # Correct initialization of flags
    px, py = 0, 0  # Initialize position
    pc = 0  # Program counter
    stack = []

    def wrap(arg, val):
        return arg % val

    def setFlags(val):
        nonlocal fe, fg, fl
        if val == 0:
            fe, fg, fl = True, False, False
        elif val > 0:
            fe, fg, fl = False, True, False
        else:
            fe, fg, fl = False, False, True

    labels = {}
    i = 0
    while i < len(prog):
        if prog[i].isdigit():
            start = i
            while i + 1 < len(prog) and prog[i + 1].isdigit():
                i += 1
            labels[''.join(prog[start:i + 1])] = start

        i += 1

    def get_immediate():
        nonlocal pc
        start = pc
        while pc + 1 < len(prog) and prog[pc + 1].isdigit():
            pc += 1
        return int(''.join(prog[start:pc + 1]))


    while pc < len(prog):
        match prog[pc]:
            case "l":
                px = wrap(px - 1, gs)
            case "r":
                px = wrap(px + 1, gs)
            case "u":
                py = wrap(py - 1, gs)
            case "d":
                py = wrap(py + 1, gs)
            case "*":
                pc += 1
                grid[py][px] *= get_immediate()
            case "/":
                pc += 1
                grid[py][px] //= get_immediate()
            case "-":
                pc += 1
                grid[py][px] -= get_immediate()
            case "+":
                pc += 1
                grid[py][px] += get_immediate()
            case "s":
                stack.append(grid[py][px])
            case "p":
                if stack:
                    grid[py][px] = stack.pop()
                else:
                    raise IndexError("Stack underflow!")
            case "c":
                setFlags(grid[py][px])
            case "j":
                pc += 1
                label = get_immediate()
                pc = labels.get(str(label), pc)
            case ">":
                pc += 1
                label = get_immediate()
                if fg:
                    pc = labels.get(str(label), pc)
            case "=":
                pc += 1
                label = get_immediate()
                if fe:
                    pc = labels.get(str(label), pc)
            case "<":
                pc += 1
                label = get_immediate()
                if fl:
                    pc = labels.get(str(label), pc)
            case "o":
                print(chr(grid[py][px]))
            case "i":
                char = input("Put in a character: ")[0]
                grid[py][px] = ord(char)
            case _:  # Handle invalid instruction
                raise ValueError(f"Unknown instruction: {prog[pc]} at position {pc}")

        pc += 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <program_file> <grid_size>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read().replace('\n', '')
        program = data
        gridSize = int(sys.argv[2])
        run(program, gridSize)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
