#def get_summ(one, two, delimiter='&'):
#   one = str(one)
#    two = str(two)
#    return one+delimiter+two
#
#result = get_summ('Learn','Python')
#print(result.upper())



names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']


def find_person(name):
    index = 0
    while index < len(names):
        if names[index] == 'Валера':
            print('Валера нашелся')
        index += 1
    
find_person('Валера')