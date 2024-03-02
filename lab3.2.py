import re

def replace_time(post):
    pattern = r"([01][0-9]|2[0-3])(:[0-5][0-9])(:([0-5][0-9]))?" # Регулярное выражение для поиска времени
    replaced_post = re.sub(pattern, "(TBD)", post) # Замена времени на "(TBD)"
    return replaced_post

# Тесты

# Тест 1
post1 = "Доп. занятие по информатике будет в 09:30:00, а не в 10:00:00"
expected1 = "Доп. занятие по информатике будет в (TBD), а не в (TBD)"
result1 = replace_time(post1)
print(f"Тест 1: Ожидаемый результат: {expected1}, Полученный результат: {result1}")
print()

# Тест 2
post2 = "Занятие начнется в 15:30, а не в 16:00"
expected2 = "Занятие начнется в (TBD), а не в (TBD)"
result2 = replace_time(post2)
print(f"Тест 2: Ожидаемый результат: {expected2}, Полученный результат: {result2}")
print()

# Тест 3
post3 = "Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже точно кончится."
expected3 = "Уважаемые студенты! В эту субботу в (TBD) планируется доп. занятие на 2 часа. То есть в (TBD) оно уже точно кончится."
result3 = replace_time(post3)
print(f"Тест 3: Ожидаемый результат: {expected3}, Полученный результат: {result3}")
print()

# Тест 4
post4 = "Встреча в 10:00 будет перенесена на 11:30"
expected4 = "Встреча в (TBD) будет перенесена на (TBD)"
result4 = replace_time(post4)
print(f"Тест 4: Ожидаемый результат: {expected4}, Полученный результат: {result4}")
print()

# Тест 5
post5 = "Семинар будет проводиться в 13:30 и закончится в 15:30"
expected5 = "Семинар будет проводиться в (TBD) и закончится в (TBD)"
result5 = replace_time(post5)
print(f"Тест 5: Ожидаемый результат: {expected5}, Полученный результат: {result5}")
