import string

def mov(command : list):
    return command[1], command[2]

def if_loop(location : list):
    location[0] = location[0].split(" ")
    if "==" in location[0]:
        print()
    elif "!=" in location[0]:
        print()
    elif "<=" in location[0]:
        print()
    elif "<" in location[0]:
        print()
    elif ">=" in location[0]:
        if location[0][1] >= location[0][3]:
            return
    elif ">" in location[0]:
        print()

def run(program : list):
    final_list = []
    command_list = {}
    for item in program:
        item = item.split(" ")
        if "MOV" in item:
            x = mov(item)
            command_list[x[0]] = x[1]
        elif "PRINT" in item:
            final_list.append(int(command_list[item[1]]))
        elif "ADD" in item:
            if item[2] in string.ascii_letters:
                command_list[item[1]] = int(command_list[item[1]]) + int(command_list[item[2]])
            else:
                command_list[item[1]] = int(command_list[item[1]]) + int(item[2])
        elif "begin:" in program:
            location = program[program.index("begin:") + 1:program.index("quit:")]
        elif "IF:" in item:
            if_loop(location)
        elif "END" in item:
            return final_list


if __name__ == '__main__':
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)