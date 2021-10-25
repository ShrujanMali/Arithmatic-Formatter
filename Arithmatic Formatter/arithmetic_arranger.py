def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_number = []
    second_number = []
    operator = []
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:
        list1 = problem.split()
        first_number.append(list1[0])
        operator.append(list1[1])
        second_number.append(list1[2])

    # Here checks for * or / operator
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."
      
    # function to more than 4 numbaers
    for i in range(len(first_number)):
        if len(first_number[i]) > 4 or len(second_number[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Check the digits
    for i in range(len(first_number)):
        if not (first_number[i].isdigit() and second_number[i].isdigit()):
            return "Error: Numbers must only contain digits."

    
    for i in range(len(first_number)):
        if len(first_number[i]) > len(second_number[i]):
            first_line.append(" "*2 + first_number[i])
        else:
            first_line.append(" "*(len(second_number[i]) - len(first_number[i]) + 2) + first_number[i])

    for i in range(len(second_number)):
        if len(second_number[i]) > len(first_number[i]):
            second_line.append(operator[i] + " " + second_number[i])
        else:
            second_line.append(operator[i] + " "*(len(first_number[i]) - len(second_number[i]) + 1) + second_number[i])

    for i in range(len(first_number)):
        third_line.append("-"*(max(len(first_number[i]), len(second_number[i])) + 2))

    if answer:
        for i in range(len(first_number)):
            if operator[i] == "+":
                ans = str(int(first_number[i]) + int(second_number[i]))
            else:
                ans = str(int(first_number[i]) - int(second_number[i]))

            if len(ans) > max(len(first_number[i]), len(second_number[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first_number[i]), len(second_number[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems