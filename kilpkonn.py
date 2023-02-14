import turtle

def read_instructions(filename):
    with open(filename, "r") as file:
        instructions = file.readlines()
        return instructions

def parse_instructions(instructions):
    for i in range(len(instructions)):
        instructions[i] = instructions[i].strip().split()
        instructions[i][1] = int(instructions[i][1])
    return instructions

def draw_shape(instructions):
    t = turtle.Turtle()
    for instruction in instructions:
        command, value = instruction
        if command == "edasi":
            t.forward(value)
        elif command == "tagasi":
            t.backward(value)
        elif command == "paremale":
            t.right(value)
        elif command == "vasakule":
            t.left(value)
    turtle.done()

def main():
    filename = "kilpkonn.txt"
    instructions = read_instructions(filename)
    parsed_instructions = parse_instructions(instructions)
    draw_shape(parsed_instructions)

if __name__ == "__main__":
    main()
