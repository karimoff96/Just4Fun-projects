

def arithmetic_arranger(problems):
    def add(a, b):
        return str(int(a) + int(b))

    def diff(a, b):
        return str(int(a) - int(b))

    def get_max_len(lst):
        return len(max(lst, key=len))

    with_answers = False
    if problems[-1] == True:
        problems = problems[0]
        with_answers = True

    new_list = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for item in problems:
        i = item.split()
        len_i = get_max_len(i)

        if i[1] != '+' and i[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if not (i[0].isdigit() and i[2].isdigit()):
            return "Error: Numbers must only contain digits."

        if len(i[0]) > 4 or len(i[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if i[1] == '+':
            n_list = [
                ' '*(len_i+2-len(i[0]))+i[0], i[1] + ' ' *
                (len_i+1-len(i[2]))+i[2], '-'*(len_i+2),
                ' '*(len_i+2-len(add(i[0], i[2]))) + add(i[0], i[2])
            ]

        elif i[1] == '-':
            n_list = [
                ' '*(len_i+2-len(i[0]))+i[0], i[1] + ' ' *
                (len_i+1-len(i[2]))+i[2], '-'*(len_i+2),
                ' '*(len_i+2-len(diff(i[0], i[2])))+diff(i[0], i[2])
            ]

        new_list.append(n_list)

    res = []
    for i in range(4 if with_answers else 3):
        res.append("    ".join([each_one[i] for each_one in new_list]))

    return '\n'.join(res)


print(arithmetic_arranger(
    [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True]))
