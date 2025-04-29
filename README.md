# PsychoByte Interpreter

## Description
The `PsychoByte` interpreter is a custom programming language interpreter that processes a grid-based virtual machine. The interpreter reads a program file and grid size as input, then executes the instructions based on the defined semantics. 

## Features
- **Grid-based computation:** Operates on a grid where each cell holds an integer value.
- **Custom instructions:** Includes movement, arithmetic operations, stack manipulation, and conditional jumps.
- **Interactive inputs:** Accepts user input for certain operations.

## Usage
Run the PsychoByte interpreter directly as a terminal executable:

```bash
psychobyte <program_file> <grid_size>
```

### Arguments
1. **`<program_file>`**: Path to the file containing the PsychoByte program.
2. **`<grid_size>`**: The size of the square grid to operate on (e.g., `10` for a 10x10 grid).

### Example
```bash
psychobyte program.txt 10
```

This executes the program `program.txt` on a 10x10 grid.

## Instruction Set
The interpreter supports the following commands:

| Instruction | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| `l`         | Move left on the grid.                                                    |
| `r`         | Move right on the grid.                                                   |
| `u`         | Move up on the grid.                                                      |
| `d`         | Move down on the grid.                                                    |
| `*`         | Multiply the current cell value by an immediate value.                    |
| `/`         | Divide the current cell value by an immediate value.                      |
| `+`         | Add an immediate value to the current cell.                                |
| `-`         | Subtract an immediate value from the current cell.                        |
| `s`         | Push the current cell value onto the stack.                                |
| `p`         | Pop a value from the stack and place it in the current cell.               |
| `c`         | Set flags (`fe`, `fg`, `fl`) based on the current cell value.              |
| `j`         | Jump to a label unconditionally.                                           |
| `>`         | Jump to a label if the `fg` flag (greater) is set.                         |
| `=`         | Jump to a label if the `fe` flag (equal) is set.                           |
| `<`         | Jump to a label if the `fl` flag (less) is set.                            |
| `o`         | Output the ASCII character corresponding to the current cell value.        |
| `i`         | Input a single character and store its ASCII value in the current cell.    |

## Labels
Labels are numeric values embedded in the program and used for jumps (`j`, `>`, `=`, `<`). A label is a sequence of digits, and the interpreter associates it with the position in the program.

## Error Handling
- **Stack underflow:** Raised when attempting to pop from an empty stack.
- **Unknown instruction:** Raised when an invalid instruction is encountered.

## Development
### Dependencies
This script requires Python 3.8 or later.

### Running Tests
To test the interpreter, create sample program files and run them with various grid sizes. Examples:

#### Sample Program: `hello.txt`
```
i+72o+29o+7o+3o+3o+83o
```
Command:
```bash
psychobyte hello.txt 10
```
Expected Output:
```
Hello!
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

