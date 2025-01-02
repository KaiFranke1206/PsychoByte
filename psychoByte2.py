import sys

def run(prog_, gs):
    print("Program: ", prog_)
    print("Gridsize: ", gs)
    prog = list(prog_)
    grid = [[0] * gs] * gs
    fe, fg, fl = False
    px, py = 0
    pc = 0
    stack = []

    def wrap(arg, val):
        return arg % val

    def setFlags(val):
        if val == 0:
            fe, fg, fl = True, False, False
        elif val > 0:
            fe, fg, fl = False, True, False
        else:
            fe, fg, fl = False, False, True

    labels = {}
    for i, char in enumerate(prog):
        if char.isdigit():
            labels[char] = i

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
                grid[py][px] *= prog[pc]
            case "/":
                pc += 1
                grid[py][px] /= prog[pc]
            case "-":
                pc += 1
                grid[py][px] -= prog[pc]
            case "+":
                pc += 1
                grid[py][px] += prog[pc]
            case "s":
                stack.append(grid[py][px])
            case "p":
                grid[py][px] = stack.pop()
            case "c":
                setFlags(grid[py][px])
            case "j":
                pc += 1
                pc = labels[prog[pc]]
            case ">":
                pc += 1
                if fg 
                
                

        pc += 1


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        data = file.read().replace('\n', '')
    program = data
    gridSize = int(sys.argv[2])
    run(program, gridSize)
