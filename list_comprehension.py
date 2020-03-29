# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.

print([x for x in map(str, range(1001)) if '7' in x])

# 2. Взять предложение **Would it save you a lot of time if I just gave up and went mad now?**
# и сделать его же без гласных. **up:** можно оставить в виде списка слов и не собирать строку.

string = "Would it save you a lot of time if I just gave up and went mad now?"
glasnye = "a,A,e,E,i,I,o,O,u,U,y,Y"
print("".join([x for x in string if x not in glasnye]))

# 3. Для предложения The ships hung in the sky in much the same way that bricks don't составить
# словарь, где слову соответствует его длина.

new_string = "The ships hung in the sky in much the same way that bricks don't"
print({x: len(x) for x in new_string.split(' ')})

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).

print({x: y for x in range(1, 1001) for y in range(1, 10) if not x % y})

# 5*. Список всех чисел от 1 до 1000, не имеющих делителей среди чисел от 2 до 9.

print([b for b in range(1, 1001) if b not in [x for x in range(1, 1001) for y in range(2, 10) if not x % y]])
