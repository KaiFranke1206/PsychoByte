
# PsychoByte Programming Language

PsychoByte is a minimalistic, grid-based esoteric programming language that operates on a fixed-size grid. The language uses a single pointer, an infinite stack, and various commands for movement, arithmetic, and control flow.

---

## Features

- **Grid-Based Execution:** Operates on a fixed-size `x * x` grid (defined at runtime).
- **Pointer Movement:** Moves a pointer across the grid.
- **Arithmetic Operations:** Modify cell values using immediate values.
- **Stack Operations:** Supports an infinite stack for advanced computations.
- **Control Flow:** Includes conditional jumps and labels for program logic.
- **Input/Output:** ASCII-based input and output.

---

## Language Commands

### Pointer Movement
- `l` - Move pointer **left**.
- `r` - Move pointer **right**.
- `u` - Move pointer **up**.
- `d` - Move pointer **down**.

The pointer wraps around the grid when reaching edges.

### Arithmetic
- `*value` - Multiply the current cell's value by `value`.
- `/value` - Divide the current cell's value by `value`. Division by zero returns 0.
- `-value` - Subtract `value` from the current cell's value.
- `+value` - Add `value` to the current cell's value.

### Stack Operations
- `s` - Push the current cell's value onto the stack.
- `p` - Pop the top value from the stack into the current cell. Popping from an empty stack returns 0.

### Comparison
- `c` - Compare the current cell's value to zero and set flags:
  - **Zero Flag:** True if the value is `0`.
  - **Positive Flag:** True if the value is greater than `0`.
  - **Negative Flag:** True if the value is less than `0`.

### Control Flow
- **Labels:** `0`, `1`, `2`, `3`, ..., `9` - Define program jump points.
- **Unconditional Jump:** `j(label)` - Jump to a label.
- **Conditional Jumps:**
  - `>(label)` - Jump to a label if the **Positive Flag** is set.
  - `=(label)` - Jump to a label if the **Zero Flag** is set.
  - `<(label)` - Jump to a label if the **Negative Flag** is set.

### Input/Output
- `o` - Output the ASCII representation of the current cell's value.
- `i` - Wait for a single character of input and store its ASCII value in the current cell.

---

## Execution Rules

- **Initialization:** All grid cells are initialized to `0`.
- **Pointer Start:** The pointer starts at the top-left corner of the grid (`0, 0`).
- **Wrapping:** Pointer movement wraps around the grid edges.
- **Arithmetic:** All operations use immediate values and modify the current cell.
- **Invalid Operations:** Return `0`.
- **Stack Behavior:** The stack size is infinite. Popping from an empty stack returns `0`.

---

## Example Program: "Hello, World!"

The following program outputs "Hello, World!":

```plaintext
+72or+101or+108oor+111or+32or+87or+111or+114or+108or+100o
```

- `+72` adds `72` (ASCII for 'H') to the current cell.
- `o` outputs the ASCII character for the current cell's value.
- Repeated arithmetic and output commands produce the desired text.

---

## Running a Program

To execute a PsychoByte program, use the provided Python script:

```python
if __name__ == "__main__":
    grid_size = 12  # Define the grid size
    program = "+72or+101or+108oor+111or+32or+87or+111or+114or+108or+100o"
    run(program, grid_size)
```

---

## License

This project is licensed under the MIT License.
