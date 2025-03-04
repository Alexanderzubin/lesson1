def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return one+delimiter+two

result = get_summ('Learn','Python')
print(result.upper())

