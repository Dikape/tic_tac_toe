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
    current_step = step
    for i in range(4):
        current_step = tuple(map(lambda t1, t2: t1+t2, current_step, direction))
        if current_step in all_steps:
            number_in_row += 1
        else:
            break
    current_step = step
    for i in range(4):
        current_step = tuple(map(lambda t1, t2: t1 - t2, current_step, direction))
        if current_step in all_steps:
            number_in_row += 1
        else:
            break
    if number_in_row >= 5:
        return True
    return False

# 1. Обираємо точку
# 2. Перевірки вправо/вліво, вверх/вниз, права на ліво діагональ, ліва на право діаг
# 3. Робимо крок від точки, перевіряємо чи є така точка, якщо є вертаємо +1
# 4. Якщо нема крок в іншу сторону і повторяємо 3
#
# По горизонталі крок вбік: (0,1)/(0,-1)
# По вертикалі крок верх/вниз: (1,0)/(-1,0)
#  ліва на право діаг (-1, -1)/(1,1)
# права на ліво діагональ (-1, 1)/(1,-1)