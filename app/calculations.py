def check_winner(all_steps, current_step):
    if len(all_steps) < 5:
        return False
    else:
        if find_five_in_row(current_step, (0,1), all_steps):
            return True
        elif find_five_in_row(current_step, (1,0), all_steps):
            return True
        elif find_five_in_row(current_step, (1,1), all_steps):
            return True
        elif find_five_in_row(current_step, (-1,1), all_steps):
            return True
        return False


def find_five_in_row(step, direction, all_steps):
    number_in_row = 1
    for i in check_next_cell(step, direction, all_steps):
        number_in_row += i
    direction = tuple(map(lambda t: t*(-1), direction))
    for i in check_next_cell(step, direction, all_steps):
        number_in_row += i
    if number_in_row >= 5:
        return True
    return False


def check_next_cell(step, direction, all_steps):
    current_step = step
    for i in range(4):
        current_step = tuple(map(lambda t1, t2: t1+t2, current_step, direction))
        if current_step in all_steps:
            yield 1
        else:
            break