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
#Так делать не нужно
    if age >= min_age:
        if age <= max_age:
            if salary >= min_salary:
                return True
            else:
                return False
        else:
            return False
    else:
        return False