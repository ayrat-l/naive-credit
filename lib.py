def is_creditable(age, salary):
    #Первый тест - проверка на позитив
    """
    >>> is_creditable(30, 40_000)
    True
    >>> is_creditable(20, 40_000)
    False

    >>> is_creditable(70, 40_000)
    False

    >>> is_creditable(30, 10_000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    if age < min_age:
        return False #Early exit

    if age > max_age:
        return False #Early exit

    if salary < min_salary:
        return False
    #В этой точке все проверки пройдены
    return True


    #Так делать не нужно
    if min_age <= age <= max_age and salary >= min_salary:
        return True
    else:
        return False
